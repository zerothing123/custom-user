from django.contrib import admin
from.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm,UserAdminChangeForm

class UserAdmin(BaseUserAdmin):

    form=UserAdminChangeForm
    add_form=UserAdminChangeForm

    list_display = ('email', 'admin')
    list_filter = ('admin','staff','active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email','fullname')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
