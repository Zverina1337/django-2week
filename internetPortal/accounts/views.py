from urllib import request
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
                
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def password_reset():
    return render(
        request,
        'registration/password_reset.html'
    )
def profile(request):
    return render(
        request,
        'registration/profile.html'
    )

def logged_out(request):
    return render(
        request,
        'registration/logged_out.html'
    )