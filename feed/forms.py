from django import forms

class PostForm(forms.Form):
    title = forms.CharField(initial='Title')
    text = forms.CharField(label="Description")
    image = forms.FileField()
   
