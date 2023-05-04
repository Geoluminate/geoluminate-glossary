# mypy: ignore-errors
# an open issue with django-model-utils (https://github.com/jazzband/django-model-utils/issues/558) raises errors due to missing type annotations. Disabling errors for entire file until it's fixed.
from django.contrib.contenttypes.fields import GenericForeignKey

# from djangocms_text_ckeditor.fields import HTMLField
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext as _
from geoluminate.utils import geoluminate_content_types


class ModelMeta(models.Model):
    content_type = models.OneToOneField(
        ContentType, limit_choices_to=geoluminate_content_types, on_delete=models.CASCADE
    )

    description = models.TextField()

    class Meta:
        verbose_name = _("Model Meta")
        verbose_name_plural = _("Model Meta")
