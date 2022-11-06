from django.urls import path

from class_based_views.web.views import IndexView, EmployeeListView, EmployeeDetailsView, CreateEmployeeView, \
    UpdateEmployeeView, DeleteEmployeeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('employees/', EmployeeListView.as_view(), name='all_employees'),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='details'),
    path('create/', CreateEmployeeView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateEmployeeView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteEmployeeView.as_view(), name='delete'),

]
