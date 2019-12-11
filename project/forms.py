from django import forms
from .models import Laptop, Student
class CreateStudentForm(forms.ModelForm):
    '''A form to add new quotes to teh database.'''

    class Meta:
        '''associate this form w Student model '''
        model = Student
        fields = ['name','student_id','email', 'phone','laptop'] #which fields from model 

class UpdateStudentForm(forms.ModelForm):
    '''A form to update a student to the database.'''

    class Meta: 
        '''associate this form with the Student model.'''
        model = Student
        fields = ['email','phone'] #which fields from model should we use

