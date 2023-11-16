
from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name="recipes-home"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create', RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name="recipes-delete"),
]