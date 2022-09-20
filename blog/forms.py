from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'updated_on', 'created_on', 'likes', 'slug']
        labels = {
            'excerpt': 'Method',
            'content': 'Ingredients'
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
        labels = {
            'excerpt': 'Method',
            'content': 'Ingredients'
        }
