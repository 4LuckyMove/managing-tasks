from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'date_joined', 'last_login', )
    list_display_links = ('email', )
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',
                           'username', 'first_name', 'last_name', 'date_joined', 'last_login',
                           )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )
    search_fields = ('email', )
    ordering = ('email', )
