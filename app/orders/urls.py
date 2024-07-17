from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("api/order", views.OrderView)

urlpatterns = router.urls
