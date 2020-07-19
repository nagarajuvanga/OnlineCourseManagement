from pyexpat.errors import messages

from django.shortcuts import render, redirect

# Create your views here.
from app.models import Schedule_class, Student,Entrol
from django.http import HttpResponseRedirect


def showIndex(request):
    return render(request,"index.html")


def admin_page(request):
    return render(request,"admin_login.html")


def save_adminlogin(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    if un == "nagaraju" and pa == "nagaraju":
        return render(request, "admin_welcome.html")
    else:
        return render(request, "admin_login.html",{"error_messages":"Invalid User"})


def schedule_class(request):
    return render(request,"schedule_class.html")


def save_schedule(request):
    na=request.POST.get("s1")
    fa=request.POST.get("s2")
    da=request.POST.get("s3")
    tim=request.POST.get("s4")
    fee=request.POST.get("s5")
    dur=request.POST.get("s6")
    Schedule_class(name=na,faculty=fa,date=da,time=tim,fee=fee,duration=dur).save()
    return redirect("schedule_class")


def view_all(request):
    res=Schedule_class.objects.all()
    return render(request,"viewall_classes.html",{"data":res})


def home_page(request):
    return render(request,"admin_welcome.html")


def show_update(request):
    na=request.POST.get("t1")
    res=Schedule_class.objects.get(name=na)
    return render(request,"update.html",{"data":res})


def update_record(request):
    na = request.POST.get("u1")
    fa = request.POST.get("u2")
    da = request.POST.get("u3")
    tim = request.POST.get("u4")
    fee = request.POST.get("u5")
    dur = request.POST.get("u6")
    Schedule_class.objects.filter(name=na).update(faculty=fa,date=da,time=tim,fee=fee,duration=dur)
    return redirect("view_all")


def student_login(request):
    return render(request,"student_login.html")


def delete(request):
    na=request.GET.get("name")
    Schedule_class.objects.filter(name=na).delete()
    return redirect("view_all")

def save_studentdata(request):
    na=request.POST.get("p1")
    con=request.POST.get("p2")
    em=request.POST.get("p3")
    pas=request.POST.get("p4")
    Student(sname=na,contactno=con,email=em,password=pas).save()
    return redirect("student_login")


def login(request):
    return render(request,"student_welcome.html")


def login_s(request):
    em=request.POST.get("t1")
    pa=request.POST.get("t2")
    try:

        da = Schedule_class.objects.all()
        res = Student.objects.get(email=em,password=pa)


        return render(request, "home_page.html",{"naga":res,"result":da})



    except Student.DoesNotExist:
        return render(request, "student_welcome.html",{"error_message": "Invalid User"})

def student_home(request):
    res = Schedule_class.objects.all()

    return render(request,"student_home.html",{"data":res})


def entrol(request):
    co = request.GET.get("s1")
    cno = request.GET.get("s2")
    Entrol(course=co, contact=cno).save()

    da = Schedule_class.objects.all()
    res = Student.objects.get(contactno=cno)
    return render(request, "home_page.html", {"naga": res, "result": da})


def view_entrol(request):


    no = request.GET.get("u1")
    a = Entrol.objects.filter(contact=no).values()


    n = Student.objects.all()
    y=[]
    for x in a:
        s = x["course"]
        z=Schedule_class.objects.filter(coid=s)
        y.append(z)

    return render(request,"dummy.html",{"raj":y,"naga":n,"en":no})


def cancel(request):
    ci = request.GET.get("c2")
    cn = request.GET.get("c1")

    Entrol.objects.filter(course=ci,contact=cn).delete()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))