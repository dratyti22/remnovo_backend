from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("api/tag", views.TagsView)
router.register('api/file', views.FileView)
router.register('api/material', views.MaterialView)
router.register('api/description/file', views.DescriptionFileView)

urlpatterns = [
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

urlpatterns += router.urls
