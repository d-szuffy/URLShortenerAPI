from django.shortcuts import redirect
from rest_framework import generics
from rest_framework import mixins
from .serializers import URLShortenerSerializer
from .common.utils.utils import create_shortened_url
from .models import URL
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class URLShortenerApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = URLShortenerSerializer

    def get_queryset(self):

        queryset = URL.objects.all()
        url_param = self.request.query_params.get('url')
        slug_param = self.request.query_params.get('slug')

        if url_param is not None:
            queryset = queryset.filter(url=url_param)

        if slug_param is not None:
            queryset = queryset.filter(slug=slug_param)

        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        slug = create_shortened_url(URL)
        serializer = self.get_serializer(data={"url": request.data['url'], "slug": slug})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def url_redirect(request, slugs):
    data = URL.objects.get(slug="http://localhost:8000/" + slugs)
    return redirect(data.url)
