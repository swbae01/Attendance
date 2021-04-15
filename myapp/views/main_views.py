from django.shortcuts import render, get_object_or_404
from ..models import Lecture
import os
from django.conf import settings
import csv

def main(request):
    patha = getattr(settings, "BASE_DIR", None)
    newpath = os.path.join(patha, "static/etc/data.csv")
    with open(newpath, encoding="utf-8") as csvfile:
        rr= csv.reader(csvfile, delimiter=',')
        for row in rr:
            print(row)

    print(newpath)

    context = {}
    return render(request, 'myapp/index.html', context)

def lecture_load(request):
    json_path = os.path.abspath(__file__)
    lecture_list = Lecture.objects.all()
    context = {'lecture_list': lecture_list}
    return render(request, 'myapp/lecture/lecture_list.html', context)