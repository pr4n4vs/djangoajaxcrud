Djangoajax crud
---------------------------
1- create dir using django-admin startproject project_name
2- move to created dir 
3- python manage.py startapp app_name
4- register app in django setting i.e., project_name->settings.py->Installed apps
5- if you are using mysql database then change occur in setting.py->Database
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    	}
	}
6- Create one model like class Class_name(models.Model):
7- then, python manage.py makemigrations
8- python manage.py migrate
9- then, python manage.py createsuperuser
	this command used to access the admin pannel 
10- then you can check by running project by using following command,
	python manage.py runserver		//you can give diffrent port no. also like python manage.py runserver 4444
11- now the opening url shown in the cmd and you can access the admin portal by 127.0.0.1:8000/admin //which is default one you can change the admine access url
12- Created model has to registered on the admin portal so that following are used: 
	-> first of all you have toh include/import the model and models function by writting following line of code(LOC)
	from .models import * 
		OR
	from .models import model_name		//eg. model_name=User
	-> then here are two methods to register for admin 
		LOCs eg. are:
		@admin.register(User)
		class UserAdmin(admin.ModelAdmin):
		    list_display=('id','name','email','password')
					
					OR

		class UserAdmin(admin.ModelAdmin):
		    list_display=['id','name','email','password']
		admin.site.register(User,UserAdmin)
13- if you are using forms to get input then you have to create the forms.py in app and also include/import model as above 
	LOCs are:
	from django import forms
	from .models import User

	class StudentRegistration(forms.ModelForm):
	    class Meta:
	        model=User
	        field=['name','email','password']

meta:-Django automatically derives the name of the database table from the name of your model class and the app that contains it.

14- rendring this form we have to write the LOCs for view.py and before creating the view you must be prepare with the templates dir
	LOCs are:

	from django.shortcuts import render
	from .forms import *
	# Create your views here.

	def home(request):
	    data=StudentRegistration()
	    return render(request,'studentinfo/home.html',{'data':data})

15- after updating view.py we have to update the urls.py by adding the path for home so, we have to include first the view.py in urls.py then we create the path to connect like this path('',views.home,name="Homepage")

