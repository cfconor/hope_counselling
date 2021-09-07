from django.urls import path

from . import views

urlpatterns = [
    path('book-now', views.book_now, name='book_now'),
    path('show-available-times', views.show_available_times, name='show-available-times')
]