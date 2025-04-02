"""
URL configuration for Blooddonation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bloodDonationApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('login_db/',views.login_db),
    path('admin_home/',views.admin_home),
    path('add_organization/',views.add_organization),
    path('add_organization_db/',views.add_organization_db),
    path('delete_organaization/',views.delete_organaization),
    path('delete_organization_db/<int:Ornganization_id>',views.delete_organization_db),
    path('add_superUser/',views.add_superUser),
    path('add_superUser_db/',views.add_superUser_db),
    path('delete_superUser/',views.delete_superUser),
    path('delete_superUser_db/<int:User_id>',views.delete_superUser_db),
    path('superUser_home/',views.superUser_home),
    path('lgout/',views.lgout),
    path('lgout_Superuser/',views.lgout_Superuser),
    path('lgout_PU/',views.lgout_PU),
    path('lgout_USER/',views.lgout_USER),
    path('add_user/',views.add_user),
    path('add_user_db/',views.add_user_db),
    path('delete_user/',views.delete_user),
    path('delete_user_db/<int:User_id>',views.delete_user_db),
    path('add_area/',views.add_area),
    path('add_area_db/',views.add_area_db),
    path('delete_area/',views.delete_area),
    path('delete_area_db/<int:Area_code>',views.delete_area_db),
    path('add_hospital_superUser/',views.add_hospital_superUser),
    path('add_hospital_superUser_db/',views.add_hospital_superUser_db),
    path('delete_hospital_superUser/',views.delete_hospital_superUser),
    path('delete_hospital_superUser_db/<int:Hospital_id>',views.delete_hospital_superUser_db),
    path('Donor_registration_SU/',views.Donor_registration_SU),
    path('Donor_registration_SU_db/',views.Donor_registration_SU_db),
    path('donate_blood_db/<int:Donor_id>',views.donate_blood_db),
    path('view_donors_SU/',views.view_donors_SU),
    path('view_donors_db_SU/',views.view_donors_db_SU),
    path('Donor_report_SU/',views.Donor_report_SU),
    path('Donor_report_find/',views.Donor_report_find),
    path('export_donor_report_SU/',views.export_donor_report_SU),
    path('PU_home/',views.PU_home),
    path('PU_add_hospital/',views.PU_add_hospital),
    path('PU_add_hospital_db/',views.PU_add_hospital_db),
    path('PU_view_hospital/',views.PU_view_hospital),
    path('PU_donor_registration/',views.PU_donor_registration),
    path('PU_donor_registration_db/',views.PU_donor_registration_db),
    path('PU_donate_blood_db/<int:Donor_id>',views.PU_donate_blood_db),
    path('PU_donor_report/',views.PU_donor_report),
    path('PU_donor_report_find/',views.PU_donor_report_find),
    path('PU_export_donor_report/',views.PU_export_donor_report),
    path('USER_home/',views.USER_home),
    path('donor_search_SU/',views.donor_search_SU),
    path('donor_search_SU_db/',views.donor_search_SU_db),
    path('donate_blood_SU/<int:Donor_id>',views.donate_blood_SU),
    path('donate_blood_SU_db/',views.donate_blood_SU_db),
    path('Donor_edit_SU/<int:Donor_id>',views.Donor_edit_SU),
    path('Donor_edit_SU_db/',views.Donor_edit_SU_db),
    path('PU_donor_search/',views.PU_donor_search),
    path('PU_donor_search_db/',views.PU_donor_search_db),
    path('PU2_donate_blood/<int:Donor_id>',views.PU2_donate_blood),
    path('PU2_donate_blood_db/',views.PU2_donate_blood_db),
    path('PU_donor_edit/<int:Donor_id>',views.PU_donor_edit),
    path('PU_donor_edit_db/',views.PU_donor_edit_db),
    path('PU_view_donors/',views.PU_view_donors),
    path('PU_view_donors_db/',views.PU_view_donors_db),
    path('USER_donor_registration/',views.USER_donor_registration),
    path('USER_donor_registration_db/',views.USER_donor_registration_db),
    path('USER_donate_blood_db/<int:Donor_id>',views.USER_donate_blood_db),
    path('USER_donor_search/',views.USER_donor_search),
    path('USER_donor_search_db/',views.USER_donor_search_db),
    path('USER2_donate_blood/<int:Donor_id>',views.USER2_donate_blood),
    path('USER2_donate_blood_db/',views.USER2_donate_blood_db),
    path('USER_donor_edit/<int:Donor_id>',views.USER_donor_edit),
    path('USER_donor_edit_db/',views.USER_donor_edit_db),
    path('USER_donor_report/',views.USER_donor_report),
    path('USER_donor_report_find/',views.USER_donor_report_find),
    path('USER_export_donor_report/',views.USER_export_donor_report),
    path('USER_view_donors/',views.USER_view_donors),
    path('USER_view_donors_db/',views.USER_view_donors_db),
]
