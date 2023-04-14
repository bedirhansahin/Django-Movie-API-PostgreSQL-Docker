from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import *


admin.site.site_header = 'Movie API Admin Page'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'gender', 'birth_date', 'is_active']
    search_fields = ['username']
    search_help_text = "You can search by username"
    list_filter = ['gender', 'is_active', 'is_staff']
    list_per_page = 10
    ordering = ['date_joined']
    readonly_fields = ['username', 'email']


class MovieInline(admin.TabularInline):
    model = Movie
    extra = 0


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_id', 'movie_name', 'director', 'imdb']
    search_fields = ['movie_name', 'director', 'genre']
    search_help_text = "You can search by movie name, director name or category"
    list_filter = ['director', 'genre', 'country']
    list_per_page = 10
    readonly_fields = ['movie_id']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    search_help_text = "You can search by director name"
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']

    inlines = [MovieInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    search_help_text = "You can search by director name"
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']

