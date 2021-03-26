from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from django.contrib.auth.forms import UserCreationForm
from userapp.serializers import UserSerializer, UserAddressSerializer, UserRemarkSerializer
from userapp.models import User, UserAddress, UserRemark

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAddressViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

class UserRemarkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = UserRemark.objects.all()
    serializer_class = UserRemarkSerializer
