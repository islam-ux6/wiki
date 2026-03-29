from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import markdown2
from random import choice

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
            "html": html,
            "title": title
            })
    else:
        return HttpResponse("File Not Found")
    
def search(request):
    q = request.POST["q"]
    entries = util.list_entries()

    if q in entries:
        return HttpResponseRedirect(reverse("show_ent", args=[q]))
    else:
        entries_sub = [entry for entry in entries if q.lower() in entry.lower()]

        return render(request, "encyclopedia/search.html", {
            "entries": entries_sub
        })

def create(request):
    if request.method == "POST":
        title = request.POST.get("label")
        content = request.POST.get("page_content")
        if title in util.list_entries():
            return HttpResponse("Entry already exist")
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("show_ent", args=[title]))
    else:
        return render(request, "encyclopedia/create.html")
    
def edit(request, name):
    content = util.get_entry(name)
    if request.method == "POST":
        edited_content = request.POST.get("edited_content")
        util.save_entry(name, edited_content)
        return HttpResponseRedirect(reverse("show_ent", args=[name]))
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": name,
            "content": content
        })
    
def random(request):
    entries = util.list_entries()
    random_entry = choice(entries)
    return HttpResponseRedirect(reverse("show_ent", args=[random_entry]))