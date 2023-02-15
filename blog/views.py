from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import RecipeModel


class RecipeModelList(generic.ListView):
    model = RecipeModel
    queryset = RecipeModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = RecipeModel.objects.filter(status=1)
        recipemodel = get_object_or_404(queryset, slug=slug)
        comments = recipemodel.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipemodel.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipemodel,
                "comments": comments,
                "liked": liked,
            },
        )
        
        


