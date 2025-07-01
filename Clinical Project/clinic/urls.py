"""
URL configuration for clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from appone import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.patientListView.as_view(),name='index'),
    path('patient/',views.PatientCrateView.as_view()),
    path('update/<int:pk>/',views.PatientUpdateView.as_view()),
    path('delete/<int:pk>/',views.PatientDeleteView.as_view()),
    path('patient/<int:pk>/adddata/', views.adddata, name='adddata'),
    path('patient/<int:pk>/analyze/', views.analyze, name='analyze'),

    # path('adddata/<int:pk>/',views.adddata),
    # path('analyze/<int:Patient_id>/',views.analyze)
]
