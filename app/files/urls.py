from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("api/tag", views.TagsView)
router.register('api/file', views.FileView)

urlpatterns = router.urls
