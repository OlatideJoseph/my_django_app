from django.urls import path
from . import views
urlpatterns=[
    path('',views.IndexListView.as_view(),name="index"),
    path('olatide-joseph-adeniyi',views.portfolio,name='olatide'),
]