from django.contrib import admin

from shared.models import Staff, Contact


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'profession']
    search_fields = ['full_name', 'profession', 'info']
    list_filter = ['created_at', 'updated_at']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'subject', 'message']
    search_fields = ['full_name', 'email', 'subject']
    list_filter = ['created_at', 'updated_at', 'is_read']

