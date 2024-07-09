# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('register/student/', StudentRegisterView.as_view(), name='student_register'),
    path('register/teacher/', TeacherRegisterView.as_view(), name='teacher_register'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
