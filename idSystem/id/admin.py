from django.contrib import admin

# Register your models here.

from . models import IdType, IdCredentials

@admin.register(IdType)
class IdTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('idType_category',)}

@admin.register(IdCredentials)
class IdCredentialsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('idCred_name',)}