from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # ex: /polls/5/
    path('detail/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('vote/', views.vote, name='vote'),
]