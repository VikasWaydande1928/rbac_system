from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin-only/', views.admin_only_view, name='admin_only'),
    path('moderator-only/', views.moderator_only_view, name='moderator_only'),
    path('user-only/', views.user_only_view, name='user_only'),
]