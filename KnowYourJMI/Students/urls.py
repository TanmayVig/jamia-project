from django.urls import path
from . import views

app_name='students'
urlpatterns=[
    path('',views.StudentListView.as_view(), name='students'),
    path('<int:pk>/',views.StudentDetail.as_view(), name='single'),
]
