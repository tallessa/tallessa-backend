class SetTenantOnCreate(object):
    def perform_create(self, serializer):
        return serializer.save(tenant=self.request.tenant)
