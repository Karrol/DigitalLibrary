from django.conf.urls import url

import librarian.views as views
app_name='librarian'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'index', views.index, name='index'),
    url(r'^librarian_book', views.librarian_book, name='librarian_book'),
    url(r'^librarian_Booktype', views.librarian_booktype, name='librarian_Booktype'),
    url(r'^librarian_borrow', views.librarian_borrow, name='librarian_borrow'),
    url(r'^librarian_history', views.librarian_reser, name='librarian_history'),
    url(r'^librarian_user', views.librarian_user,name='librarian_user'),
    url(r'^librarian_Usertype', views.librarian_usertype, name='librarian_Usertype'),
    url(r'^librarian_ebook', views.librarian_ebook, name='librarian_ebook'),
    url(r'^bookshelf', views.bookshelf, name='bookshelf'),
    url(r'^librarian_CD', views.librarian_CD, name='librarian_CD'),
    url(r'^add_user_to_database', views.add_user_to_database, name='add_user_to_database'),
    url(r'^add_book_to_database', views.add_book_to_database, name='add_book_to_database'),
    url(r'^add_CD_to_database', views.add_CD_to_database, name='add_CD_to_database'),
    url(r'^add_usertype_to_database', views.add_usertype_to_database, name='add_usertype_to_database'),
    url(r'^add_booktype_to_database', views.add_booktype_to_database, name='add_booktype_to_database'),
    url(r'^add_ebook_to_database', views.add_ebook_to_database, name='add_ebook_to_database'),
    url(r'^add_bookshelf_to_database', views.add_bookshelf_to_database, name='add_bookshelf_to_database'),
    url(r'^change_user_to_database', views.change_user_to_database, name='change_user_to_database'),
    url(r'^change_book_to_database', views.change_book_to_database, name='change_book_to_database'),
    url(r'^change_CD_to_database', views.change_CD_to_database, name='change_CD_to_database'),
    url(r'^change_usertype_to_database', views.change_usertype_to_database, name='change_usertype_to_database'),
    url(r'^change_booktype_to_database', views.change_booktype_to_database, name='change_booktype_to_database'),
    url(r'^change_ebook_to_database', views.change_ebook_to_database, name='change_ebook_to_database'),
    url(r'^change_bookshelf_to_database', views.change_bookshelf_to_database, name='change_bookshelf_to_database'),
    url(r'^delete_user', views.delete_user, name='delete_user'),
    url(r'^delete_borrowing_to_database', views.delete_borrowing_to_database, name='delete_borrowing_to_database'),
    url(r'^delete_CD_to_database', views.delete_CD_to_database, name='delete_CD_to_database'),
    url(r'^delete_book_to_database', views.delete_book_to_database, name='delete_book_to_database'),
    url(r'^delete_Usertype_to_database', views.delete_usertype_to_database, name='delete_Usertype_to_database'),
    url(r'^delete_booktype_to_database', views.delete_booktype_to_database, name='delete_booktype_to_database'),
    url(r'^delete_ebook_to_database', views.delete_ebook_to_database, name='delete_ebook_to_database'),
    url(r'^delete_bookshelf_to_database', views.delete_bookshelf_to_database, name='delete_bookshelf_to_database'),

]
