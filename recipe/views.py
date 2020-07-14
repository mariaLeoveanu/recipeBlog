from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RecipeForm
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']
    paginate_by = 5


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/details.html'
    context_object_name = 'recipe'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    success_url = '/'
    form_class = RecipeForm

    def get_object(self, queryset=None):
        obj = super(RecipeUpdateView, self).get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404()
        return obj


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/'
    context_object_name = 'recipe'

    def get_object(self, queryset=None):
        obj = super(RecipeUpdateView, self).get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404()
        return obj


class SearchResultsView(ListView):
    model = Recipe
    template_name = 'recipe/home.html'
    context_object_name = 'recipes'
    paginate_by = 5
    ordering = ['-date_posted']

    def get_queryset(self):
        query = self.request.GET.get('search-bar')
        recipe_list = Recipe.objects.filter(name__icontains=query)
        return recipe_list


class RecipeTypeListView(ListView):
    model = Recipe
    template_name = 'recipe/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']

    def get_queryset(self):
        requested_type = self.kwargs['recipe_type']
        filtered_recipes = Recipe.objects.filter(type=requested_type).order_by('-date_posted')
        return filtered_recipes

