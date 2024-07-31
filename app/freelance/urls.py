from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("api/freelance", views.OrderFreelanceView)

urlpatterns = router.urls
