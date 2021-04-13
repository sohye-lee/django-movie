from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models

class AbstractItem(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class FavoriteBookGenre(AbstractItem):

    class Meta:
        verbose_name = "Favorite Book Genre"
        ordering = ["name"]

class FavoriteMovieGenre(AbstractItem):
    
    class Meta:
        verbose_name = "Favorite Book Genre"
        ordering = ["name"]

class User(AbstractUser):

    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"
    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_SPANISH = "spanish"
    LANGUAGE_CHINESE = "chinese"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_SPANISH, "Spanish"),
        (LANGUAGE_CHINESE, "Chinese"),
    )


    bio = models.TextField(blank=True)
    preference = models.CharField(choices=PREFERENCE_CHOICES, max_length=10, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, blank=True)
    # favorite_book_genre = models.CharField(max_length=20, blank=True)
    favorite_book_genre = models.ManyToManyField("FavoriteBookGenre", blank=True)
    favorite_movie_genre = models.ManyToManyField("FavoriteMovieGenre", blank=True)
