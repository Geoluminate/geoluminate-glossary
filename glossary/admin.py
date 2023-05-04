from django.contrib import admin

from .models import ModelMeta


@admin.register(ModelMeta)
class ModelMetaAdmin(admin.ModelAdmin):
    pass
