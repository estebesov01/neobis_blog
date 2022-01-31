from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=25)
    email = forms.EmailField(label='Ваша почта')
    to = forms.EmailField(label='Почта получателя')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Комментарии')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField(label='Запрос')
