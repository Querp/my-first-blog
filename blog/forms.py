from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # fields = ('author', 'title', 'text', 'created_date', 'published_date', 'smaak')
        fields = '__all__'
        widgets = {
            'smaak': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'oninput':'this.nextElementSibling.value = this.value' }),
            'malsheid': forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'oninput':'this.nextElementSibling.value = this.value' }),
        } 
   