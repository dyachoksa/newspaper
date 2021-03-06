"""newspaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.users.views import AuthorDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", include("apps.articles.urls")),
    path("accounts/", include("apps.users.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author"),
    path("search/", include("haystack.urls")),
    path("", include("apps.pages.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
