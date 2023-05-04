from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from simple_menu import Menu, MenuItem

Menu.add_item(
    "toolbar",
    MenuItem(
        _("Glossary"),
        reverse("glossary"),
        weight=4,
        icon="fa-th-list",
    ),
)
