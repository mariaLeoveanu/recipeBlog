from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from recipe.models import Recipe
from users.forms import UserSignUpForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile


def signup(request):
    if request.method == "POST":
        form_user = UserSignUpForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('login')
    else:
        form_user = UserSignUpForm()

    return render(request, 'users/signup.html', {'user_form': form_user})


class UserDetailsProfile(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(UserDetailsProfile, self).get_context_data(**kwargs)
        context['user_recipes'] = Recipe.objects.filter(author=kwargs.get('object').user).order_by('-date_posted')
        print(kwargs)
        return context


@login_required
def update_user_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user_profile', pk=request.user.profile.id)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/user_update.html', context)




