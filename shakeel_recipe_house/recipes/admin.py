from django.contrib import admin
from .models import Recipe, RecipeImage  # Import both models

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1  # Number of empty forms to display

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'ingredients', 'instructions')
    inlines = [RecipeImageInline]

@admin.register(RecipeImage)
class RecipeImageAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'image')
    list_filter = ('recipe',)