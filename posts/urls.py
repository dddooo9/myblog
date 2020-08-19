from django.urls import path
from .views import * # *은 views에 있는 모든 함수를 가져옴.

app_name = "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('<int:id>', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"), 
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
]