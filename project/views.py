from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from .forms import *


def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.all()
    model = BlogModel.objects.filter(
        Q(category__name__contains=q) |
        Q(title__icontains=q)
        )
    page = Paginator(model, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    if request.method == 'POST':
        email = request.POST.get('email')
        news_feed = NewsFeedModel(email=email)
        news_feed.save()
        return redirect('/')
    context = {'categories': categories, 'page': page}
    return render(request, 'main/index.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "You're Successful Registered")
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
    context = {}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def profile(request, pk):
    person = User.objects.get(id=pk)
    blog = person.blogmodel_set.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=person)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=person.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', pk=person.id)
    else:
        u_form = UserUpdateForm(instance=person)
        p_form = ProfileUpdateForm(instance=person.profilemodel)
    context = {'person': person, 'u_form': u_form, 'p_form': p_form, 'blogs': blog}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def edit_blog(request, pk):
    model = BlogModel.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogUpdateForm(request.POST or None, instance=model)
        form.save()
        return redirect('/')
    else:
        form = BlogUpdateForm(instance=model)
    context = {'form': form}
    return render(request, 'main/edit_blog.html', context)


@login_required(login_url='login')
def delete_blog(request, pk):
    model = BlogModel.objects.get(id=pk)
    if request.method == 'POST':
        model.delete()
        return redirect('/')
    return render(request, 'main/delete.html', {})


@login_required(login_url='login')
def blog_details(request, pk):
    model = BlogModel.objects.get(id=pk)
    comment = model.commentmodel_set.all()
    count = comment.count()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.blog = model
            instance.save()
            return redirect('blog_details', pk=model.id)
    else:
        form = CommentForm()
    context = {'model': model, 'comments': comment, 'count': count, 'form': form}
    return render(request, 'main/details.html', context)


@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = CreateBlogForm()
    if request.method == 'POST':
        c_form = CategoryForm(request.POST or None)
        if c_form.is_valid():
            c_form.save()
            return redirect('/')
    else:
        c_form = CategoryForm()
    context = {
        'form': form,
        'c_form': c_form
    }
    return render(request, 'main/create_blog.html', context)
