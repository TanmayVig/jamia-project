from django.urls import path
from . import views

app_name='students'
urlpatterns=[
    path('',views.StudentList.as_view(), name='studentlist'),
    path('<username>/',views.StudentDetail.as_view(), name='studentdetail'),
]
