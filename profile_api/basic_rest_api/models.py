from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.email