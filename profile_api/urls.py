from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profile_api import views

router = DefaultRouter()
router.register('test-viewset', views.HelloViewSet, base_name='test-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('test-view/', views.HellAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
