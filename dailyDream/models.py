from django.db import models

# Create your models here.
class DailyDream(models.Model):
    dreamId = models.AutoField(primary_key=True)
    userNameAddS = models.CharField(max_length=100)
    dreamDate = models.CharField(max_length=100)
    dreamType = models.CharField(max_length=300)
    dreamThing = models.CharField(max_length=900)
