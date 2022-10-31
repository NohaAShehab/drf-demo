import http
import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from students.models import Student
from students.api.serializers import StudentSerlizer


# @csrf_exempt
# def students_index(request):
#     if request.method=="GET":
#         students = Student.objects.all()
#         # return JsonResponse(students)
#         serliazed_students = []
#         for std in students:
#             serliazed_students.append({
#                 "href": reverse("api.students.show", args=[std.id]),
#                 "id": std.id,
#                 "name": std.name,
#                 "grade":std.grade,
#                 # "track":std.track.id if std.track else None,
#                 "track":{
#                   "id": std.track.id if std.track else None,
#                   "name": std.track.name  if std.track else None,
#                 },
#                 "created_at": std.created_at,
#                 "updated_at": std.updated_at
#             })
#
#         # return JsonResponse({"students":serliazed_students}) # return dict
#         # return JsonResponse( serliazed_students, safe=False)  # return list of dicts
#         return JsonResponse( serliazed_students, safe=False, status=http.HTTPStatus.OK)  # return list of dicts
#     elif request.method=="POST":
#         print(request.body)
#         body = json.loads(request.body)
#         print(body)
#         student =Student.objects.create(name=body["name"], grade=body["grade"])
#         serialized_student = {
#             "id": student.id,
#             "name": student.name,
#             "grade": student.grade,
#             # "track":std.track.id if std.track else None,
#             "track": {
#                 "id": student.track.id if student.track else None,
#                 "name": student.track.name if student.track else None,
#             },
#             "created_at": student.created_at,
#             "updated_at": student.updated_at
#         }
#
#         return JsonResponse(serialized_student, status=http.HTTPStatus.CREATED)
#
#
# @csrf_exempt
# def student_show(request, id):
#     student = get_object_or_404(Student, pk=id)
#     if request.method =="GET":
#         serialized_student= {
#                 "id": student.id,
#                 "name": student.name,
#                 "grade":student.grade,
#                 # "track":std.track.id if std.track else None,
#                 "track":{
#                       "id": student.track.id if student.track else None,
#                       "name": student.track.name  if student.track else None,
#                 },
#                 "created_at": student.created_at,
#                 "updated_at": student.updated_at
#             }
#
#         return JsonResponse(serialized_student,  status=http.HTTPStatus.OK)
#     elif request.method =="PUT":
#         # student.update(**request.body)
#         body = json.loads(request.body)
#         student.name= body["name"]
#         student.grade = body["grade"]
#         student.save()
#         # serialized_student = {
#         #     "id": student.id,
#         #     "name": student.name,
#         #     "grade": student.grade,
#         #     # "track":std.track.id if std.track else None,
#         #     "track": {
#         #         "id": student.track.id if student.track else None,
#         #         "name": student.track.name if student.track else None,
#         #     },
#         #     "created_at": student.created_at,
#         #     "updated_at": student.updated_at
#         # }
#         # return JsonResponse(serialized_student,  status=http.HTTPStatus.OK)
#         return JsonResponse(serliaze_student(student), status=http.HTTPStatus.OK)
#
#     elif request.method =="DELETE":
#         if student:
#             student.delete()
#             return JsonResponse({"delete":1}, status=http.HTTPStatus.NO_CONTENT)
#         else:
#             return JsonResponse({"msg": "object already deleted"}, status=http.HTTPStatus.RESET_CONTENT)
#

"""
    Get students/   200
    POST Students   201
    Get students/id  200
    put students/id   200
    patch students/id 200
    delete students/id 204(no content) first time delete,
     205 (reset content) --> if you try to delete it --> 
     reset content --? remove the cache



"""

def serliaze_student(student):
    return {
            "id": student.id,
            "name": student.name,
            "grade": student.grade,
            # "track":std.track.id if std.track else None,
            "track": {
                "id": student.track.id if student.track else None,
                "name": student.track.name if student.track else None,
            },
            "created_at": student.created_at,
            "updated_at": student.updated_at
        }



@api_view(["GET", "POST"])
def students_index(request):
    if request.method=="GET":
        students = Student.objects.all()
        serliazed_students = StudentSerlizer(students, many=True)
        return Response( serliazed_students.data, status=http.HTTPStatus.OK)  # return list of dicts

    elif request.method=="POST":
        print(request.body)
        student = StudentSerlizer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_201_CREATED)

        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "PUT", "DELETE"])
def student_show(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method =="GET":
        serialized_student= StudentSerlizer(student)
        return Response(serialized_student,  status=http.HTTPStatus.OK)
    elif request.method =="PUT":
        student= StudentSerlizer(instance=student, data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_200_OK)
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =="DELETE":
        if student:
            student.delete()
            return JsonResponse({"delete":1}, status=http.HTTPStatus.NO_CONTENT)
        else:
            return JsonResponse({"msg": "object already deleted"}, status=http.HTTPStatus.RESET_CONTENT)

