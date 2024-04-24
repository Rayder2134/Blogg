from django.urls import path, include

app_name = 'blogicum'

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls')),
]