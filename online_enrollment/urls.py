from django.urls import path
from .import views

urlpatterns =[
    
    path('account/', views.account, name = 'account'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('profile/', views.profile_view, name='profile'),
    


]   