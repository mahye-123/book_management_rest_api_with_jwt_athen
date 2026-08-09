from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Read-only for unauthenticated users, write access requires JWT token
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable Filtering, Searching, and Ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering fields (?category=... & ?author=...)
    filterset_fields = ['category', 'author']

    # Searching fields (?search=...)
    search_fields = ['title', 'author']

    # Ordering fields (?ordering=price or ?ordering=-price)
    ordering_fields = ['title', 'price', 'published_date']
    ordering = ['id']  # Default sorting