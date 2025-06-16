
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.department_list, name='all-departments'),
    path('add-department/', views.add_department, name="adddepartment"),
    path('update-department/<str:id>', views.update_department, name="update"),
    path('delete/<str:id>', views.delete_deaprtment, name="delete")

]