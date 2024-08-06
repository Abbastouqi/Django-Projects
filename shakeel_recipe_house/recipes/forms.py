from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'category']

class RecipeImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = RecipeImage
        fields = ('image', )