
from django.shortcuts import render

# Create your views here.
from .models import Laptop , Student
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView ,UpdateView , DeleteView

from .forms import CreateStudentForm , UpdateStudentForm 
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllLaptopsView(ListView):
    '''create a subclass of listview to display all laptop'''

    model = Laptop #retrieve obejcts of type laptop from database 
    template_name = 'project/show_all_laptops.html'
    context_object_name = 'all_laptop_list'

class ShowLaptopPageView(DetailView):
    '''show the detail for one laptop'''
    model = Laptop
    template_name = 'project/show_laptop_page.html'
    context_object_name = 'laptop'

class ShowAllRentalPageView(ListView):
    model = Student 
    template_name = 'project/show_all_rental_page.html'
    context_object_name = 'all_rental_list'

class ShowStudentPageView(DetailView):
    '''show the detail for one student'''
    model = Student 
    template_name = 'project/show_student_page.html'
    context_object_name = 'student'

class HomePageView(ListView): 
    '''show the homepage'''
    model = Laptop 
    template_name = 'project/home.html'
    context_object_name = 'home_list'
    
class CreateStudentView(CreateView):
    '''A view to create a new quote and save it to tjhe database'''

    form_class = CreateStudentForm
    template_name = 'project/create_student_form.html'

class UpdateStudentView(UpdateView):
    '''A view to update a new quote and save it to tjhe database'''

    form_class = UpdateStudentForm
    template_name = 'project/update_student_form.html'
    queryset = Student.objects.all()

class DeleteStudentView(DeleteView):
    '''A view to update a new quote and save it to tjhe database'''

    template_name = 'project/delete_student.html'
    queryset = Student.objects.all()
    success_url = "../../rental"

