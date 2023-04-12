from django.db import models
from sorl.thumbnail import ImageField


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    text = models.TextField(max_length=140, blank=False, null=False)
    image = ImageField()
    date_view = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
