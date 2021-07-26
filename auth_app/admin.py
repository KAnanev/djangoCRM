from django.contrib import admin
from auth_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'id']
    list_filter = []
    readonly_fields = ['user_token', 'telegram_id']
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'groups', 'is_staff', 'is_active',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('user_token', 'telegram_id'),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()
        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return form
