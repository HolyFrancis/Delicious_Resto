from django.forms import ModelForm
from app.models import Plat


class PlatForm(ModelForm):
    class Meta:
        model=Plat
        fields='__all__'
       