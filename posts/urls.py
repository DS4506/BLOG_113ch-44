django.urls import path
posts import views



urlpatterns = [
    path("", views.PostListView.as_view() name="List"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreateView.as_view(), name="new"),
]