from django.db import models
from core.models import UserProfile
from Services.models import Post

class Portfolio(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)