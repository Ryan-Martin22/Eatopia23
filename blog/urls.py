from . import views
from django.urls import path 

urlpatterns = [
    path("", views.RecipeModelList.as_view(), name="home"),
    path('detail/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('addrecipe/', views.add_recipe, name='addrecipe'),
]