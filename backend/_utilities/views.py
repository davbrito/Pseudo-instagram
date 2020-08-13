from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


def list_queryset(view: GenericAPIView, queryset):
    queryset = view.filter_queryset(queryset)
    page = view.paginate_queryset(queryset)
    if page is not None:
        serializer = view.get_serializer(page, many=True)
        return view.get_paginated_response(serializer.data)
    serializer = view.get_serializer(queryset, many=True)
    return Response(serializer.data)
