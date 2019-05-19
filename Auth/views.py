from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class MmvbLoginView(LoginView):
    template_name = 'Auth/login.html'


class MmvbLogoutView(LogoutView):
    pass
