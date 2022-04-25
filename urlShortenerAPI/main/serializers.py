from rest_framework import serializers
from .models import URL


class URLShortenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = URL
        fields = '__all__'
