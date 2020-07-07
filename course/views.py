from .models import Course, Banner,Applicant, CourseBranch 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):

    course = Course.objects.all()
    banner = Banner.objects.all()
    branch = CourseBranch.objects.all()


    context = {"course":course,"banner":banner,"branch":branch}

    return render(request,"home.html",context)

def home(request):
    course = Course.objects.all()
    banner = Banner.objects.all()
    branch = CourseBranch.objects.all()

    context = {"course":course,"banner":banner,"branch":branch}
    return render(request,"home.html",context)

def apply(request, id):

    course = Course.objects.get(id= id)
    instance = Applicant.objects.all()
    context = {
        "course":course
    }

    if request.method =="POST":

        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        mail = request.POST.get("mail")
        # taken_course=newApplicant.taken_course(course.course_name)

        instance = Applicant(name= name , phone_number=phone_number,mail=mail ,taken_course=Course.objects.get(id=id))

        

        if course.max_apply >1:
            instance.save()
            course.max_apply -=1
            course.save()
            return redirect("home")
        
        elif course.max_apply <=1:
            course.status = "passive"
            course.max_apply -=1
            instance.save()
            course.save()

        # newApplicant.save()

        return redirect("home")


    return render(request,"apply.html",context)
    

@login_required(login_url = "loginUser")
def admin(request):
    cour = Applicant.objects.all()
    course = Course.objects.all()
    branch = CourseBranch.objects.all()


    context = {"course":course,"cour":cour,"branch":branch}
    return render(request,"admin.html",context)

@login_required(login_url = "loginUser")
def addBanner(request):

    if request.method == "POST":
        bannerName = request.POST.get("bannerName")
        imageFile = request.POST.get("imageFile")
        
        newBanner = Banner(name = bannerName , image = imageFile)
        
        newBanner.save()
        
        messages.success(request, "banner başarıyla eklendi . . .")
        return redirect("home")

    else:
        messages.success(request, "banner eklenemedi . . .")
        return render(request, "addBanner.html")

@login_required(login_url="loginUser")
def addCourse(request , id):

    branch = CourseBranch.objects.all()
    branch1 = CourseBranch.objects.get(id=id)
    # course = Course.objects.all()
    # context = {"branch":branch,"course":course}

    if request.method=="POST":
        course_name = request.POST.get("course_name")
        course_place = request.POST.get("course_place")
        price = request.POST.get("price")
        max_apply = request.POST.get("max_apply")
        course_branch = request.POST.get("values")
        image = request.POST.get("image")
        
        course = Course(course_name=course_name,course_place=course_place,price=price,image=image,max_apply=max_apply,course_branch=CourseBranch.objects.get(id=id))
    
        course.save()
        return redirect("home")

    return render(request,"addCourse.html",{"branch1":branch1})


@login_required(login_url="loginUser")
def deleteCourse(request, id):
    # course1 = get_object_or_404(Course,id=id)
    course1 = Course.objects.filter(id=id).first()
    course1.delete()
    return redirect("dashboard")
@login_required(login_url = "loginUser")
def deleteCourseBranch(request, id):
    # branchDelete = get_object_or_404(CourseBranch,id=id)
    branchDelete = CourseBranch.objects.get(id=id)
    branchDelete.delete()
    return redirect("dashboard")
@login_required(login_url = "loginUser")
def deleteApplicant(request, id):
    # course1 = get_object_or_404(Course,id=id)
    applicant1 = Applicant.objects.filter(id=id).first()
    applicant1.delete()
    return redirect("dashboard")

def signin(request):

    if request.method == "POST":
        loginusername = request.POST.get("loginusername")
        loginpassword = request.POST.get("loginpassword")

        user = authenticate(username=loginusername, password=loginpassword)

        if user is None:
            messages.warning(request, "kullanici veya parola hatali")

        else:
            messages.success(request, "başarıyla giriş yaptınız")
            login(request, user)
            return redirect("index")

    return render(request, "signin.html")


def loginRegister(request):

    if request.method == "POST":
        loginusername = request.POST.get("loginusername")
        loginpassword = request.POST.get("loginpassword")

        user = authenticate(username = loginusername , password = loginpassword)

        if user is None:
            messages.warning(request,"kullanici veya parola hatali")

        else:
            messages.success(request,"başarıyla giriş yaptınız")
            login(request,user)
            return redirect("home")

    return render(request,"login-register.html")

def logoutUser(request):
    logout(request)
    messages.success(request,"başarıyla çıkış yaptınız.")

    return redirect("home")


def AddCourseBranch(request):

    branch = CourseBranch.objects.all()
    context = {"branch":branch}
    
    if request.method=="POST":
        branch_name = request.POST.get("branch_name")
        # taken_course=newApplicant.taken_course(course.course_name)

        branch_save = CourseBranch(branch_name=branch_name)

        branch_save.save()

        # newApplicant.save()

        return redirect("home")
        
    return render(request,"addCourseBranch.html")

def ActivateCourse(request,id):

    course = Course.objects.all()
    banner = Banner.objects.all()
    branch = CourseBranch.objects.all()
    context = {"course":course,"banner":banner,"branch":branch}

    activateCourse = Course.objects.get(id=id)

    activateCourse.status = "active"

    activateCourse.save()

    return redirect("dashboard")


def AcceptApplicant(request,id):

    courseApp = Applicant.objects.get(id=id)

    newCourseId = courseApp.taken_course.id

    newCourse = Course.objects.get(id=newCourseId)

    courseApp.status = "accept"
    # newCourse.max_apply -=1

    # newCourse.save()
    courseApp.save()
    # newCourseMaxApply = Course()

    courseApp.save()
    return redirect("dashboard")

def PassiveCourse(request,id):
    passiveCourse = Course.objects.get(id=id)

    passiveCourse.status = "passive"
    passiveCourse.save()

    return redirect("dashboard")

def RemoveFromCourse(request,id):

    applicantRemove = Applicant.objects.get(id=id)

    newCourseRemoveAppId = applicantRemove.taken_course.id

    newCourseRemove = Course.objects.get(id=newCourseRemoveAppId)

    newCourseRemove.max_apply +=1
    newCourseRemove.save()
    applicantRemove.delete()
    return redirect("dashboard")

def MaxLimit(request):

    courses = Course.objects.all()

    for item in courses:
        if item.max_apply<=0:
            item.status = "passive"
            item.save()
            return redirect("dashboard")
        else:
            item.status = "active"


