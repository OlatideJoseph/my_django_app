from django.urls import path
from . import views
urlpatterns=[
    path("post/<int:pk>",views.BlogDetailView.as_view(),name='post_details'),
    path('',views.IndexListView.as_view(),name="index"),
    path('olatide-joseph-adeniyi',views.PortfolioView.as_view(),name='olatide'),
]