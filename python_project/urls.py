"""python_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from recipe import views as recipe_view
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe_view.RecipeListView.as_view(template_name='recipe/home.html'),name='home'),
    path('recipe/<int:pk>/', recipe_view.RecipeDetailView.as_view(template_name='recipe/details.html'), name='details'),
    path('new/', recipe_view.RecipeCreateView.as_view(), name='new'),
    path('recipe/<int:pk>/update/', recipe_view.RecipeUpdateView.as_view(), name='update'),
    path('recipe/<int:pk>/delete/', recipe_view.RecipeDeleteView.as_view(), name='delete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', user_views.signup, name='signup'),
    path('search/', recipe_view.SearchResultsView.as_view(), name='search'),
    path('profile/<int:pk>/', user_views.UserDetailsProfile.as_view(template_name='users/user_profile.html'), name='user_profile'),
    path('type/<slug:recipe_type>/', recipe_view.RecipeTypeListView.as_view(), name='recipe_type'),
    path('profile/update/', user_views.update_user_profile, name='update_profile')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
