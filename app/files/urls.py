from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("api/tag", views.TagsView)
router.register('api/file', views.FileView)
router.register('api/material', views.MaterialView)
router.register('api/description/file', views.DescriptionFileView)

urlpatterns = router.urls
