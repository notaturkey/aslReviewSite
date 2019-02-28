from django.db import models

# Create your models here.
class word(models.Model):
    random_word = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.random_word + ': ' + self.url