from django.shortcuts import render

from first_app.forms import student_form
from first_app.models import student

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
	form=student_form()
	if request.method=="POST":
		form=student_form(request.POST)
		if form.is_valid():
			form.save()
			# return redirect('index')
			# return redirect('/')
	return render(request,'registration.html',{'form':form})

def login(request):
	return render(request,'login.html')

def dashboard(request):
	return render(request,'dashboard.html')


def about(request):
	example=student.objects.order_by('name')
	my_dict={'student':example}
	return render(request,'about.html',context=my_dict)