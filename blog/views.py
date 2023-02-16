from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import RecipeModel
from .forms import CommentForm


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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
        
    def post(self, request, slug, *args, **kwargs):
        queryset = RecipeModel.objects.filter(status=1)
        recipemodel = get_object_or_404(queryset, slug=slug)
        comments = recipemodel.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipemodel.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipemodel
            comment.author = request.user
            comment.save()

        else:
            comment_form = CommentForm()

   
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipemodel,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )