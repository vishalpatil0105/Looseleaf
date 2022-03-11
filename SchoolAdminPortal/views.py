from django.shortcuts import render
from django.shortcuts import render
from django.http.request import QueryDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students, Courses

# Create your views here.
from SchoolAdminPortal.serializers import StudentSerializers,CoursesSerializers


def format_response(data, status=200):
    context = {
        'status': status,
        'data': data
    }
    return context


# Create student
class CreateStudent(APIView):
    def post(self, request):
        try:
            if request.method == "POST" or request.method == "post":
                data = QueryDict.dict(request.data)
                if data:
                    first_name = data.get('first_name', None)
                    last_name = data.get('last_name', None)
                    standard = data.get('standard', None)
                    roll_no = data.get('roll_no', None)
                    if first_name and last_name and standard:
                        serializer = StudentSerializers(data=data)
                        is_valid = serializer.is_valid()
                        if is_valid:
                            serializer.save()
                            return Response(
                                format_response(
                                    {'message': f"Student {first_name + ' ' + last_name} Created Successfully"}, 201),
                                status=status.HTTP_201_CREATED)
                        else:
                            return Response(
                                format_response(
                                    {'message': f"Unexpected Error Occured in serializer"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(
                            format_response({'message': f"Unexpected Required Data not found Please Check Request Body"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        format_response({'message': f"Unexpected Request No Data found"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(format_response({'message': f"Unexpected Request method {request.method} found"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(format_response({'message': f"Exception encountered while user signing up:{e}"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)


# Edit student
class EditStudent(APIView):
    def put(self, request):
        try:
            if request.method == "PUT" or request.method == "put":
                data = QueryDict.dict(request.data)
                if data:
                    id = data.get('id', None)
                    first_name = data.get('first_name', None)
                    last_name = data.get('last_name', None)
                    standard = data.get('standard', None)
                    # roll_no = data.get('roll_no', None)
                    if id:
                        try:
                            is_present = Students.objects.get(id=id)
                            is_present.first_name = first_name if first_name else is_present.first_name
                            is_present.last_name = last_name if last_name else is_present.last_name
                            is_present.standard = standard if standard else is_present.standard
                            is_present.save()
                            return Response(
                                format_response(
                                    {'message': f"Student has been updated successfully."}, 200),
                                status=status.HTTP_200_OK)
                        except Exception as e:
                            return Response(
                                format_response(
                                    {'message': f"Student With the provided id is not present in the Database."}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(
                            format_response({'message': f"Id is Required to update profile"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        format_response({'message': f"Data is not present in the request body"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(format_response({'message': f"Unexpected Request method {request.method} found"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(format_response({'message': f"Exception encountered while user signing up:{e}"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)


# Delete student
class DeleteStudent(APIView):
    def delete(self,request):
        try:
            if request.method == "delete" or request.method == "DELETE":
                data = QueryDict.dict(request.data)
                if data:
                        id = data.get('id', None)
                        if id:
                            id_ = Students.objects.filter(id=id)
                            if id_:
                                id_.delete()
                                return Response(
                                    format_response(
                                        {'message': f"Student with given id is deleted successfully"}, 200),
                                    status=status.HTTP_200_OK)
                            else:
                                return Response(
                                    format_response({'message': f"Student with given id is not present in the database"}, 400),
                                    status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response(
                                format_response({'message': f"Expected Data not present in the request body"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        format_response({'message': f"Data is not present in the request body"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(format_response({'message': f"Exception encountered:{e}"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(format_response({'message': f"Exception encountered{e}"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)


# View all students
class SeeAllStudents(APIView):
    def get(self,request):
        try:
            students = Students.objects.all()
            serialized_var = StudentSerializers(students, many=True).data
            context = {
                'message': 'Students fetched successfully',
                'Students': serialized_var
            }
            return Response(format_response(context))
        except Exception as e:
            return Response(format_response({'message':f"Exception while{e}"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)


# Create course
class CreateCourses(APIView):
    def post(self,request):
        try:
            if request.method == "POST" or request.method == "post":
                data = QueryDict.dict(request.data)
                if data:
                    course_name = data.get('course_name', None)
                    standard = data.get('standard', None)
                    is_compulsory = data.get('is_compulsory', None)
                    if course_name and standard:
                        students = Students.objects.all()
                        serialized_var = StudentSerializers(students, many=True).data
                        if is_compulsory == "True":
                            for each in serialized_var:
                                data['student_id'] = each.get('id')
                                serializer = CoursesSerializers(data=data)
                                is_valid = serializer.is_valid()
                                if is_valid:
                                    serializer.save()
                                    course = Courses.objects.filter(course_name=course_name).first()
                                    student = Students.objects.get(pk=each.get('id'))
                                    course.student_id = student
                                    course.save()
                            return Response(
                                format_response({'message': f"Course Created Successfully"}, 201),
                                status=status.HTTP_201_CREATED)
                        else:
                            data['student_id'] = serialized_var[0].get('id')
                            serializer = CoursesSerializers(data=data)
                            is_valid = serializer.is_valid()
                            if is_valid:
                                serializer.save()
                                course = Courses.objects.filter(course_name=course_name).first()
                                student = Students.objects.get(pk=serialized_var[0].get('id'))
                                course.student_id = student
                                # course.student_id = int(serialized_var[0].get('id'))
                                course.save()
                                return Response(
                                    format_response({'message': f"Course Created Successfully"}, 201),
                                    status=status.HTTP_201_CREATED)
                            else:
                                return Response(
                                    format_response({'message': f"Error"}, 400),
                                    status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(
                            format_response({'message': f"Unexpected Request method {request.method} found"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        format_response({'message': f"Unexpected Request method {request.method} found"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(format_response({'message': f"Unexpected Request method {request.method} found"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(format_response({'message': f"Exception :{e}"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)


# Edit course
class EditCourse(APIView):
    def put(self,request):
        try:
            if request.method == "put" or request.method == "PUT":
                data = QueryDict.dict(request.data)
                if data:
                    id = data.get("id", None)
                    course_name = data.get('course_name', None)
                    standard = data.get('standard', None)
                    student_id = data.get('student_id', None)
                    if id:
                        try:
                            # print(Courses.objects.get(id=id))
                            course = Courses.objects.get(id=id)
                            course.course_name = course_name if course_name else course.course_name
                            course.standard = standard if standard else course.standard
                            course.student_id = student_id if Students.objects.filter(id=id).exists() else course.student_id
                            course.save()
                            return Response(
                                format_response({'message': f"Course Updated Successfully"}, 400),
                                status=status.HTTP_400_BAD_REQUEST) if Students.objects.filter(id=student_id).exists() else Response(
                                format_response({'message': f"Course Updated Successfully But as student id was not present in database  Please Create Student"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
                        except Exception as e:
                            return Response(
                                format_response({'message': f"Course is not present in the database {e}"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(format_response({'message': f"Data is Not Present In the Request body"}, 400),
                                    status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(format_response({'message': f"Exception :{e}"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)


# View all courses
class SeeAllCourses(APIView):
    def get(self,request):
        try:
            course = Courses.objects.all()
            serialized_var = CoursesSerializers(course, many=True).data
            context = {
                'message': 'Courses fetched successfully',
                'Students': serialized_var
            }
            return Response(format_response(context))
        except Exception as e:
            return Response(format_response({'message': f"Exception while{e}"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)


# Delete course
class DeleteCourse(APIView):
    def delete(self,request):
        try:
            data = QueryDict.dict(request.data)
            id = data.get('id', None)
            if Courses.objects.filter(id=id).exists():
                id_ = Courses.objects.get(id=id)
                id_.delete()
                return Response(
                    format_response(
                        {'message': f"Course with given id is deleted successfully"}, 200),
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    format_response(
                        {'message': f"Request Body is empty"}, 400),
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                format_response(
                    {'message': f"Error {e}"}, 400),
                status=status.HTTP_400_BAD_REQUEST)


# Assign non-compulsory course to a particular student
class NonCompulsoryToStudent(APIView):
    def post(self,request):
        try:
            data = QueryDict.dict(request.data)
            if data:
                course_id = data.get('course_id')
                student_id = data.get('student_id')
                if Students.objects.filter(id=student_id).exists() and Courses.objects.filter(id=course_id).exists():
                    check_course = Courses.objects.filter(pk=course_id).first()
                    if not check_course.is_compulsory:
                        assign = Courses.objects.create(course_name=check_course.course_name,standard=check_course.standard,
                                                        student_id=Students.objects.get(id=student_id))
                        assign.save()
                        return Response(
                            format_response(
                                {'message': f"Course Assign Successfully"}, 200),
                            status=status.HTTP_200_OK)
                    else:
                        return Response(
                            format_response(
                                {'message': f"Course is compulsory"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        format_response(
                            {'message': f"Required data is not found"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    format_response(
                        {'message': f"Request Body is found"}, 400),
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                format_response(
                    {'message': f"Error {e}"}, 400),
                status=status.HTTP_400_BAD_REQUEST)


# View courses of a particular student
class StudentCourseInfo(APIView):
    def post(self,request):
        try:
            data = QueryDict.dict(request.data)
            student_id = data.get('student_id')
            if Students.objects.filter(id=student_id).exists():
                student_data = Courses.objects.filter(student_id=student_id)
                # student_data = Courses.objects.filter(course_name="Bio")
                serialized_var = CoursesSerializers(student_data, many=True).data
                context = {
                    'message': 'Courses fetched successfully',
                    'Students': serialized_var
                }
                return Response(format_response(context))
            else:
                return Response(
                    format_response(
                        {'message': f"Student With provided id is not found in the dataset"}, 400),
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                format_response(
                    {'message': f"Error {e}"}, 400),
                status=status.HTTP_400_BAD_REQUEST)