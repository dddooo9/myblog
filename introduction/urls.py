from django.urls import path
from . import views #같은 디렉토리 안 views를 가져옴


app_name='introduction'
urlpatterns=[
    path('', views.profile, name="profile"),
]