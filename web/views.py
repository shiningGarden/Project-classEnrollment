from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
import requests
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth

def board(request):
    posts = Post.objects.all()
    return render(request, 'board.html', {'posts':posts})

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', {'post':post})

def home(request):
    if request.method == "POST":
        search = request.POST['textarea']
        q1 = Q(professor = search)
        q2 = Q(subject = search)
        result = Lecture.objects.filter(q1 | q2)
        return render(request,'home.html',{"lecture" : result})
    else:
        return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.user = request.user
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('detail', id=post.id)

def update(request, id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/detail/'+str(post.id))
    return render(request, 'update.html', {'result':post})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/board/')

def ratings(request, id):
    lecture = Lecture.objects.get(id=id)
    return render(request, 'ratings.html', {'lecture':lecture})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            signup = Signup()
            signup.std_num = request.POST['std_num']
            signup.major = request.POST['major']
            signup.name = request.POST['name']
            signup.user = user
            signup.save()
            auth.login(request, user)
            return redirect('home')
    return render(request,'signup.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate (request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home') 
        return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def rate(request):
    return render(request, 'rate.html')

def lecture(request, id):
    url = "http://18.214.131.153:5000/course"
    response = requests.get(url)
    data = response.json()['data']
    for i in data:
        lecture = Lecture()
        lecture.subject = i['subject']
        lecture.dept = i['dept']
        lecture.professor = i['professor']
        lecture.instruction_id = i['instruction_id']
        lecture.rq_year = i['rq_year']
        lecture.rq_semester = i['rq_semester']
        lecture.area = i['area']
        lecture.url = i['url']
        lecture.credit = i['credit']
        lecture.class_time = i['class_time']
        lecture.required = i['required']
        lecture.foreigner = i['foreigner']
        lecture.team_teaching = i['team_teaching']
        lecture.mooc = i['mooc']
        lecture.online = i['online']
        lecture.number_of_people = i['number_of_people']
        lecture.note = i['note']
        lecture.save()
    return redirect('/')