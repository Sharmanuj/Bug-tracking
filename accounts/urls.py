from django.urls import path
from accounts.views import UserCreateView, UserUpdateView

urlpatterns = [
    path('usercreate/', UserCreateView.as_view(), name='usercreate'),
    path('userupdate/<int:user_pk>', UserUpdateView.as_view(), name='userupdate'),
]
