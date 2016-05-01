from rest_framework import filters


class TenantFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(tenant=request.tenant)
