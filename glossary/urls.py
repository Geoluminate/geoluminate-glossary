from django.urls import path

from .views import GlossaryView

urlpatterns = [
    path("glossary/", GlossaryView.as_view(), name="glossary"),
]
