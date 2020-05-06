from django.urls import path, include
from . import views

"""from views import (
    employee_list,
    employee_delete,
    employee_form
)
"""


urlpatterns = [
    path('', views.employee_form) ,
    path('<int:id>/', views.employee_form,name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name = 'delete_employee'),
    path('list/', views.employee_list)
]