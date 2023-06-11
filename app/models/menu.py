from django.db import models

class Menu(models.Model):
    image=models.ImageField(upload_to="app/static/app/images/")
    title=models.TextField(max_length=50)
    description=models.TextField(max_length=50)
    
    def __str__(self):
        return self.title