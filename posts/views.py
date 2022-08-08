# posts/views.py
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
 
class PostViewSet(viewsets.ModelViewSet): # ModelViewSet provides both a List view and Detail view
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
