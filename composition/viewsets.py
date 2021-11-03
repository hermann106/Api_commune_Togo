from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly  
from django.shortcuts import get_object_or_404
from .serializers import (
    Region,
    Prefecture,
    Commune,
    Canton,
    Village,
    Quartier,

    RegionSerializer,
    PrefectureSerializer,
    CommuneSerializer,
    CantonSerializer,
    VillageSerializer,
    QuartierSerializer
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins


class RegionViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class PrefectureViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Prefecture.objects.all()
    serializer_class = PrefectureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class CommuneViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    permission_classes([IsAuthenticated])
    permission_classes = [IsAuthenticatedOrReadOnly]



class CantonViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Canton.objects.all()
    serializer_class = CantonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class VillageViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class QuartierViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]