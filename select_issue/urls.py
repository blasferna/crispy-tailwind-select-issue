from django.urls import path

from demo.autocomplete import PersonAutocomplete
from demo.views import index


urlpatterns = [
    path("", index, name="index"),
    path(
        "person-autocomplete/", PersonAutocomplete.as_view(), name="person-autocomplete"
    ),
]
