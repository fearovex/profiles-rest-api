from django.urls import path

from profile_api import views

urlpatterns = [
    path('test/', views.HellAPIView.as_view())
]
