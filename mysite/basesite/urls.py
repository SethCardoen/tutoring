from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeview, name='homeview'),
    path('<int:profile_id>/profile/', views.profileview, name='profile'),
    path('<int:profile_id>/search/', views.searchview, name='search'),
    path('<int:profile_id>/notes/', views.notesview, name='notes'),
]
