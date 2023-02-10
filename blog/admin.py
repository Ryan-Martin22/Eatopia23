from django.contrib import admin
from .models import RecipeModel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RecipeModel)
class Admin(SummernoteModelAdmin):
   
    summernote_fields = ('ingredients_list', 'instructions')