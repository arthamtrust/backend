from django.db import models


# Create your models here.
class Gallery(models.Model):
    """
    Model for gallery. Cards with title and thumbnail
    along with a link to google album
    """

    title = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title
