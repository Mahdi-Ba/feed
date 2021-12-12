"""Integrate with admin module."""
#
# from django.contrib import admin, messages
# from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# from django.utils.translation import gettext_lazy as _
#
# from .models import User
#
#
# @admin.register(User)
# class UserAdmin(DjangoUserAdmin):
#     """Define admin model for custom User model with no mobile field."""
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': (
#             'first_name', 'last_name', 'email')}),
#         (
#             _('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                                                    'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('mobile', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('username','first_name', 'last_name', 'email', 'is_staff', 'date_joined')
#     search_fields = ('first_name', 'last_name', 'email')
