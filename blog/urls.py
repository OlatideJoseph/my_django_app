from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('olatide-joseph-adeniyi',views.portfolio,name='olatide'),
]