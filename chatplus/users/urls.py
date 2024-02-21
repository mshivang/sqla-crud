from django.urls import path

from .views import Users, UserDetail

app_name = "users"
urlpatterns = [
    path("", Users.as_view(), name="index"),
    path("<str:pk>", UserDetail.as_view(), name="detail")
]