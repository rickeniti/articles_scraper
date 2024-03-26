from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=255, default="None")
    title = models.CharField(max_length=255, default="None")
    short_description = models.TextField(blank=False, null=False, default="")
    url = models.URLField(default="")
    image_url = models.TextField(blank=False, null=False, default="")
    publishing_datetime = models.CharField(max_length=255,blank=False, null=False, default="")
    content = models.TextField(blank=False, null=False, default="")

    class Meta:
        verbose_name = "News Article"  # Singular name for individual objects
        verbose_name_plural = "News Articles"  # Plural name for the model

    def __str__(self):
        return self.title
