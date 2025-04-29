from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)  # Name field with a max length of 255 characters
    description = models.TextField()  # Description field for longer text

    def __str__(self):
        return self.name  # String representation of the model
