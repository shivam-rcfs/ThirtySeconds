from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Team(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(_("Team Name"), max_length=50)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)
    name = models.CharField(_("Player Name"), max_length=50)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return f'{self.name}'


class CategoryData(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    words = models.CharField(_("Words"), max_length=200)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return f'{self.words}'


class Result(models.Model):
    winner = models.ForeignKey(to=Team, on_delete=models.CASCADE)
    points = models.IntegerField(_("Points"))
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return f'{self.winner.name} with {self.points} points'


class GuessedAnswer(models.Model):
    guessed_by = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    guessed_answer = models.ForeignKey(to=CategoryData, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guessed_by.name} with {self.guessed_answer.words} points'
