from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('/api/menu-items',views.MenuItemView.as_view()),
    path('/api/menu-items/<int:pk>',views.SingleMenuItemView.as_view()),
    path('home', views.index, name='home'),
    path('api-token-auth/', obtain_auth_token),
    path('see',views.example)
    
]