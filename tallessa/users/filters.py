from rest_framework import filters


class UserTeamFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(group_set=request.team.user_group)
