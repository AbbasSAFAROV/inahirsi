from django.contrib import admin
from django.urls import path,include
from . import views

# from django.contrib import admin
# from django.urls import path , include
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="home"),
    path('home/', views.home),
    path('apply/<int:id>', views.apply),
    path('dashboard/', views.admin,name="dashboard"),
    path('login/', views.loginRegister,name="loginRegister"),
    path('logout/', views.logoutUser),
    path('addBanner/', views.addBanner),
    path('addCourse/<int:id>', views.addCourse),
    path('AddCourseBranch/', views.AddCourseBranch),
    path('deleteCourse/<int:id>', views.deleteCourse),
    path('deleteCourseBranch/<int:id>', views.deleteCourseBranch),
    path('deleteApplicant/<int:id>', views.deleteApplicant),
    path('AcceptApplicant/<int:id>', views.AcceptApplicant),
    path('ActivateCourse/<int:id>', views.ActivateCourse),
    path('PassiveCourse/<int:id>', views.PassiveCourse),
    path('RemoveFromCourse/<int:id>', views.RemoveFromCourse),
    
    
    
    
    
    
]
