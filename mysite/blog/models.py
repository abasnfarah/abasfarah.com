from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', default=author)
    title = models.CharField(max_length = 140)
    body = models.TextField()
    created_date = models.DateTimeField( default=timezone.now)
    date = models.DateTimeField()

    def publish(self):
        self.date=timezone.now()
        self.save()

    def author(self):
        return "Abas Farah"

    def __str__(self):
        return self.title
