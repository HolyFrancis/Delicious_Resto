from django.forms import ModelForm
from app.models import Menu

class MenuForm(ModelForm):
    
    class Meta():
        model=Menu
        fields='__all__'