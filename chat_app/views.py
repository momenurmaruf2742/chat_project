# chatapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import RegistrationForm
from django.urls import reverse_lazy
from chat_app.models import User
from .forms import RegistrationForm,LoginForm

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration

    def form_valid(self, form):
        # Log the user in after successful registration
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or the chat page
                return redirect('chat')  # Replace 'chat' with the actual chat URL
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})