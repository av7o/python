from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=255)  # Title field with a max length of 255 characters
    author = models.CharField(max_length=255)  # Author field with a max length of 255 characters

    def __str__(self):
        return self.title  # String representation of the model
