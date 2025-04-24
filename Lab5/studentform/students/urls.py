from django.urls import path
from .views import student_entry

urlpatterns = [
    path('', student_entry, name='student_entry'),
]
