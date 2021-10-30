from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from .models import *

# Create your views here.

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')

    return render(request, 'index.html')

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)

        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST.get('gender')
        

        try:
            Enquiry.objects.create(name = n, contact = c, emailid = e, age = a, gender = g)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_enquiry.html', d)

def View_Enquiry(request):
    if not request.user.is_staff:
        return redirect('login')
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'view_enquiry.html', d)

def Delete_Enquiry(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    enquiry = Enquiry.objects.get(id = pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        de = request.POST.get('description')

        try:
            Equipment.objects.create(name = n, price = p, unit = u, date = d, description = de)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_equipment.html', d)

def View_Equipment(request):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.all()
    d = {'equipment': equipment}
    return render(request, 'view_equipment.html', d)

def Delete_Equipment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.get(id = pid)
    equipment.delete()
    return redirect('view_equipment')

def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']

        try:
            Plan.objects.create(name = n, amount = a, duration = d)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)

def View_Plan(request):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.all()
    d = {'plan': plan}
    return render(request, 'view_plan.html', d)

def Delete_Plan(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.get(id = pid)
    plan.delete()
    return redirect('view_plan')

def Add_Member(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        jd = request.POST['joindate']
        ed = request.POST['expiredate']
        i = request.POST['initialamount']

        try:
            Member.objects.create(name = n, contact = c, emailid = e, age = a, gender = g, plan = p, joindate = jd, expiredate = ed, initialamount = i)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_member.html', d)

def View_Member(request):
    if not request.user.is_staff:
        return redirect('login')
    member = Member.objects.all()
    d = {'member': member}
    return render(request, 'view_member.html', d)

def Delete_Member(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    member = Member.objects.get(id = pid)
    member.delete()
    return redirect('view_member')
