from django.conf.urls import url
from django.urls import path, include
from userapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'address', views.UserAddressViewSet)
router.register(r'remark', views.UserRemarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]