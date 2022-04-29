from rest_framework import viewsets
from .models import Song
from .serializers import SongSerializer

class SongView(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
