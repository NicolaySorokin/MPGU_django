from django.urls import path
from .views import StaticPageView

app_name = 'pages'

urlpatterns = [
    path('<slug:slug>/', StaticPageView.as_view(), name='static_pages'),
]
