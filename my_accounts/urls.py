from django.urls import path
from my_accounts import views

app_name='my_accounts'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up')
]
