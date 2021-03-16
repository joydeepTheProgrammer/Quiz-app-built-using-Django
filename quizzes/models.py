from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100, null=True)
    option3 = models.CharField(max_length=100, null=True)
    option4 = models.CharField(max_length=100, null=True)
    correctAnswer = models.CharField(max_length=100)

    def __str__(self):
        return self.question
