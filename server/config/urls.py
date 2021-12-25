from apps.contributors.views import ContributorViewSet
from apps.gallery.views import GalleryViewSet
from apps.posts.views import CharityPostViewSet, EventPostViewSet
from apps.students.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"students", StudentViewSet, basename="student")
router.register(r"charities", CharityPostViewSet, basename="charity")
router.register(r"events", EventPostViewSet, basename="event")
router.register(r"gallery", GalleryViewSet, basename="gallery")
router.register(r"contributors", ContributorViewSet, basename="contributor")


urlpatterns = router.urls
