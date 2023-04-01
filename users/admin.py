from django.contrib import admin
from .models import SchoolUser


# Register your models here.
@admin.register(SchoolUser)
class SchoolUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'user_type', 'user_icon')
    actions = ('ban_users', 'unlock_users')
    list_filter = ('first_name', 'last_name')
    search_fields = ('username',)
    ordering = ('username',)

    fieldsets = [
        ('User entry', {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('local_address', 'permanent_address')
        }),
        ('School info', {
            'fields': ('standard', 'subject')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
    ]

    # USER BANNING FUNCTION
    def ban_users(self, request, queryset):
        queryset.update(is_active=False)

    def unlock_users(self, request, queryset):
        queryset.update(is_active=True)
