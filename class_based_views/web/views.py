from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from class_based_views.web.models import Employee


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees.html'
    context_object_name = 'employees'


class EmployeeDetailsView(DetailView):
    model = Employee
    template_name = 'details.html'

    # context_object_name = 'employees'


class CreateEmployeeView(CreateView):
    model = Employee
    template_name = 'create_employee.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={
            'pk': self.object.pk,
        })
    # or just to employee page:
    #     return reverse_lazy('all_employees')


class UpdateEmployeeView(UpdateView):
    model = Employee
    template_name = 'update_employee.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={
            'pk': self.object.pk,
        })

    def dispatch(self, request, *args, **kwargs):
        # if the employee to update is the same as the user logged in => continue
        return super().dispatch(request, *args, **kwargs)


class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'delete_employee.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('all_employees')

