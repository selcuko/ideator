from django.forms import ModelForm
from .models import Idea


class IdeaInlineForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['title']

class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description']
        