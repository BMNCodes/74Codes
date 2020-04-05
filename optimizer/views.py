from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response

from __future__ import print_function
from gams import *
import os
import sys


def transport1():
    if __name__ == "__main__":
        if len(sys.argv) > 1:
            ws = GamsWorkspace(system_directory=sys.argv[1])
        else:
            ws = GamsWorkspace()

        ws.gamslib("trnsport")

        t1 = ws.add_job_from_file("trnsport.gms")
        t1.run()

        for rec in t1.out_db["x"]:
            return rec.key(0), rec.key(1), str(rec.level), str(rec.marginal)


def index(request):
    if request.method=="GET":
        py_obj=transport1()
        return render(request, 'index.html', {"output":py_obj})