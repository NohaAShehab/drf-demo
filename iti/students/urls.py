
from django.urls import path
from students.api.views import students_index, student_show
urlpatterns =[
    path("api/index", students_index, name = 'api.students.index'),
    path("api/<int:id>", student_show, name = 'api.students.show')
]