from django.db import models

class City(models.Model):
    # creator will go here when users are created
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    #creator = models.ForgeinKey(null=True, default=True, on_delete=models.CASCADE)
    name = models.TextField(max_length=120)
    city = models.ForeignKey(to='City', on_delete=models.CASCADE, null=True, default=True, related_name='restaurant')

    def __str__(self):
        return self.name
