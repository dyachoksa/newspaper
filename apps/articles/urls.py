from django.urls import path

from .views import ArticleListView, ArticleDetailView

app_name = "articles"

urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("by-category/<slug:slug>/", ArticleListView.as_view(), name="by_category"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="detail"),
]
