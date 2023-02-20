from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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
                "recipemodel": recipemodel,
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
                "recipemodel": recipemodel,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
        
        
class RecipeLike(View):
    """
    Likes
    """
    def post(self, request, slug, *args, **kwargs):
        recipemodel = get_object_or_404(RecipeModel, slug=slug)

        if recipemodel.likes.filter(id=request.user.id).exists():
            recipemodel.likes.remove(request.user)
        else:
            recipemodel.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
