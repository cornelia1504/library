"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from libraryapp.views import vw_home, vw_book, vw_book2, vw_book3, vw_books, \
    vw_book4, vw_books2, vw_books3, vw_books4, vw_book_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vw_home),
    path('book/', vw_book),
    path('book2/', vw_book2),
    path('book3/<int:bookid>', vw_book3),
    path('books/', vw_books),
    path('book4/<int:bookid>', vw_book4, name='book4'),
    path('books2/', vw_books2),
    path('books3/', vw_books3),
    path('books4/', vw_books4),
    path('book_search_form/', vw_book_form),

]
