from django.db import models

# Create your models here.
class Bts(models.Model):
    name = models.CharField(max_length=500)
    work = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.id}--{self.name}"
    