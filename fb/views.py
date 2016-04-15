from django.shortcuts import render
#from fdb import
from .fdb import fedit, fdelete, fview


def form(request):
    return render(request, 'fb/home.html')

def firecreate(request):
	sname = request.POST["sname"]
	semail = request.POST["semail"]
	sschool = request.POST["sschool"]
	sgrade = request.POST["sgrade"]
	text = fedit(sname,semail,sschool,sgrade)
	response = {'text':text}
	return render(request, 'fb/output.html', context = response)

def firedelete(request):
	sname = request.POST["sname"]
	semail = request.POST["semail"]
	text = fdelete(sname,semail)
	response = {'text':text}
	return render(request, 'fb/output.html', context = response)

def fireview(request):
	sname = request.POST["sname"]
	semail = request.POST["semail"]
	text = fview(sname,semail)
	response = {'text':text}
	return render(request, 'fb/output.html', context = response)