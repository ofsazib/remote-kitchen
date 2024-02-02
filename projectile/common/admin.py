from django.contrib import admin
from reversion.admin import VersionAdmin

admin.site.site_header = "Remote Kitchen Admin"
admin.site.index_title = "Remote Kitchen Administration Portal"

class BaseModelAdmin(VersionAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [
            field.attname for field in model._meta.fields]
        # select fields those are foreign key
        self.raw_id_fields = [
            field.name for field in model._meta.fields if field.is_relation]
        super(BaseModelAdmin, self).__init__(model, admin_site)

    list_filter = ('status',)
    show_full_result_count = True
