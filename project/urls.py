
# project/urls.py

from django.urls import path 
from .views import ShowAllLaptopsView , DeleteStudentView, ShowLaptopPageView , ShowStudentPageView, UpdateStudentView, HomePageView,  CreateStudentView , ShowAllRentalPageView #our view class definition

#urls for every pages 
urlpatterns = [
    path('laptop',ShowAllLaptopsView.as_view(), name='show_all_laptops'), 
    path('laptop/<int:pk>',ShowLaptopPageView.as_view(), name='show_laptop_page' ),
    path('student/<int:pk>',ShowStudentPageView.as_view(), name = 'show_student_page'),
    path('rental',ShowAllRentalPageView.as_view(), name = 'rental_page'),
    path('',HomePageView.as_view(), name = 'home'),#generic home 
    path('student/<int:pk>/delete',DeleteStudentView.as_view(),name = "delete_student"),
    path('student/<int:pk>/update',UpdateStudentView.as_view(), name = 'update_student'),
    path('create_student',CreateStudentView.as_view(),name='create_student'),
] 