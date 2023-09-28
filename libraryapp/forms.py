from django import forms
from .models import Book

class FormSearchBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title',)