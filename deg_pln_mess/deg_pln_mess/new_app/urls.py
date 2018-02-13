from django.urls import path
from . import views

app_name = 'new_app'

urlpatterns = [
    #/new_app/
    path('', views.IndexView.as_view(), name = 'index'),
    path('eligible/', views.EligibleView.as_view(), name = 'eligible'),
    path('taken/', views.TakenView.as_view(), name = 'taken'),
    ]
