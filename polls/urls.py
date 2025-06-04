from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Это для главной страницы /polls/
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/results/', views.results, name='results'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
]