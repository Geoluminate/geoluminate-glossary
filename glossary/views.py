from django.contrib.admindocs import utils, views
from django.db import models
from django.views.generic import TemplateView
from geoluminate.utils import get_database_models


class GlossaryView(TemplateView):
    template_name = "glossary/glossary.html"
    exclude_fields = ["site_ptr", "date_added", "historic_id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            models=self.get_model_info(),
            exclude=self.exclude_fields,
        )
        return context

    def get_model_info(self):
        model_info = []
        for model in get_database_models():
            opts = model._meta

            title, body, metadata = utils.parse_docstring(model.__doc__)

            # Gather fields/field descriptions.
            fields = []
            for field in opts.fields:
                if isinstance(field, models.ForeignKey):
                    data_type = field.remote_field.model.__name__
                else:
                    data_type = views.get_readable_field_data_type(field)
                choices = None
                if field.choices:
                    choices = [x[0] for x in field.get_choices()]
                if data_type == "Choice":
                    choices = field.get_choices_queryset()

                fields.append((field, data_type, choices or None))

            # Gather many-to-many fields.
            for field in opts.many_to_many:
                choices = None
                if field.choices:
                    choices = [x[0] for x in field.get_choices()]
                if data_type == "Choice":
                    choices = field.get_choices_queryset()
                fields.append((field, field.remote_field.model.__name__, choices or None))

            model_info.append(
                {
                    "name": opts.verbose_name,
                    "summary": title,
                    "description": body,
                    "fields": sorted(fields, key=lambda x: x[0].name),
                }
            )
        return model_info
