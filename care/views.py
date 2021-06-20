from django.http import HttpResponse
from django.shortcuts import render, redirect
from care.models import Upload,DonorProfile,CreateUserForm
from django.contrib import messages
import pandas as pd
import numpy as np
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        comment = request.POST.get('comment')
        data = {
            'name':name,
            'email':email,
            'mobile':mobile,
            'comment':comment,
        }

        message = '''
        NEW MESSAGE :{}
        FROM: {}
        '''.format(data['comment'], data['email'])
        send_mail(data['email'],message,email,['vcareforyou21@gmail.com'])
    return render(request,'index.html')


def receiverdetails(request):
    receiver = Upload.objects.all()
    return render(request,'receiverdetails.html',{'receiver':receiver})

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required
def donorprofile(request):
    if request.method == 'POST':
        b = request.user
        try:
            a = DonorProfile.objects.get(id = b.id)
            a.name=request.POST.get('name')
            a.email=request.POST.get('email')
            a.phone=request.POST.get('phone1')
            a.whatsappphone=request.POST.get('phone2')
            a.street=request.POST.get('street')
            a.city=request.POST.get('city')
            a.state=request.POST.get('state')
            a.zip=request.POST.get('zip')
            a.idi=request.POST.get('idi')
            a.save()
            messages.success(request,'Profile Updated Successfully')
            return render(request,'donorprofile.html',{'a':a})
        except DonorProfile.DoesNotExist:
            saverecord=DonorProfile()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone1')
            saverecord.whatsappphone=request.POST.get('phone2')
            saverecord.street=request.POST.get('street')
            saverecord.city=request.POST.get('city')
            saverecord.state=request.POST.get('state')
            saverecord.zip=request.POST.get('zip')
            saverecord.idi=request.POST.get('idi')
            messages.success(request,'Profile Recorded Successfully')
            saverecord.save()
            b = request.user
            try:
                a = DonorProfile.objects.get(id = b.id)
            except DonorProfile.DoesNotExist:
                a=None
            return render(request,'donorprofile.html',{'a':a})
    else:
        b = request.user
        try:
            a = DonorProfile.objects.get(id = b.id)
        except DonorProfile.DoesNotExist:
            a=None
        return render(request,'donorprofile.html',{'a':a})


def govschemes(request):
    return render(request,'govschemes.html')

def ngos(request):
    return render(request,'ngos.html')


def upload(request):
    dataset = pd.read_csv('project.csv')
    pred = []
    pred.append(request.POST.get('age'))
    pred.append(request.POST.get('gender'))
    pred.append(request.POST.get('workclass'))
    pred.append(request.POST.get('education'))
    pred.append(request.POST.get('maritalstatus'))
    pred.append(request.POST.get('hoursofwork'))
    pred.append(request.POST.get('income'))
    X = dataset.iloc[:,:7]
    Y = dataset.iloc[:,7]
    Ylist = list(Y)
    length = len(Ylist)
    Noyes = Ylist.count("Yes")
    NoNo = Ylist.count("No")
    probyes = Noyes/length
    probno = NoNo/length
    def counting(x,Ylist,length,value,ped):
        ycount = 0
        for i in range(len(x)):
            if x[i] == ped and Ylist[i] == value:
                ycount = ycount + 1
        return ycount
    age_group = list(X['Age_Group'])
    ageyes = counting(age_group,Ylist,length,"Yes",pred[0])
    ageNo = counting(age_group,Ylist,length,"No",pred[0])
    probageY = ageyes/Noyes
    probageN = ageNo/NoNo
    gender = list(X['Gender'])
    genderyes = counting(gender,Ylist,length,"Yes",pred[1])
    genderno = counting(gender,Ylist,length,"No",pred[1])
    probgenderY = genderyes/Noyes
    probgenderN = genderno/NoNo
    workclass = list(X['Workclass'])
    workclassyes = counting(workclass,Ylist,length,"Yes",pred[2])
    workclassno = counting(workclass,Ylist,length,"No",pred[2])
    probworkclassY = workclassyes/Noyes
    probworkclassN = workclassno/NoNo
    educationlevel = list(X['Education_Level'])
    educationlevelyes = counting(educationlevel,Ylist,length,"Yes",pred[3])
    educationlevelno = counting(educationlevel,Ylist,length,"No",pred[3])
    probeducationlevelY = educationlevelyes/Noyes
    probeducationlevelN = educationlevelno/NoNo
    maritalstatus = list(X['marital_status'])
    maritalstatusyes = counting(maritalstatus,Ylist,length,"Yes",pred[4])
    maritalstatusno = counting(maritalstatus,Ylist,length,"No",pred[4])
    probmaritalstatusY = maritalstatusyes/Noyes
    probmaritalstatusN = maritalstatusno/NoNo
    hoursofwork = list(X['Average_hours_per_week_worked'])
    hoursofworkyes = counting(hoursofwork,Ylist,length,"Yes",pred[5])
    hoursofworkno = counting(hoursofwork,Ylist,length,"No",pred[5])
    probhoursofworkY = hoursofworkyes/Noyes
    probhoursofworkN = hoursofworkno/NoNo
    income = list(X['Income'])
    incomeyes = counting(income,Ylist,length,"Yes",pred[6])
    incomeno = counting(income,Ylist,length,"No",pred[6])
    probincomeY = incomeyes/Noyes
    probincomeN = incomeno/NoNo
    productyes = probageY * probgenderY * probworkclassY * probeducationlevelY * probmaritalstatusY * probhoursofworkY * probincomeY * probyes

    productNo = probageN * probgenderN * probworkclassN * probeducationlevelN * probmaritalstatusN * probhoursofworkN * probincomeN * probno
    if request.method == 'POST':
        if productyes>productNo:
            saverecord=Upload()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone1')
            saverecord.whatsappphone=request.POST.get('phone2')
            saverecord.street=request.POST.get('street')
            saverecord.city=request.POST.get('city')
            saverecord.state=request.POST.get('state')
            saverecord.zip=request.POST.get('zip')
            saverecord.age=request.POST.get('age')
            saverecord.gender=request.POST.get('gender')
            saverecord.workclass=request.POST.get('workclass')
            saverecord.education=request.POST.get('education')
            saverecord.maritalstatus=request.POST.get('maritalstatus')
            saverecord.hoursofwork=request.POST.get('hoursofwork')
            saverecord.income=request.POST.get('income')
            saverecord.tdr=request.POST.get('tdr')
            saverecord.filepath = request.POST.get('incomefile')
            saverecord.save()
            messages.success(request,'You are eligible to receive the donations, interested donor will contact you soon')
            return render(request,'upload.html')
        else:
            messages.error(request,'You are not eligible to receive the donations')
            return render(request,'upload.html')
    else:
        return render(request,'upload.html')

def howitworks(request):
    return render(request,'howitworks.html')

def howitworksdonor(request):
    return render(request,'howitworksdonor.html')

def registerdonor(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CreateUserForm()
    return render(request,'registerdonor.html',{'form':form})

def admlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username1')
        password=request.POST.get('password4')
        if (username=="careadmin" and password=="vcare4u21"):
            return render(request,'admindashboard.html')
        else:
            messages.error(request,'Please enter correct username and password')
            return render(request,'adminlogin.html')
    else:
        return render(request,'adminlogin.html')

def admindonor(request):
    donor = DonorProfile.objects.all()
    return render(request,'admindashboard.html',{'donor':donor})

def adminreceiver(request):
    receiver = Upload.objects.all()
    return render(request,'adminreceivers.html',{'receiver':receiver})

def dashboard(request):
    totalreceivers = Upload.objects.all().count()
    totaldonors = DonorProfile.objects.all().count()
    d = {'totaldonors':totaldonors,'totalreceivers':totalreceivers}
    return render(request,'dashboard.html',d)

@login_required
def donordashboard(request):
    totalreceivers = Upload.objects.all().count()
    totaldonors = DonorProfile.objects.all().count()
    d = {'totaldonors':totaldonors,'totalreceivers':totalreceivers}
    return render(request,'donordashboard.html',d)
