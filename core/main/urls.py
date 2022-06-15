from django.urls import path
from . import views

urlpatterns = [
    path('', views.GaghaparListView.as_view(), name = 'home'),
    path('post_detail/', views.post_detail, name='post_detail'),
    path('home/<int:id>', views.GaghaparDetailView.as_view(), name = 'home_detail'),
    path('login/', views.login_request, name='login'),
    path('logout', views.logout_request, name = 'logout'),
    path('register/', views.register_request, name='register'),
    # path('search/', views.search, name='search'),
]
