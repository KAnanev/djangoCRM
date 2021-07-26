from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('<int:pk>', views.UserView.as_view(), name='profile'),
    path('get_telegram_id', views.get_telegram_id),
    path('', views.redirect_to_user_page, name='accounts')
]
