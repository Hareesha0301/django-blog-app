from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexView.as_view(), name="blog" ),
    path("posts", views.AllPostsView.as_view(), name="posts" ),
    path("posts/<slug:slug>", views.IndividualPostView.as_view(), name="post-detail-page" ),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]