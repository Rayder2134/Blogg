from django.urls import path, include

app_name = 'blogicum'

urlpatterns = [
    path('', include('blog.urls')),
    path('', include('pages.urls')),
]
