from . import views
from django.urls import path 
from .views import DeleteRecipeView, UpdateRecipeView

urlpatterns = [
    path("", views.RecipeModelList.as_view(), name="home"),
    path('about/', views.about, name='about'),
    path('detail/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('addrecipe/', views.add_recipe, name='addrecipe'),
    path('recipe_edit/<slug:slug>', views.UpdateRecipeView.as_view(),
         name='recipe_edit'),
    path('recipe_delete/<slug:slug>', views.DeleteRecipeView.as_view(),
         name='recipe_delete'),
]