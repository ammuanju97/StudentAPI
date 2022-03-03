from django.urls import path
from . views import(
    StudentProfileView, StudentHome, StudentsList
)
urlpatterns = [
    path('student-profile/', StudentProfileView.as_view(), name = 'student-profile'),
    path('student-home/', StudentHome.as_view(), name = 'student=home'),
    path('student-list/', StudentsList.as_view(), name = 'student-list'),
]