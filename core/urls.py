from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),  # Utiliza LogoutView.as_view()
    path('register/', views.register_view, name='register'),
]
