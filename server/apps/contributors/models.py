from datetime import date

from django.db import models


# Create your models here.
class Contributor(models.Model):
    """
    Lists all contributors for each month
    """

    contribution_date = models.DateField(default=date.today)
    contributor_list = models.TextField()

    def __str__(self):
        return self.contribution_date.strftime("%B, %Y")

    class Meta:
        ordering = [
            "-contribution_date",
        ]
