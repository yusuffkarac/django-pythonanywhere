from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    is_bought = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
