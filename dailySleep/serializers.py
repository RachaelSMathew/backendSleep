from rest_framework import serializers
from .models import DailySleep


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySleep
        fields = ('sleepId',
                  'userAddS',
                  'start',
                  'end')
