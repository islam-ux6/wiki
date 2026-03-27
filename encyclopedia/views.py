from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_ent(request, title):
    md_file = util.get_entry(title)
    if md_file:
        html = markdown2.markdown(md_file)
        return render(request, "encyclopedia/show_entry.html", {
            "html": html
            })
    else:
        return HttpResponse("File Not Found")
    
def search(request):
    q = request.POST["q"]

    return HttpResponseRedirect(reverse("show_ent", args=[q]))