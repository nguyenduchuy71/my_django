from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'polls'
CACHE_TIME = 5*60

urlpatterns = [
    path(r'', cache_page(CACHE_TIME)(views.IndexView.as_view()), name='index'),
    path(r'<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path(r'search/', views.PostSearchView.as_view(), name='search'),
    path(r'mypost/', cache_page(CACHE_TIME)(views.PostViewByUser.as_view()), name='mypost'),
    path(r'sendmail/', views.SenMailView.as_view(), name='sendmail'),
    path(r'create/', views.CreatePostView.as_view(), name='create'),
    path(r'<int:post_id>/comment/', views.CreateCommentView.as_view(), name='comment'),
    path(r'<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path(r'<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
]
