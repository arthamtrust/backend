from rest_framework import viewsets

from .models import Post
from .paginations import CharityPostPagination, EventPostPagination
from .serializers import CharityPostSerializer, EventPostSerializer


# Create your views here.
class CharityPostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.filter(kind="charity").all()
    serializer_class = CharityPostSerializer
    pagination_class = CharityPostPagination


class EventPostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.filter(kind="event").all()
    serializer_class = EventPostSerializer
    pagination_class = EventPostPagination
