from django.urls import path
from .views import CreateStudent, SeeAllStudents, DeleteStudent, EditStudent, CreateCourses, EditCourse, SeeAllCourses,DeleteCourse,NonCompulsoryToStudent,StudentCourseInfo

urlpatterns = [
    path('create_student/', CreateStudent.as_view(), name="create-student"),
    path('update_student/', EditStudent.as_view(), name="create-student"),
    path('delete_student/', DeleteStudent.as_view(), name="create-student"),
    path('all_students/', SeeAllStudents.as_view(), name="create-student"),
    path('create_course/',CreateCourses.as_view(), name="CreateCourses"),
    path('edit_course/',EditCourse.as_view(), name="CreateCourses"),
    path('see_all_cources/', SeeAllCourses.as_view(), name='seeAllCources'),
    path('delete_course/', DeleteCourse.as_view(), name='seeAllCources'),
    path('assign_course/', NonCompulsoryToStudent.as_view(), name='seeAllCources'),
    path('student_course_info/', StudentCourseInfo.as_view(), name='seeAllCources')
]