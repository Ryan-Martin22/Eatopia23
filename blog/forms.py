from .models import Comment, RecipeModel
from django import forms


class AddRecipeForm(forms.ModelForm):
    """
    Form to add recipe
    """
    class Meta:
        model = RecipeModel
        fields = [
            'title',
            'excerpt',
            'cooking_time',
            'ingredients_list',
            'instructions',
            'featured_image',
        ]
    
       
    def __init__(self, *args, **kwargs):
        super(AddRecipeForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)