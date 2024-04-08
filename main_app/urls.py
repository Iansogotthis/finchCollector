from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='finches'),
    path('all_finches/', views.all_finches_view, name='all_finches'),
    path('finch/<int:finch_id>/', views.finch_detail, name='finch_detail'),

]