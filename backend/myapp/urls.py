from django.urls import path
from .views import UserCreate, UserList, UserDetail, login, login_page

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', login, name='login'), 
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('login_page/', login_page, name='login-page'), 
]
