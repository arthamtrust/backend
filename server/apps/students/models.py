from django.db import models


class Student(models.Model):
    """
    Student's adopted by Artham
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()

    def __str__(self):
        return self.name
