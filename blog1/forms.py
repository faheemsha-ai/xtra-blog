from django import forms
from .models import Post , Login
from django.forms import TextInput, FileInput , PasswordInput

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['item','image','content']
        widgets = {
            'item':TextInput(
                attrs={
                    "class":"form-control",
                    "name":"name",
                    "type":"text"
                }
            ),
            'image': FileInput(
                attrs={
                    "class":"form-control",
                    "name":"email",
                    "type":"file"
                }
            ),
            'content' : TextInput(
                attrs={
                    "class":"form-control",
                    "name":"message" ,
                    "rows":"6"
                }
            )
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username' , 'password']
        widgets = {
            'username':TextInput(
                attrs={
                        "type":"text" ,
                        "class":"form-control" ,
                        "aria-label":"Sizing example input" ,
                        "aria-describedby":"inputGroup-sizing-default",
                        "placeholder" : "ENTER USERNAME & PASSWORD",
                }
            ),
            'password': PasswordInput(
                attrs={
                        "type":"text",
                        "class":"form-control",
                        "aria-label":"Sizing example input", 
                        "aria-describedby":"inputGroup-sizing-default"
                }
            ),
        }
    