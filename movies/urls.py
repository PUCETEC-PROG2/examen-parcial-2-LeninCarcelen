from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/<int:movie_id>/", views.movies, name="movies"),
    path("user/<int:user_id>/", views.user, name="user"),
    path("add_movies/", views.add_pokemon, name="add_movies"),
    path("edit_movie/<int:movie_id>", views.edit_movies, name="edit_movies"),
    path("delete_movies/<int:movie_id>", views.delete_movies, name="delete_movies"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/<int:user_id", views.edit_user, name="edit_user"),
    path("delete_user/<int:trainer_id>", views.delete_user, name="delete_user"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]