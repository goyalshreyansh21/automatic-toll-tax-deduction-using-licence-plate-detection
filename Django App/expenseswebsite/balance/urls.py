from django.urls import path
from balance.views import balance

urlpatterns = [
    # other URL patterns
    path('balance/', balance, name='balance'),
]
