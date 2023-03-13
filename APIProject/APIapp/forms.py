from django import forms
from .models import Student,Movie

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'