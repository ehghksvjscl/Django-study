from django import forms
from .models import Post

import re

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message','photo','tag_set','is_public']

    def clean_message(self):
        data = self.cleaned_data.get("message")
        if data:
            data = re.sub(r'[a-zA-Z]+','',data)
        return data
    
