from django.db import models

# Create your models here.
class TweeterScraper(models.Model):
    username = models.CharField(max_length=255)
    tweet_text = models.CharField(max_length=255)
    tweet_date = models.DateTimeField()
    tweet_link = models.URLField()
   