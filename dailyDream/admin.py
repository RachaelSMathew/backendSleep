from django.contrib import admin
# Register your models here.
from .models import DailyDream

models_list = [DailyDream]
admin.site.register(models_list)