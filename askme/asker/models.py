from django.db import models
from django.conf import settings
# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_SER_MODEL,
        on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class Question(models.Model):
    author = models.ForeignKey(
        to=Progile,
        on_delete=models.CASCADE)
    title = models.CharFields(max_lenght=128)
    created_at = models.DateTimeField()

class QuestionManager(models.Model):
    def new(self):
        return self.order_by('-created_at')
