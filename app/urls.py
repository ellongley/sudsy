from django.urls import path
from . import views

urlpatterns = [
 path('', views.rowestats, name='rowestats'),
 path('github',views.github, name='github'),
]

#path('timeseries',views.timeseries, name='timeseries'),
#path('timeseries',views.factors, name='factors')
