from django.contrib import admin
from .models import RecipeModel, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RecipeModel)
class Admin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients_list', 'instructions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'recipe', 'created_on',)
    list_filter = ('author', 'created_on')
    search_fields = ('author', 'body')
