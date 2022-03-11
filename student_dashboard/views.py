from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StudentProfile, StudentMarkDetails
from .serializers import StudentProfileSerializer, StudentMarkDetailsSerializer


# displaying all the registered students
class StudentsList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, format = None):
        data = {}
        students_name = [user.username for user in User.objects.all()]
        data['All student in the classs'] = students_name
        # return Response({'Names': data})
        return Response(data)


# student home
class StudentHome(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        user1 = StudentProfile.objects.filter(user = user)
        print(user1)
        return StudentProfile.objects.filter(user = user)

    def get(self, request):
        data = {}
        user = request.user
        data['user'] = user.username
        return Response(data, status = status.HTTP_200_OK)


# Student profile create, update, edit view
class StudentProfileView(generics.GenericAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        serializer = StudentProfileSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = StudentProfile.objects.create(
                user = request.user,
                image = serializer.validated_data['image'],
                DOB = serializer.validated_data['DOB'],
                address = serializer.validated_data['address']
            )
            user.save()
            data['message'] = 'Profile fields added sucessfully'
        else:
            data = serializer.errors
            return Response(data, status = status.HTTP_400_BAD_REQUEST)
        return Response(data, status = status.HTTP_201_CREATED)
    
    def get(self, request):
        user = StudentProfile.objects.get(user = request.user)
        username = User.objects.get(username = request.user)
        data = {}
        data['username'] = username.username
        data['email'] = username.email
        data['image'] = str(user.image) 
        data['DOB'] = user.DOB
        data['address'] = user.address
        return Response ({'Profile Details' : data}, status = status.HTTP_200_OK)
    
    def put(self, request):
        user = StudentProfile.objects.get(user = request.user)
        data = {}
        serializer = StudentProfileSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            data['message'] = 'Profile updated sucessfully'
            return Response(data)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


# student academic details view
class StudentAcademicView(APIView):
    serializer_class = StudentMarkDetailsSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = StudentMarkDetailsSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            mark_details = StudentMarkDetails.objects.create(
                user = request.user,

                english_mark = serializer.validated_data['english_mark'],
                maths_mark = serializer.validated_data['maths_mark'],
                science_mark = serializer.validated_data['science_mark'],
                malayalam_mark = serializer.validated_data['malayalam_mark']
            )
            # calculating total mark
            total_mark = mark_details.english_mark+mark_details.maths_mark+mark_details.science_mark+mark_details.malayalam_mark
            mark_details.total_mark = total_mark
            # calculating percentage
            percentage = (mark_details.total_mark * 100)/ mark_details.grand_total
            mark_details.percentage = percentage
            if mark_details.percentage >=90 and mark_details.percentage<=100:
                mark_details.grade = "A+"
            elif mark_details.percentage >=80 and mark_details.percentage<=89:
                mark_details.grade = "A"
            elif mark_details.percentage >=70 and mark_details.percentage<=79:
                mark_details.grade = "B+"
            elif mark_details.percentage >=60 and mark_details.percentage<=69:
                mark_details.grade = "B"
            elif mark_details.percentage >=50 and mark_details.percentage<=59:
                mark_details.grade = "C"
            else:
                mark_details.grade = "F"

            if mark_details.grade == "A+":
                mark_details.final_result = "Outstanding"
            elif mark_details.grade == "A":
                mark_details.final_result = "Excellent"
            elif mark_details.grade == "B+":
                mark_details.final_result = "Very Good"
            elif mark_details.grade == "B":
                mark_details.final_result = "Good"
            elif mark_details.grade == "C":
                mark_details.final_result = "Average"
            else: 
                mark_details.final_result = "Fail"
            mark_details.save()
            data['message'] = 'Mark fields added sucessfully'
        else:
            data = serializer.errors
            return Response(data, status = status.HTTP_400_BAD_REQUEST)
        return Response(data, status = status.HTTP_201_CREATED)
         