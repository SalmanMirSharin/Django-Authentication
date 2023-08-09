from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('signup/',views.signup, name='singup'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('pass_change/', views.Pass_change, name='paschange'),
    path('profile/',views.profile, name='profile')
]
