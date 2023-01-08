from django import forms
from .models import Post


class FormUpdatePost(forms.ModelForm):
    post_title = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Title',
                                                               'class': 'form-control',
                                                               }))
    post_content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Post
        fields = ['post_title', 'post_content']
