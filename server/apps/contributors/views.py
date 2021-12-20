from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Contributor
from .serializers import ContributorSerializer


@api_view(["POST"])
def create_contributor(request, format=None):
    serializer = ContributorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def contributors_by_year(request, year, format=None):
    contributors = (
        Contributor.objects.filter(contribution_date__year=year)
        .order_by("name")
        .distinct("name")
        .all()
    )

    serializer = ContributorSerializer(contributors, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def contributors_by_year_and_month(request, year, month, format=None):
    contributors = (
        Contributor.objects.filter(
            contribution_date__year=year, contribution_date__month=month
        )
        .order_by("name")
        .distinct("name")
        .all()
    )

    serializer = ContributorSerializer(contributors, many=True)
    return Response(serializer.data)
