from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('topic/<int:pk>/',views.SubBlogDetailView.as_view(),name = 'subtopic_home')
]