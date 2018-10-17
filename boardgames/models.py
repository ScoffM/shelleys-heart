from django.db import models
from django.core.validators import MinValueValidator
# from django.core.validators import MaxValueValidator


class Game(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    playtime = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField()
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    players = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:100]+"..."
