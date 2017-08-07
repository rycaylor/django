# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.



class BookManager(models.Manager):
    def book_knit(self, postData, user):
        results = {'create': True, 'add':False, 'error': [], 'book':None, 'author':None}
        if postData['author_add'] != '':
            author_try = Author.objects.filter(name=postData['author_add'])
            if len(author_try)>0:
                results['create'] = False
                results['add'] = False
                results['error'].append('We already have that author availible for you, please select that author and resubmit your review')
            else:
                results['add'] = True
                author = postData['author_add']
                print author
        if results['add'] == False:
            author = postData['author_made']

        if postData['book'] == '':
            results['create'] = False
            results['error'].append('Please give us a book title so that we can add your review')
        elif postData['book'] != '':
            grab_author = Author.objects.filter(name=author)
            for author in grab_author:
                if len(Book.objects.filter(author_id=author.id).filter(title=postData['book']))>0:
                    results['create'] = False
                    results['error'].append('We already have that book availible for review please see our homepage to review it there link is in progress')
            else:
                book = postData['book']
        if postData['review'] == '':
            results['create'] = False
            results['error'].append('We would love to hear from you please provide some information')
        else:
            review = postData['review']
        if results['create']:
            rating = postData['rates']
            if results['add']:
                make_author = Author.objects.create(name = author)
                make_book = Book.objects.create(title=book, author_id=make_author.id)
                make_review = Review.objects.create(content=review, rating = rating, book_id=make_book.id, user_id=user)

                make_author.save()
                make_book.save()
                make_review.save()

                results['book'] = make_book
                results['author'] = make_author
            else:
                grab_author = Author.objects.get(name=postData['author_made'])
                make_book = Book.objects.create(title=book, author_id=grab_author.id)
                make_review = Review.objects.create(content=review, rating = rating, book_id=make_book.id, user_id=user)

                make_book.save()
                make_review.save()

                results['book'] = make_book
                results['author'] = grab_author
        return results



class ReviewManager(models.Manager):
    def review_knit(self, postData, user):
        results = {'create':True, 'error':[], 'user':None}
        if postData['review'] == '':
            results['create'] = False
            results['error'].append('Please add add text if you wish to review this book')
        elif results['create']:
            user = User.objects.get(id=user)
            content = postData['review']
            book = postData['book']
            rate = postData['rates']
            make_review = Review.objects.create(content=content, rating=rate, book_id=book, user_id=user.id)

            make_review.save()

            results['user'] = user

        return results

    def review_delete(self, user, num):
        delete = Review.objects.get(id=num).delete()
        return delete

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name = 'author_name')
    objects = BookManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    content = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    book = models.ForeignKey(Book, related_name = 'book_title')
    user = models.ForeignKey(User, related_name = 'user_name')
    objects = ReviewManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
