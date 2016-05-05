class SetTeamOnCreate(object):
    def perform_create(self, serializer):
        return serializer.save(team=self.request.team)
