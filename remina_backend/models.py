from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    rate = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, **kwargs):
        item = cls(**kwargs)
        return item
