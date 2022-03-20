from django.forms import ModelForm
from .models import RoomPost


class RoomPostForm(ModelForm):
    class Meta:
        model = RoomPost
        fields = '__all__'
