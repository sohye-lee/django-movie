from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "bio",
        "language",
        "preference",
    )

    list_filter = UserAdmin.list_filter + (
        "language",
        "preference",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "additional_information", {
                "fields": (
                "bio",
                "language",
                "preference",
                "favorite_book_genre",
                "favorite_movie_genre",
                )
            }
        ),
    )

    filter_horizontal = (
        "favorite_book_genre",
        "favorite_movie_genre",
    )