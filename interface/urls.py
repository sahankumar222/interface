"""interface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'), 
    path('students/', views.student_list, name='student_list'),  
    path('students/new/', views.student_create, name='student_create'),  
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'), 
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),  
    path('books/', views.book_list, name='book_list'), 
    path('books/new/', views.book_create, name='book_create'),  
    path('books/edit/<int:pk>/', views.book_edit, name='book_edit'),  
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'), 
     # Home page URL
    
    path('', views.library_list, name='library_list'),  # List all library records
    path('new/', views.library_create, name='library_create'),  # Add new library record
    path('edit/<int:pk>/', views.library_edit, name='library_edit'),  # Edit library record
    path('delete/<int:pk>/', views.library_delete, name='library_delete'),
    path('library/', views.library_list, name='library_list'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)