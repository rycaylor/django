# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login.models import User
from django.contrib import messages
from .models import Author, Book, Review, BookManager
# Create your views here.
def index(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        try:
            context = {
                    'user': User.objects.get(id=int(request.session['logged'])),
                    'books': Book.objects.all(),
                    'reviews':Review.objects.all(),
                    'writers': User.objects.all(),

                }
            return render(request, 'reviewer/index.html', context)
        except:
            return redirect('login:index')

def add(request):
        if 'logged' not in request.session:
            return redirect('login:index')
        else:
            try:
                context = {
                        'user': User.objects.get(id=int(request.session['logged'])),
                        'authors' : Author.objects.all()
                    }
                return render(request, 'reviewer/add.html', context)
            except:
                return redirect('login:index')

def make(request):
        user = int(request.session['logged'])
        book_valid = Book.objects.book_knit(dict(request.POST.items()), user)
        if book_valid['create']:
            book = book_valid['book']
            author = book_valid['author']
            messages.add_message(request, messages.INFO, 'Thanks for adding ' + book.title  + ' by ' + author.name + '. Add another book to review or return to the homepage')
            return redirect('books:add')
        else:
            for error in book_valid['error']:
                messages.add_message(request, messages.INFO, error)
            return redirect('books:add')


def book(request, id):
    num = int(id)
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        try:
            context = {
                    'user': User.objects.get(id=int(request.session['logged'])),
                    'book': Book.objects.get(id=num),
                    'reviews':Review.objects.filter(book_id = num),

                }
            return render(request, 'reviewer/book.html', context)
        except:
            return redirect('login:index')



def add_review(request):
        user = int(request.session['logged'])
        review_valid = Review.objects.review_knit(dict(request.POST.items()), user)
        if review_valid['create']:
            messages.add_message(request, messages.INFO, 'Thanks for adding a review')
            return redirect('books:index')
        else:
            for error in review_valid['error']:
                messages.add_message(request, messages.INFO, error)
            return redirect('books:index')

def thanks(request, id):
    num = int(id)
    user = int(request.session['logged'])
    review_delete = Review.objects.review_delete(user, num)
    return redirect('books:index')

def profile(request, id):
    num = int(id)
    context = {
        'user' : User.objects.get(id=num),
        'reviews' : Review.objects.filter(user_id=num),
    }
    return render(request, 'reviewer/profile.html', context)
