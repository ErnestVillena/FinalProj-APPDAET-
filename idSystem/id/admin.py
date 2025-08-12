from django.contrib import admin

# Register your models here.

from . models import IdType, IdCredentials

@admin.register(IdType)
class IdTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('idType_category',)}
    list_display = ('idType_category', 'idType_number', 'idType_kind', 'owner', 'idType_expdate', 'idType_isexp')
    list_filter = ('idType_kind', 'idType_isexp')
    search_fields = ('idType_category', 'idType_number', 'owner__idCred_name')


@admin.register(IdCredentials)
class IdCredentialsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('idCred_name',)}
    list_display = ('idCred_name', 'idCred_addr', 'idCred_dob')
    search_fields = ('idCred_name', 'idCred_addr')

