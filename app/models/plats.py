from django.db import models
from app.models import Menu

class Plat(models):
    name=models.CharField( max_length=50, null=True)
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    description=models.TextField(max_length=50, null=True)
    prix=models.FloatField()
    disponibilite=models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    