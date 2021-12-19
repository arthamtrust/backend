from django.db import models


class Post(models.Model):
    """
    Model for Charity or Event Post
    """

    POST_KINDS = [(kind, kind) for kind in ["charity", "event"]]

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(max_length=10, choices=POST_KINDS)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "-published_date",
        ]
