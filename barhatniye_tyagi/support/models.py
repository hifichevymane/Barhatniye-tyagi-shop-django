from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return f"name: ({self.name}), email: ({self.email}), message: ({self.message})"
    