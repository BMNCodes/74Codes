from django import  forms
from .models import Comment


"""
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text=”, label='name')
    class Meta:
        model = User fields = (‘username’,’first_name’ ,’password1′ )
        def __init__(self, *args, **kwargs): super().__init__(*args, **kwargs) delself.fields[‘password2’]
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ('name', 'email', 'body')