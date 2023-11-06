# authentication/views.py

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = 'registration/login/'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    pass
    # No template needed for logout

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

class CustomRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from login.forms import AdminLoginForm
class CustomLoginView_new(LoginView):

    template_name = 'registration/adminlogin.html'
    success_url = reverse_lazy('admin_dashboard')  # Redirect to user dashboard on successful user login
    authentication_form = AuthenticationForm
    extra_context = {'admin_login_form': AdminLoginForm()}


  # <script src="https://apis.google.com/js/platform.js" async defer></script>
  #   <meta name="google-signin-client_id" content="7588829440-18h2gt9ku6nvudj6brf88294l81fctg1.apps.googleusercontent.com">