from rest_framework import filters


class TeamFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(team=request.team)
