from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('members/', views.index, name='index'),
    path('pmembers/', views.pindex, name='pindex'),
    # path('lvmembers/', login_required(views.lvindex.as_view()), name='lvindex'),
    path('lvmembers/', views.lvindex.as_view(), name='lvindex'),
    path('members/add/', views.add, name='add'),
    path('members/add/addrecord/', views.addrecord, name='addrecord'),
    path('members/delete/<int:id>', views.delete, name='delete'),
    path('members/update/<int:id>', views.update, name='update'),
    path('members/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]