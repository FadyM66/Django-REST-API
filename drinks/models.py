from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name + ' ' + str(self.price)
    