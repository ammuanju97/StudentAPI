from django.urls import path
from . views import(
    StudentProfileView, StudentHome, StudentsList, StudentAcademicView
)
urlpatterns = [
    path('student-profile/', StudentProfileView.as_view(), name = 'student-profile'),
    path('student-home/', StudentHome.as_view(), name = 'student=home'),
    path('student-list/', StudentsList.as_view(), name = 'student-list'),
    path('student-academic/', StudentAcademicView.as_view(), name = 'student-academic'),
]