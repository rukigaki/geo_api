from django.urls import path

from .views import PointAPIView, PointMessageAPIView, PointSearchListAPIView, MessageSearchAPIView


urlpatterns = [
    path("points/", PointAPIView.as_view()),
    path("points/search/", PointSearchListAPIView.as_view()),

    path("points/messages/", PointMessageAPIView.as_view()),
    path("points/messages/search/", MessageSearchAPIView.as_view())

]