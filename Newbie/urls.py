from django.urls import path

from . import views

app_name='Newbie'
urlpatterns = [
    path('<int:course_id>/', views.details, name='detail'),
    path('', views.courses,name='Home-page'),
    path('<int:course_id>/your_choice/', views.your_choice,name='yourchoice'),
]
