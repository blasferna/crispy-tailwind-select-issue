from django.shortcuts import render
from demo.forms import SelectForm


def index(request):
    form = SelectForm(request.POST or None)
    return render(request, "demo/index.html", {"form": form})
