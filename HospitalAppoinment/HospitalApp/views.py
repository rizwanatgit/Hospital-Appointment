from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def indexpage(request):
    return render(request, "index.html")


def loginpage(request):
    return render(request, "logIN.html")


def signuppage(request):
    return render(request, "signup.html")


def homepage(request):
    return render(request, "home.html")


def signUP(request):
    if request.method == "POST":
        n = request.POST['name']
        ph = request.POST['phone']
        uid = request.POST['userid']
        pword = request.POST['password']
        sex = request.POST['gender']
        data1 = signup_db.objects.filter(phno=ph)
        if data1:
            messages.info(request, 'phone number already exists!')
            return redirect(signuppage)
        data = signup_db.objects.create(name=n, phno=ph, username=uid, password=pword, gender=sex)
        data.save()
        return redirect(loginpage)


def AppoinmentAction(request):
    if request.method == 'POST':
        n = request.POST['num']
        pswd = request.POST['pass']
        data = signup_db.objects.filter(phno=n)
        if data:
            data1 = signup_db.objects.get(phno=n)
            if data1.password == pswd:
                request.session['id'] = n
                return redirect(homepage)

            else:
                messages.info(request, 'Invalid email or password')
                return redirect(loginpage)
        else:
            messages.info(request, 'Invalid email or password')
            return redirect(loginpage)


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(homepage)


def adminlog(request):
    return render(request, "adminlogin.html")


def appoinment(request):
    if request.method == "POST":
        n = request.POST['name']
        mail = request.POST['email']
        dob = request.POST['date']
        opt = request.POST['option']
        sex = request.POST['gender']
        ph = request.POST['phone']
        msg = request.POST['message']
        pid = request.POST['paymentid']
        data = appoinments.objects.create(name=n, email=mail, date=dob, department=opt, gender=sex, phone_number=ph,
                                          payment=pid)
        data.save()
        messages.info(request, 'data stored')
        return redirect(homepage)


def booking_details(request):
    pending_bookings = []
    history = []
    d = appoinments.objects.filter(booking_status='pending')
    for i in d:
        if i.phone_number == request.session['id']:
            pending_bookings.append(i)
    d1 = appoinments.objects.filter(booking_status='approve')
    for j in d1:
        if j.phone_number == request.session['id']:
            history.append(j)
    return render(request, 'bookings.html', {'data': pending_bookings, 'data1': history})


def adminhome(request):
    d = signup_db.objects.all()
    return render(request, "adminhome.html", {'data': d})


def adminLog(request):
    if request.method == 'POST':
        adminid = request.POST['name']
        adminpswd = request.POST['password']
        data = admin_log.objects.filter(admin_name=adminid)
        if data:
            data1 = admin_log.objects.get(admin_name=adminid)
            if data1.admin_pass == adminpswd:
                request.session['adminid'] = adminid
                return redirect(adminhome)

            else:
                messages.info(request, 'Invalid email or password@')
                return redirect(adminlog)
        else:
            messages.info(request, 'Invalid email or password')
            return redirect(adminlog)


def pending_app(request):
    d = appoinments.objects.filter(booking_status='pending')
    return render(request, "appoinments.html", {'data': d})

def accept_app(request,id):
    appoinments.objects.filter(pk=id).update(booking_status='approve')
    messages.info(request,'Approved')
    return redirect(pending_app)

def doctors_pg(request):
    return render(request, "doctors.html")

def AddDoctor(request):
    if request.method == "POST":
        n = request.POST['docname']
        did = request.POST['docid']
        pic = request.FILES['photo']
        dep = request.POST['department']
        data = doctors.objects.create(name=n, doctor_id=did, uploadphoto= pic, department=dep)
        data.save()
        messages.info(request, 'data stored')
        return redirect(doctors_pg)

def doctortable(request):
    d= doctors.objects.all()
    return render(request,"RegisterDocs.html",{'data':d})

def docdelete(request,id):
    doctors.objects.filter(pk=id).delete()
    messages.info(request,'doctor deleted')
    return redirect(doctortable)
