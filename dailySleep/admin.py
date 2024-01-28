from django.contrib import admin

# Register your models here.
from .models import DailySleep

models_list = [DailySleep]
admin.site.register(models_list)