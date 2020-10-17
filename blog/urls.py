from django.urls import path, include
from . import views
app_name = 'blog'

urlpatterns = [
    path('',views.IndexPage.as_view(),name='index'),
    path('post_create',views.PostCreateView.as_view(),name='post_create'),
    path('post_list',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>',views.post_detail,name='post_detail'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_remove'),
    path('analysis/<int:pk>/',views.AnalysisDetailView.as_view(),name='analysis_detail')
]
