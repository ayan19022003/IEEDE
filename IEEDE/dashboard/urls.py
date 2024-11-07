from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.home , name="home"),
    ## citizens
    path('citizen-login/',views.citizen_login , name="citizen_login"),
    path('forgot-password/',views.forgot_password , name="forgot_password"),
    path('citizen-skillset/',views.citizen_skillset , name="citizen_skillset"),
    path('personal-profile/',views.personal_profile , name="personal_profile"),
    path('citizen-education-profile/',views.citizen_education_profile , name="citizen_education_profile"),
    ## institutions
    path('institution-login/',views.institution_login , name="institution_login"),
    path('institution/',views.institution , name="institution"),
    path('institution-staff/',views.institution_staff , name="institution_staff"),
    ## employees
    path('search-job/',views.search_job , name="search_job"),
    path('employer-login/',views.employer_login , name="employer_login"),
]
