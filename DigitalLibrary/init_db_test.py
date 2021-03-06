import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DigitalLibrary.settings')

import django

django.setup()

import json
import argparse
import random,string
import datetime
import codecs
import os.path as op
from search.models import book_info ,bookshelf_info ,bookEntity_info,book_shumu
from readerCenter.models import Borrowing,moneyTask
from login.models import Reader
from django.contrib.auth.models import User

from faker import Factory

fake = Factory.create('zh_CN')

def init_reader_data(amount=50):
    for i in range(amount):
        u = User.objects.get_or_create(username=fake.free_email())[0]
        u.set_password('password')
        u.save()
        r = Reader.objects.get_or_create(user=u, name=fake.name(), email=u.username)[0]
        r.balance = round(random.random() * 100, 2)
        r.inTime = datetime.date.today()
        r.save()

def getRandomSet(bits):
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    total_set = num_set + char_set

    value_set = "".join(random.sample(total_set, bits))

    return value_set


def init_bookentity_data(amount=100):
    for i in range(amount):
        bookIntime = datetime.date.today() + datetime.timedelta(random.randint(1, 30))
        quantity = random.randint(0, 7)
        bookshelfid = random.choice(bookshelf_info.objects.all())
        searchID = getRandomSet(10)
        randfloor = random.randint(1, 3)
        libname = ['文理馆中文图书', '江安馆社科图书', '文理馆基藏库', '文理馆中文图书', '文理馆工具书', '文理馆中文图书,明远文库']
        location = random.choice(libname)
        returned_flag = True

        if random.randint(1, 100) % 2 == 0:
            returned_flag = False

        if returned_flag:
            b = bookEntity_info.objects.create(

                quantity=quantity,
                bookIntime=bookIntime,
                bookshelfid=bookshelfid,
                booksearchID=searchID,
                location=location
            )
            b.save()



def init_book_data():
    with codecs.open('books.json', 'r', 'utf-8') as f:
        books = json.load(f)

    for b in books:
        if 'content_description' in b and b['content_description']:
            print(b)
            try:
                B = \
                book_info.objects.get_or_create(ISBN=b['ISBN'], title=b['name'], author=b['author'], press=b['press'],
                                                page=b['page'], price=b['price'])[0]
                B.description = b['content_description']

                B.cover = b['cover']
                B.bookID= random.choice(bookEntity_info.objects.all())
                B.save()
            except KeyError:
                continue

def init_book_shumu_data():
    with codecs.open('sichuanUniLib_books.json', 'r', 'utf-8') as f:
        books = json.load(f)

    for b in books:
        if 'ISBN' in b and b['ISBN']:
            print(b)
            try:
                B=book_shumu.objects.get_or_create(id=int(b['id']),ISBN=b['ISBN'], title=b['title'], author=b['author'], press=b['press'],
                                                page=b['page'], price=b['price'])[0]
                B.category = b['catolog']
                B.cover = b['cover']
                B.location = b['libnname']
                B.searchID = b['searchID']
                B.publishTime = b['publishTime']
                B.quantity = b['Holding']
                B.contentTable = b['contentTable']
                B.language = b['language']
                B.publishInfo = b['publishInfo']
                B.pubLocation = b['pubLocation']
                B.contentBrief = b['contentBrief']
                B.carrierMorphology = b['carrierMorphology']
                B.banci = b['banci']
                B.page = b['page']
                B.zaiti = b['zaiti']
                B.length = b['length']
                B.bookID= random.choice(bookEntity_info.objects.all())
                B.save()
            except KeyError:
                continue
                

def init_borrowing_data(amount=50):
    for i in range(amount):
        reader = random.choice(Reader.objects.all())
        isbn = random.choice(book_info.objects.all())
        issued = datetime.date.today() + datetime.timedelta(random.randint(1, 30))
        due_to_returned = issued + datetime.timedelta(30)
        date_returned = issued + datetime.timedelta(random.randint(1, 40))
        returned_flag = True

        if random.randint(1, 100) % 2 == 0:
            returned_flag = False

        if returned_flag:
            if (date_returned - issued).days > 30:
                fine = ((date_returned - issued).days - 30) * 0.1
            else:
                fine = 0

            b = Borrowing.objects.create(
                reader=reader,
                ISBN=isbn,
                date_issued=issued,
                date_due_to_returned=due_to_returned,
                date_returned=date_returned,
                amount_of_fine=fine,
            )
            b.save()
        else:

            if reader.max_borrowing > 0 and isbn.bookID.quantity > 0:
                b = Borrowing.objects.create(
                    reader=reader,
                    ISBN=isbn,
                    date_issued=issued,
                    date_due_to_returned=due_to_returned
                )

                reader.max_borrowing -= 1
                isbn.bookID.quantity -= 1
                reader.save()
                isbn.save()
                b.save()

def init_moneyTask_data(amount=50):
    for i in range(amount):
        reader = random.choice(Reader.objects.all())
        issued = datetime.date.today() - datetime.timedelta(random.randint(1, 30))
        
        task = ['馆际互借', '文印', '论文出版']
        b = moneyTask.objects.create(
                reader=reader,
                price=random.uniform(0,100),
                inTime=issued,
                taskname=random.choice(task),
        )
        b.save()




if __name__ == '__main__':
    #init_reader_data()
    init_bookentity_data()
    #init_book_data()
    #init_borrowing_data(amount=50)
    init_book_shumu_data()
    #init_moneyTask_data()