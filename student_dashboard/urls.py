from django.urls import path
from . views import(
    StudentProfileView
)
urlpatterns = [
    path('student-profile/', StudentProfileView.as_view(), name = 'student-profile'),
]