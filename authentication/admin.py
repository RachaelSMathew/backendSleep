from django.contrib import admin
from .models import CustomUser

models_list = [CustomUser]
admin.site.register(models_list)
