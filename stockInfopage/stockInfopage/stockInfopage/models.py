from django.db import models

from jsonfield import JSONField


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

 
class Book(models.Model):
    isbn = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    memo = models.TextField()
 
    def __str__(self):
        return self.title


class Daily(models.Model):
    code = models.CharField(max_length=128)
    date = models.DateTimeField()
    open = models.BigIntegerField()
    high = models.BigIntegerField()
    low = models.BigIntegerField()
    close = models.BigIntegerField()
    diff = models.BigIntegerField()
    volume = models.BigIntegerField()
    def __str__(self):
        return self.title