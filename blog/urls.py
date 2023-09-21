from django.urls import path
from django.views.decorators.cache import cache_page
from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', cache_page(5)(BlogListView.as_view()), name='home'),
    path('view/<int:pk>/', cache_page(5)(BlogDetailView.as_view()), name='view'),
]
