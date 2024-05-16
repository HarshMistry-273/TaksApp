from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register('task', TaskView)

urlpatterns = [
    path('', root, name='root'),
    path('task/', TaskList.as_view()),
    path('task/<str:pk>/', TaskDetail.as_view()),
    path('get-task/', GetTaskList.as_view()),
    path('get-task/<str:pk>/', GetTaskDetail.as_view()),
    path('login/', LoginView.as_view()),
    # path('logout/', LogoutView.as_view()),
    # path('', include(router.urls)),
]