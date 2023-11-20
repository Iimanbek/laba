from django.urls import path
from .views import manga_list_view, manga_list_detail_view

urlpatterns = [
    path('film_list/', manga_list_view),
    path('film_list/<int:id>/', manga_list_detail_view),
]
