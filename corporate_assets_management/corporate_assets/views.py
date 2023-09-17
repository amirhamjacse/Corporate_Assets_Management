from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import *
from rest_framework.views import APIView

class CompanyCreateViewAPI(
    generics.CreateAPIView
):
    serializer_class = CompanyInfoSerializer
    permission_classes = [IsAdminUser]


class CompanyListViewAPI(
    generics.ListAPIView
):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [IsAuthenticated]


class CompanyUpdateViewAPI(
    generics.RetrieveUpdateAPIView
):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [IsAdminUser]


class EmployeeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            try:
                employee = EmployeeInfo.objects.get(pk=pk)
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data)
            except EmployeeInfo.DoesNotExist:
                return Response(
                    {"error": "Employee not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            employees = EmployeeInfo.objects.all()
            serializer = EmployeeSerializer(
                employees, many=True
            )
            return Response(serializer.data)
    def put(self, request, pk, format=None):
        try:
            employee = EmployeeInfo.objects.get(pk=pk)
        except EmployeeInfo.DoesNotExist:
            return Response(
                {"error": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response(EmployeeSerializer(employee).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response(EmployeeSerializer(employee).data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            employee = EmployeeInfo.objects.get(pk=pk)
        except EmployeeInfo.DoesNotExist:
            return Response({"error": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
