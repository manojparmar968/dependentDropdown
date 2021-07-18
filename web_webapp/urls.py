from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', Contact_view.as_view()),
    path('',DropDown,name='DropDown'),
    path('load-list/', load_list, name='ajax_load_list'),
    path('load-district', load_district, name='ajax_load_district'),
    path('list/',index,name='index'),
    path('load-courses/', load_courses, name='ajax_load_courses'),
]