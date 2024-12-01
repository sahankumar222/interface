from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from testapp.models import Student
from testapp.forms import StudentForm
from testapp.models import Book
from testapp.forms import BookForm
from testapp.models import Library
from testapp.forms import LibraryForm
from django.utils.timezone import now

def homepage(request):
    return render(request, 'testapp/homepage.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'testapp/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'testapp/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'testapp/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

#Book interface

def book_list(request):
    books = Book.objects.all()
    return render(request, 'testapp/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'testapp/book_form.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'testapp/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'testapp/book_confirm_delete.html', {'book': book})

#library interface
def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'testapp/library_list.html', {'libraries': libraries})

def library_create(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm()
    return render(request, 'testapp/library_form.html', {'form': form})

def library_edit(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=library)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm(instance=library)
    return render(request, 'testapp/library_form.html', {'form': form})

def library_delete(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        library.delete()
        return redirect('library_list')
    return render(request, 'testapp/library_confirm_delete.html', {'library': library})

def my_view(request):
    return render(request, 'homepage.html', {'timestamp': now().timestamp()})