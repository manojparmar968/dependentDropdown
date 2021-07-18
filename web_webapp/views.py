from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Q
from .models import *

def DropDown(request):
    country = CountryList.objects.all()
    return render(request, 'web_app/contact.html', {'country':country,})

def load_list(request):
    country_id = request.GET.get('country')
    state_obj = StateList.objects.filter(country_id=country_id).order_by('name')
    # state_id = request.GET.get('state')
    # print('state_id',state_id)
    # district_obj = DistrictList.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'web_app/state_list.html', {'state_obj':state_obj, })

def load_district(request):
    state_id = request.GET.get('state')
    print('state_id',state_id)
    district_obj = DistrictList.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'web_app/district_list.html',{'district_obj':district_obj,})

def index(request):
    program = Programming.objects.all()
    d = {'program': program}
    return render(request,'index.html',d)

def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})