from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
	title = models.CharField(max_length=250)
	author = models.CharField(max_length=250)
	date = models.DateField()
	body = RichTextUploadingField(blank=True)

# Create your models here.
