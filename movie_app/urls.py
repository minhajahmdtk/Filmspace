from django.urls import path
from . import views



urlpatterns = [
  path('',views.index,name='index'),
  path('home', views.home, name='home'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('register',views.register,name='register'),
  path('movies',views.movies,name='movies'),
  path('series',views.series,name='series'),
  path('add_movie_watchlist/<int:movie_id>/', views.add_movie_watchlist, name='add_movie_watchlist'),
  path('add_series_watchlist/<int:series_id>/', views.add_series_watchlist, name='add_series_watchlist'),
  path('movie_watchlist/', views.movie_watchlist, name='movie_watchlist'),
  path('series_watchlist/', views.series_watchlist, name='series_watchlist'),
  path('remove_series_watchlist/<int:ws_id>/', views.remove_series_watchlist, name='remove_series_watchlist'),
  path('admin_login',views.admin_login,name='admin_login'),
  path('admin_home',views.admin_home,name='admin_home'),
  path('add_movie',views.add_movie,name='add_movie'),
  path('admin_manage_movies/', views.admin_manage_movies, name='admin_manage_movies'),
  path('update_movie/<int:p_id>/',views.update_movie,name='update_movie'),
  path('delete_movie/<int:delete_mov>',views.delete_movie,name='delete_movie'),
  path('add_series',views.add_series,name='add_series'),
  path('admin_manage_series/', views.admin_manage_series, name='admin_manage_series'),
  path('update_series/<int:up_id>/',views.update_series,name='update_series'),
  path('delete_series/<int:delete_ser>',views.delete_series,name='delete_series'),

  

]
