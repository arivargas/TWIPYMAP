from django.db import models

# Create your models here.

from django.utils.timezone import now
class Location(models.Model):
    address = models.CharField(max_length=200)
    lat = models.IntegerField()
    lon = models.IntegerField()
    link = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('twipymap_location_detail', (), {'pk': self.pk})

class Contact(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.ForeignKey('Location')
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('twipymap_contact_detail', (), {'pk': self.pk})
