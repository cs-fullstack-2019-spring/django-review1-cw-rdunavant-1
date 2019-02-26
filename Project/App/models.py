from django.db import models


# Create your models here.
class Page(models.Model):
    page_number = models.IntegerField()

    def __str__(self):
        return self.page_number
