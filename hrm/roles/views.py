
from django.shortcuts import render, redirect
from .models import Role

# Create your views here.

def role_list(request):
    role = Role.objects.all()
    return render(request, "roles.html", {"all_roles":role})

from .models import Role

def add_role(request):
    if request.method == "POST":
        role_id = request.POST.get('role_id')
        role_name = request.POST.get('role_name')
        description = request.POST.get('description')

        if role_id and role_name:
            try:
                role = Role(
                    role_id=role_id,
                    role_name=role_name,
                    description=description,
                )
                role.save()
                return redirect("all-roles")  # Make sure this URL is working
            except Exception as e:
                return render(request, "roles.html", {
                    "error": f"Error saving role: {e}",
                    "all_roles": Role.objects.all()
                })
        else:
            return render(request, "roles.html", {
                "error": "Role ID and Name are required.",
                "all_roles": Role.objects.all()
            })

    # This ensures data is sent even on GET
    return render(request, "roles.html", {"all_roles": Role.objects.all()})

def update_role(request, id):
    if request.method == "POST":
         role_id = request.POST.get('role_id')
         role_name = request.POST.get('role_name')
         description = request.POST.get('description')
         created = request.POST.get('created')
         updated = request.POST.get('updated')

         role = Role(
            role_id = role_id,
            role_name = role_name,
            description =  description,
            created =created,
            updated = updated,
        )
         role.save()
         return redirect("all_role")
    return render(request, 'role.html',{'role': role} )

def delete_role(request, id):
    role = Role.objects.filter(id=id)
    role.delete()

    return redirect("all_roles")