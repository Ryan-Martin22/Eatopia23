from django.contrib import admin
from .models import Recipe_model
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe_model)
class Admin(SummernoteModelAdmin):
    
    summernote_fields = ('content')


