from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #example: /polls/
    path('', views.IndexView.as_view(), name="index"),
    #example: /polls/5/ 
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    #example: /polls/5/results 
    path('<int:pk>/results', views.ResultView.as_view(), name="results"),
    #example: /polls/5/vote
    path('<int:question_id>/vote', views.vote, name="vote")
    #<int:question_id> es el parámetro question_id que se le pasa a cada función dentro de views.py
]