from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Recipe_model(models.Model):
    """
    Model for recipe
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipe_author')
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    cooking_time = models.IntegerField(default=1,
                                       validators=[
                                                   MinValueValidator(1),
                                                   MaxValueValidator(120)
                                                   ])
    ingredients_list = SummernoteTextField()
    instructions = SummernoteTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes',
                                   blank=True)

    class Meta:
        """
        Order the recipes in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Returns the number of likes on a post
        """
        return self.likes.count()
