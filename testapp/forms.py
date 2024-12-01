from django import forms
from testapp.models import Student
from testapp.models import Book
from testapp.models import Library
import re
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'photo', 'video']
        
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z\s]+$', name):  # Allows alphabets and spaces only
            raise forms.ValidationError("Student name should contain only alphabets and spaces.")
        return name
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publication', 'year']
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z0-9\s]+$', name):  # Allows alphabets, numbers, and spaces
            raise forms.ValidationError("Book name should contain only alphabets, numbers, and spaces.")
        return name

        
class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['student', 'book', 'start_date', 'end_date']