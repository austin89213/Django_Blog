from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}))
    class Meta():
        model = Post
        fields = ('title','content')
        
class CommentForm(forms.ModelForm):

    content = forms.CharField(label='Say Something',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Content'}))
    class Meta():
        model = Comment
        fields =('content',)

