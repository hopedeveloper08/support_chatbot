from django.db import models
from django.contrib.auth.models import User

class Bussiness(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    support_info = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
