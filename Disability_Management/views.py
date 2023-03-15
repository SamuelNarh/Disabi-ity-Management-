from django.shortcuts import render,redirect
from .models import Disable
from datetime import datetime
from django.contrib import messages

# Create your views here.
def mainpage(request):
    if request.method=='POST':
        name = request.POST['name']
        image = request.FILES['image']
        gender= request.POST['gender']
        date_of_birth=request.POST['date_of_birth']
        age=request.POST['age']
        telephone=request.POST['telephone']
        nhis=request.POST['nhis']
        type_of_diasbilities=request.POST['type_of_diasbilities']
        rescidential=request.POST['rescidential']
        educational_level=request.POST['educational_level']
        school_vocation=request.POST['school_vocation']
        school=request.POST['school']
        guardian_name=request.POST['guardian_name']
        occupation_g=request.POST['occupation_g']
        type_of_support=request.POST['type_of_support']
        disability=request.POST['disability']
        date=datetime.now()
        date_format=date.strftime('%d-%m-%Y')
        disable=Disable(name=name,picture=image,birth_day=date_of_birth,date=date_format,gender=gender,age=age,
            telephone=telephone,nhis=nhis,type_of_diasbilities=type_of_diasbilities,rescidential=rescidential,
            educational_level=educational_level,school_vocation=school_vocation,school=school,
            guardian_name=guardian_name,occupation_g=occupation_g,type_of_support= type_of_support,
            disability=disability )       
        disable.save()
    return render(request,'mainindex.html')

def information(request):
    # print(request.GET)
    container=Disable.objects.all()       
    request.method == 'GET'
    search = request.GET.get("search") #Gets input typed by user
    if search!=None:
        #__icontains allows users to filter well
        container= container.filter(name__icontains=search)
    context={'container':container} 
    return render(request,'index.html',context)

def update(request,pk):
    container=Disable.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        image = request.POST['image']
        gender= request.POST['gender']
        date_of_birth=request.POST['date_of_birth']
        age=request.POST['age']
        telephone=request.POST['telephone']
        nhis=request.POST['nhis']
        type_of_diasbilities=request.POST['type_of_diasbilities']
        rescidential=request.POST['rescidential']
        educational_level=request.POST['educational_level']
        school_vocation=request.POST['school_vocation']
        school=request.POST['school']
        guardian_name=request.POST['guardian_name']
        occupation_g=request.POST['occupation_g']
        type_of_support=request.POST['type_of_support']
        disability=request.POST['disability']
        date=datetime.now()
        date_format=date.strftime('%d-%m-%Y')
        disable=Disable(id=pk,name=name,date=date_format,birth_day=date_of_birth,picture=image,gender=gender,age=age,
            telephone=telephone,nhis=nhis,type_of_diasbilities=type_of_diasbilities,
            rescidential=rescidential,educational_level=educational_level,school_vocation=school_vocation,
            school=school,guardian_name=guardian_name,occupation_g=occupation_g,type_of_support= type_of_support,
            disability=disability )
        disable.save()
        return redirect('info')
    context={'container':container}
    return render(request,'update.html',context)

def delete(request,pk):
    container=Disable.objects.get(id=pk)
    container.delete()
    messages.success(request,'Details deleted successful')
    return redirect('info')




