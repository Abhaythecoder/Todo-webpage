# models.py
from django.db import models


class Todopage(models.Model):
    tasks = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.tasks
