from django.urls import path
from .views import DreamView

#To call the view, we need to map it to a URL
urlpatterns = [
    path('dailydreams/', DreamView.as_view()),
    path('dailydreams/<int:pk>/', DreamView.as_view())
]