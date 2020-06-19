from django.db import models


class Example(models.Model):
    img = models.ImageField(upload_to="media", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
