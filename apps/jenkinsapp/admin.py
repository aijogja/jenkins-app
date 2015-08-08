from django.contrib import admin
from .models import Jobs, Member

# Register your models here.

class JobsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    readonly_fields = ('name', 'status')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, instance=None):
        return False

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Jobs, JobsAdmin)
admin.site.register(Member, MemberAdmin)
