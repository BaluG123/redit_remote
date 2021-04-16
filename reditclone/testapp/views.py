from django.shortcuts import render,get_object_or_404,redirect
from testapp.models import Post
from testapp import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_listview(request):
    post_list=Post.objects.all()
    return render(request,'testapp/post_list.html',{'post_list':post_list})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,title=post,status="publish",publish__year=year,publish__month=month,publish__day=day)
    return render(request,'testapp/post_detail.html',{'post':post})

@login_required
def post_create(request):
    form=forms.CreateForm()
    if request.method=='POST':
        form=forms.CreateForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('/redit')
    return render(request,'testapp/post_create.html',{'form':form})

def SignUpView(request):
    form=forms.SignUpform()
    if request.method=='POST':
        form=forms.SignUpform(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return redirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

def logout_view(request):
    return render(request,'testapp/logout.html')    
