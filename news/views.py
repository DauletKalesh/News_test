from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import News, Category, Tag
from .serializers import NewsSerializer, CategorySerializer, TagSerializer, UserNewsSerializer
from rest_framework import filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    # without prefix (search for containing words)
    search_fields = ['title', 'content', 'tags__name', 'category__name']

    def get_permissions(self):
        if self.request.user.is_staff:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    
    def get_serializer_class(self):
        if not self.request.user.is_staff:
            return UserNewsSerializer
        return self.serializer_class
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_published=True)
        return queryset
    
    @method_decorator(cache_page(60*15))  # Cache 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]
