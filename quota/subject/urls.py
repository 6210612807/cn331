from django.urls import path

from . import views

app_name = "subject"

urlpatterns = [
        path('',views.index, name="index"),
        path('<int:subject_id>', views.course, name="subject")
    ]