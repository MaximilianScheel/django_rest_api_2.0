import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )

    def _str_(self):
        return self.title