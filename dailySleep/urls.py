from django.urls import path
from .views import SleepView

urlpatterns = [
    path('dailysleep/', SleepView.as_view()),
    path('dailysleep/<int:pk>/', SleepView.as_view())
]