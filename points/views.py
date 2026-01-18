from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Point, Message
from .serializers import PointSerializer, MessageSerializer
from .utils import get_points_in_radius


class PointAPIView(generics.CreateAPIView):
    queryset = Point.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PointSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PointSearchListAPIView(generics.ListAPIView):
    serializer_class = PointSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return get_points_in_radius(self.request)


class PointMessageAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessageSearchAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        points_in_radius = get_points_in_radius(self.request)
        return Message.objects.filter(point__in=points_in_radius)
