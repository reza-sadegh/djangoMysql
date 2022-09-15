from .models import Members
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator



@login_required(login_url='/accounts/login/')
def home(request):
  current_user = request.user
  grps=request.user.groups.all()
  if(current_user.groups.filter(name='manager').exists()):
    ismanager='is manager'
  else:
    ismanager = 'is not manager'
    return redirect('/about/')

  return render(request,'home.html',{'today': datetime.today(),'uname': current_user,'grps':grps,'ismanager':ismanager})

@login_required(login_url='/accounts/login/')
def index(request):
  current_user = request.user
  grps=request.user.groups.all()
  if(current_user.groups.filter(name='manager').exists()):
    mymembers = Members.objects.all()
    return render(request, 'index.html', {'mymembers': mymembers,})
  else:
    return redirect('/accounts/login/')
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))

def about(request):
  courses=[
    {"id":"1","name":"c#"},
    {"id":"2","name":"python"},
    {"id":"3","name":"java"},
    {"id":"4","name":"c++"},
    {"id":"5","name":"c"},
    {"id":"6","name":"sql"},
  ]
  return render(request,'about.html',{"courses":courses})

class lvindex(LoginRequiredMixin,ListView):
  model = Members
  paginate_by = 3
  template_name = 'lvindex.html'
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'

@login_required(login_url='/accounts/login/')
def pindex(request):
  mymembers = Members.objects.all()
  page_num = request.GET.get('page', 1)
  paginator = Paginator(mymembers, 3)
  page_obj = paginator.page(page_num)
  return render(request, 'pindex.html', {'page_obj': page_obj})


  return render(request, 'index.html', {'mymembers': mymembers,})


