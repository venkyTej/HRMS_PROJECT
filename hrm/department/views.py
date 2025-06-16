

# Create your views here.
from django.shortcuts import render, redirect
from .models import Department

# Create your views here.

def department_list(request):
    department = Department.objects.all()
    return render(request, "department.html", {"all_departments":department})

def add_department(request):
    if request.method == "POST":
        dept_name = request.POST.get('dept_name')
        description = request.POST.get('description')

        department = Department(
            dept_name=dept_name,
            description=description,
        
        )
        department.save()
        return redirect("all-departments")  # make sure this matches your URL name

    return render(request, "department.html")

def update_department(request, id):
    if request.method == "POST":
         dept_id = request.POST.get('dept_id')
         dept_name = request.POST.get('dept_name')
         description = request.POST.get('description')
         created = request.POST.get('created')
         updated = request.POST.get('updated')

         department = Department(
            dept_id = dept_id,
            dept_name = dept_name,
            description =  description,
            created =created,
            updated = updated,
        )
         department.save()
         return redirect("all_department")
    return render(request, 'department.html',{'department': department} )

def delete_deaprtment(request, id):
    department = Department.objects.filter(id=id)
    department.delete()

    return redirect("all_departments")