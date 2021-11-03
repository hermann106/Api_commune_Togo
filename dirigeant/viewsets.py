from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import (
    Leader,
 
    LeaderSerializer,
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins

class LeaderViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
