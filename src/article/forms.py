# -*- coding: utf-8 -*-

from models import Comments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["comments_text"]
        widgets = {
            'comments_text': forms.Textarea(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }