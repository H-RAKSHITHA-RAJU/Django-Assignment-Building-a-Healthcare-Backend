from django.urls import path
from .views import (
    RegisterView, LoginView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    PatientDoctorMappingListCreateView, PatientDoctorMappingDetailView,
    PatientDoctorsListView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
    path('mappings/<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors-list'),
]