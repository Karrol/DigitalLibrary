from django.shortcuts import render,redirect
from django.http import  HttpResponse
from test1.models import reader_info,book_info,bookborrow_info,bookback_info
from . import forms
import hashlib
# Create your views here.
def hash_code(s, salt='mysite'):#
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    return render(request, 'test1/librarian.html')

def librarian_book(request):
    books = book_info.objects.all()
    new_book_form = forms.NewBookForm()
    change_book_form = forms.ChangeBookForm
    context = {
        'users': books,
        'new_user_form':new_book_form,
        'change_user_form':change_book_form,
    }
    return render(request, 'test1/librarian_book.html',context)

def librarian_CD(request):
    return render(request, 'test1/librarian_CD.html')

def librarian_bookshelf(request):
    return render(request, 'test1/librarian_booktype.html')

def librarian_ebook(request):
    return render(request, 'test1/librarian_ebook.html')

def librarian_usertype(request):
    return render(request, 'test1/librarian_usertype.html')

def librarian_booktype(request):
    return render(request, 'test1/librarian_booktype.html')

def librarian_borrow(request):
    return render(request, 'test1/librarian_borrow.html')

def librarian_history(request):
    return render(request, 'test1/librarian_history.html')

def librarian_user(request):
    users = reader_info.objects.all()
    new_user_form = forms.NewUserForm()
    change_user_form = forms.ChangeUserForm()
    context = {
        'users': users,
        'new_user_form':new_user_form,
        'change_user_form':change_user_form,
    }
    return render(request, 'test1/librarian_user.html',context)

def add_user_to_database(request):
    new_user_form = forms.NewUserForm(request.POST)
    if new_user_form.is_valid():
        username = new_user_form.cleaned_data['username']
        password = new_user_form.cleaned_data['password']
        readertypeName = new_user_form.cleaned_data['readertypeName']
        bookNumber = new_user_form.cleaned_data['bookNumber']
        email = new_user_form.cleaned_data['email']
        sex = new_user_form.cleaned_data['sex']
        new_reader = reader_info()
        new_reader.Name = username
        new_reader.Password = password  # 使用加密密码
        new_reader.readertypeName = readertypeName
        new_reader.bookNumber = bookNumber
        new_reader.email = email
        new_reader.Sex = sex
        new_reader.save()
        return redirect("librarian_user")

def change_user_to_database(request):
    if request.method == 'post':
        change_user_form = forms.ChangeUserForm(request.POST)
        if change_user_form.is_valid():
            oldusername = change_user_form.cleaned_data['oldusername']
            username = change_user_form.cleaned_data['username']
            password = change_user_form.cleaned_data['password']
            readertypeName = change_user_form.cleaned_data['readertypeName']
            bookNumber = change_user_form.cleaned_data['bookNumber']
            email = change_user_form.cleaned_data['email']
            sex = change_user_form.cleaned_data['sex']
            change_user = reader_info.objects.get(Name = oldusername)
            if change_user:
                change_user.update(Name = username,Password = password,readertypeName = readertypeName,bookNumber = bookNumber,email = email,Sex = sex)
            return redirect("librarian_user")

def delete_user(request):
    reader_info.objects.get(Name = request.GET.get("userName")).delete()
    return redirect("librarian_user")
