from django.urls import path
from django.views.decorators.cache import cache_page
from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='view'),
]
