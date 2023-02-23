from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import RecipeModel
from .forms import CommentForm
from .forms import AddRecipeForm


class RecipeModelList(generic.ListView):
    model = RecipeModel
    queryset = RecipeModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = RecipeModel.objects.filter(status=1)
        recipemodel = get_object_or_404(queryset, slug=slug)
        comments = recipemodel.comments.order_by("-created_on")
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
        comments = recipemodel.comments.order_by("-created_on")
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


@login_required
def add_recipe(request):
    """
    Add recipe page
    """
    recipe_form = AddRecipeForm()
    print(request.method)
    if request.method == "POST":
        recipe_form = AddRecipeForm(request.POST, request.FILES)
        print(recipe_form.is_valid())
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.title = recipe_form.title.title()
            recipe_form.author = request.user
            recipe_form.status = 1
            recipe_form.save()
            return redirect('home')

    return render(request, 'add_recipe.html', context={'recipe_form':
                  recipe_form})


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


class UpdateRecipeView(UpdateView):
    """
    Edit recipe
    """
    model = RecipeModel
    form_class = AddRecipeForm
    template_name_suffix = '_update_form'
    template_name = 'update_recipe.html'
    success_url = '/'


class DeleteRecipeView(DeleteView):
    """
    Delete Recipe
    """
    model = RecipeModel
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')


def about(request):
    """
    Renders about page
    """
    return render(request, 'about.html')
