from apps.contributors.views import (
    contributors_by_year,
    contributors_by_year_and_month,
    create_contributor,
)
from apps.posts.views import CharityPostViewSet, EventPostViewSet
from apps.students.views import StudentViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"charities", CharityPostViewSet, basename="charity")
router.register(r"events", EventPostViewSet, basename="event")


contributor_urlpatterns = format_suffix_patterns(
    [
        path(
            "year/<int:year>/",
            include(
                [
                    path(
                        "",
                        contributors_by_year,
                        name="contributor-year-list",
                    ),
                    path(
                        "month/<int:month>",
                        contributors_by_year_and_month,
                        name="contributor-year-month-list",
                    ),
                ]
            ),
        ),
        path(
            "",
            create_contributor,
            name="contributor-create",
        ),
    ]
)

urlpatterns = [
    path("contributors/", include(contributor_urlpatterns)),
    path("", include(router.urls)),
]
