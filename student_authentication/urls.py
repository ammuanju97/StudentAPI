from django.urls import path
from .views import StudentRegisterView, StudentLogin
urlpatterns = [
    path('student-register/', StudentRegisterView.as_view(), name ='register'),
    path('student-login/', StudentLogin.as_view(), name='login'),
]
