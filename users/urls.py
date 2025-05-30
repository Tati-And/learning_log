from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    # страница входа
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'  # поиск шаблона в users/templates/registration/login.html
        ),
        name='login'
    ),
    # страница выхода
    path(
        'logout/',
        auth_views.LogoutView.as_view(),          # по умолчанию ищет users/templates/registration/logged_out.html
        name='logout'
    ),

    # Registration page.
    path('register/', views.register, name='register'),
]
