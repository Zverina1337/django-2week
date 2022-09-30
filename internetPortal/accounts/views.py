from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .forms import UserRegistrationForm, ApplicationCreateForm
from django.views import generic
from .models import Application
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy

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

def password_reset(request):
    return render(
        request,
        'registration/password_reset.html'
    )
def profile(request):
    return render(
        request,
        'registration/profile.html'
    )

class view_applications(generic.ListView):
    model = Application
    paginate_by = 3
    def get_queryset(self):
        return Application.objects.filter(user__exact=self.request.user.id)

class create_application(CreateView):
    model = Application
    fields = ('title', 'desc', 'img')
    
    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.save()
       
        return super().form_valid(form)

class detail_application(DetailView):
    model = Application
    template_name = 'accounts/application_detail.html'

class delete_application(DeleteView):
    model = Application
    success_url = reverse_lazy('profile_applications')