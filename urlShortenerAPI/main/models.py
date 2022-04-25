from django.db import models

# Create your models here.


class URL(models.Model):

    url = models.URLField(max_length=300)
    slug = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.url} has been shortened to {self.slug}'
