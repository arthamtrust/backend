from rest_framework import viewsets

from .models import Contributor
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):

        queryset = Contributor.objects.all()

        year = self.request.query_params.get("year")
        month = self.request.query_params.get("month")

        if year is None and month is None:
            return queryset

        if year is not None:
            queryset = queryset.filter(contribution_date__year=year)

        if month is not None:
            queryset = queryset.filter(contribution_date__month=month)

        return queryset.order_by("name").distinct("name")
