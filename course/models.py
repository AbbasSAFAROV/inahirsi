from django.db import models

class CourseBranch(models.Model):
    branch_name = models.CharField(max_length=100)
    def __str__(self):
        return self.branch_name

class Course(models.Model):
    course_name = models.CharField(max_length=220)
    course_branch = models.ForeignKey(CourseBranch,on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True)
    starting_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    due_date = models.DateTimeField(auto_now_add=False,auto_now=True)
    course_place = models.CharField(max_length=220)
    price = models.SmallIntegerField()
    max_apply = models.IntegerField(default=1)
    choice = (('passive','passive'),('active','active'),)
    status = models.CharField(choices=choice ,max_length=100,default="passive")
    def __str__(self):
        return self.course_name




class Student(models.Model):
    name = models.CharField(max_length=220)
    tel = models.CharField(max_length=220)
    email = models.EmailField()

    alinan_kurs = models.ForeignKey(Course,on_delete=True)
    created_date = models.DateTimeField(auto_now_add=False,auto_now=True)

    # choice = ((1,'accept'),(0,'declined'),(2,'waiting'))

    # status = models.SmallIntegerField(choices=choice)

    def __str__(self):
        return self.name

class Banner(models.Model):

    name = models.CharField(max_length=100)
    image = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return self.name



class Applicant(models.Model):
    name = models.CharField(max_length=220)
    phone_number = models.CharField(max_length=220)
    mail = models.EmailField()
    taken_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    applicant_date = models.DateTimeField(auto_now_add=False,auto_now=True)


    choice = (('accept','accept'),('declined','declined'),('waiting','waiting'))
    status = models.CharField(choices=choice , max_length=202 , default='waiting')

    def __str__(self):
        return self.name


