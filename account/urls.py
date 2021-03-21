from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import CustomerCreate, CustomerViewSet


app_name = 'account'

urlpatterns = [
    path('register/', CustomerCreate.as_view(), name='register'),
    path('login/', LoginView.as_view(
        template_name='common/register.html',
        extra_context={'site_header': 'ГАМБИТ'},
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('customers/', CustomerViewSet.as_view({'get': 'list'}), name='customers')
]
