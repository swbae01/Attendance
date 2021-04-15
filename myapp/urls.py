from django.urls import path
from .views import main_views

app_name = 'myapp'

urlpatterns = [
    path('', main_views.main, name='main'),
    path('lecture_load', main_views.lecture_load, name='lecture_load'), # Load lecture_load.html
]