from django.urls import path
from .views import CreateStudent, SeeAllStudents, DeleteStudent, EditStudent, CreateCourses, EditCourse, SeeAllCourses,DeleteCourse,NonCompulsoryToStudent,StudentCourseInfo

urlpatterns = [
    path('create_student/', CreateStudent.as_view(), name="create-student"),
    path('update_student/', EditStudent.as_view(), name="update_student"),
    path('delete_student/', DeleteStudent.as_view(), name="delete_student"),
    path('all_students/', SeeAllStudents.as_view(), name="all_students"),
    path('create_course/',CreateCourses.as_view(), name="create_course"),
    path('edit_course/',EditCourse.as_view(), name="edit_course"),
    path('see_all_cources/', SeeAllCourses.as_view(), name='see_all_cources'),
    path('delete_course/', DeleteCourse.as_view(), name='delete_course'),
    path('assign_course/', NonCompulsoryToStudent.as_view(), name='assign_course'),
    path('student_course_info/', StudentCourseInfo.as_view(), name='student_course_info')
]