from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_list, name='all-roles'),
    path('add-role/', views.add_role, name="addrole"),
    path('update-role/<str:id>', views.update_role, name="update"),
    path('delete/<str:id>', views.delete_role, name="delete"),
]
