from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)


class Participant(models.Model):
    livesInLA = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(1)])

class QuestionResponse(models.Model):
    dateTime = models.DateTimeField(default = timezone.now)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    answer = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(1)])
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
