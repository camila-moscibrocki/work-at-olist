from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.api.viewsets import BookViewSet
from authors.api.viewsets import AuthorViewSet


router = routers.DefaultRouter()
"""
Uses the viewsets as parameters for register
"""
router.register(r'books', BookViewSet, basename="authors")
router.register(r'authors', AuthorViewSet, basename='books')

"""
Includes routers for urls
"""
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
