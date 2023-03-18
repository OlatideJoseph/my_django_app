from django.urls import path
from . import views
urlpatterns=[
    path("post/<int:pk>",views.BlogDetailView.as_view(),name='post_details'),
    path("post/<int:pk>/delete",views.BlogDeleteView.as_view(),name='delete_post'),
    path("post/<int:pk>/edit",views.BlogUpdateView.as_view(),name='edit_post'),
    path('',views.IndexListView.as_view(),name="index"),
    path('olatide-joseph-adeniyi',views.PortfolioView.as_view(),name='olatide'),
    path('create',views.BlogCreateView.as_view(),name='create-post'),
]