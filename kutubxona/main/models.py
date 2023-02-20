from django.db import models


# Create your models here.
class BookData(models.Model):
    name = models.CharField(max_length=150)
    writer = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.CharField(max_length=200)

    def __str__(self):
        return self.name