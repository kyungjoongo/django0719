from django import forms
from django.forms import models

from .models import Post
from .models import ContentModel

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)




'''content모델 폼입니다'''
class ContentModelForm(forms.ModelForm):
    class Meta:
        model = ContentModel
        fields = ('title', 'file', 'author')

    # def __init__(self, *args, **kwargs):
    #     # super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False