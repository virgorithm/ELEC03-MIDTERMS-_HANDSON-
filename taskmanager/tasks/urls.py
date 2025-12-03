from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/complete/<int:task_id>/", views.complete_task, name="complete_task"),
]
