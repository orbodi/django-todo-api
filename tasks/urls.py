from django.urls import path  
from .views import Tasks, TaskDetail, hello_world 
  
urlpatterns = [
    path("", Tasks.as_view()),   
    path("<str:pk>", TaskDetail.as_view()),
    path("hello", hello_world, name="hello")
]
