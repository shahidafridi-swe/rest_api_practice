from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=17)
    subject = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
