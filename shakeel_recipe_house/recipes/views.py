from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm
from django.forms import modelformset_factory

def home(request):
    return render(request, 'home.html')

def recipe_list(request, category):
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipe_list.html', {'recipes': recipes, 'category': category})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    ImageFormSet = modelformset_factory(RecipeImage, form=RecipeImageForm, extra=3)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=RecipeImage.objects.none())
        
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = RecipeImage(recipe=recipe, image=image)
                    photo.save()
            
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
        formset = ImageFormSet(queryset=RecipeImage.objects.none())
    
    return render(request, 'add_recipe.html', {'form': form, 'formset': formset})