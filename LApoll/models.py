from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)

class QuestionResponse(models.Model):
    answer = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(1)])
    rating = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(9)])
     
class Participant(models.Model):
    response = models.ManyToManyField(QuestionResponse)
