from django.urls import path
from . import views
from .views import (
	SongDetailView,
	InstrumentalDetailView,
	VideoDetailView,

	)


urlpatterns = [
    path('songs/', views.songs, name='songs'),
    path('song/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    path('instrumentals/', views.instrumentals, name='instrumentals'),
    path('instrumental/<int:pk>/', views.InstrumentalDetailView.as_view(), name='instrumental-detail'),
    path('videos/', views.videos, name='videos'),
    path('video/<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
]