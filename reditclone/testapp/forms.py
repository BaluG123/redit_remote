from django import forms
from testapp.models import Post
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['name','image','video','caption','title','status','tags']

class SignUpform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
