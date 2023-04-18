from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from django_countries.fields import CountryField

from uuid import uuid4

from .models_choices import *


class User(AbstractUser):
    birth_date = models.DateField(_("birth date"), null=True, blank=True,)
    gender = models.CharField(_("gender"), max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=155, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Director(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=155, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Director, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.UUIDField(
        _("id"),
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False
    )
    movie_name = models.CharField(_("movie name"), max_length=255)
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        verbose_name=_("director"),
        related_name='movies'
    )
    genre = models.ManyToManyField(Genre, verbose_name=_("genre"), related_name='movies')
    country = CountryField(multiple=True, countries=SomeCountries)
    production_year = models.PositiveIntegerField(_("production year"), choices=YEAR_CHOICES)
    duration = models.PositiveIntegerField(null=True, blank=True)
    imdb = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    story_line = models.TextField(_("story line"))

    def __str__(self):
        return self.movie_name


class CommentAndScore(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comment_score')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_score')
    comment = models.TextField(_("comment"))
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(_("created_at"), auto_now=True)

    class Meta:
        unique_together = ('movie', 'owner')
        verbose_name = 'Comment and Score'
        verbose_name_plural = 'Comments and Scores'

    def __str__(self):
        return self.comment

