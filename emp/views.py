from django.shortcuts import render, redirect
from emp.forms import *
from django.http import HttpResponse


# Create your views here.
def insertdata(request):
	if request.method=='POST':
		eform=EmployeeForm(request.POST)
		try:
			if eform.is_valid():
				eform.save()
				#return HttpResponse('Record Saved')
				return redirect('/show')
		except:
			pass 
	else:
		eform=EmployeeForm()
	return render(request, 'index.html',{'form':eform})

def show(request):
	data=Employee.objects.all()
	return render(request,'show.html',{'record':data})


def deleterecord(request,id):
	emp=Employee.objects.get(id=id)
	emp.delete()
	return redirect('/show')

def editrecord(request,id):
	emp=Employee.objects.get(id=id)
	return render(request,'edit.html',{'record':emp})
	

def updatedata(request,id):
	srecord=Employee.objects.get(id=id)
	form=EmployeeForm(request.POST,instance=srecord)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,'edit.html',{'record':srecord})