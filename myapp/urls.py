from django.urls import path
import myapp.views as my_views

urlpatterns = [
    path("", my_views.post_list, name='post-list'),
    path("<int:pk>", my_views.post_detail, name='post-details')
]
