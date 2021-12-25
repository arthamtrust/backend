from datetime import date

from django.db import models


# Create your models here.
class Contributor(models.Model):
    """
    Lists all contributors for each month
    """

    contribution_date = models.DateField(default=date.today)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    def __str__(self):
        date = f"{self.contribution_date.month}, {self.contribution_date.year}"
        return f"{self.name} : {date}"

    class Meta:
        ordering = [
            "-contribution_date",
            "name",
        ]
