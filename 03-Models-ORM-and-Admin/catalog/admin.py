from django.contrib import admin
from .models import Author, Genre, Book

# Register your models here.

# these other classes are allowing us to 
# control the Models from the Admin Page
# we do that by using ModelAdmin 
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # for managing the Author table in the Admin page 
    list_display = ("first_name", "last_name", "birth_year")
    search_fields = ("first_name", "last_name")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year", "isbn")
    list_filter = ("publication_year", "genre")
    search_fields = ("title", "author__last_name", "isbn")