from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Personal_info, Education, Work_experience, Skills

def index(request):
    latest_question_list = Personal_info.objects.all()
    template = loader.get_template("cv/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, info_id):
    info = get_object_or_404(Personal_info, pk=info_id)
    edu = get_list_or_404(Education, personal_info=info_id)
    wrk = get_list_or_404(Work_experience, personal_info=info_id)
    skl = get_list_or_404(Skills, personal_info=info_id)
    return render(request, "cv/detail.html", {"info": info, "edu": edu, "wrk": wrk, "skl": skl})