from django.urls import path
from .views import StudentRegisterView, StudentLogin
urlpatterns = [
    path('register/', StudentRegisterView.as_view(), name ='register'),
    path('login/', StudentLogin.as_view(), name='login'),
]
