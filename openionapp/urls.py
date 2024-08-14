from django.urls import path
from openionapp.views import PostOpenion

urlpatterns = [
    path('post/', PostOpenion.as_view(), name="post_openion")
]