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
