from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import OrganizationCustomer, Customer, Organization, CustomUser

User = get_user_model()

class CheckUserAPIView(APIView):
    def post(self, request, org_uuid):
        """Checks if the user exists based on email"""
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        organization = Organization.objects.filter(api_url__contains=org_uuid).first()
        print("Organization: ",organization)

        if not organization:
            return Response({"error": "Invalid organization"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user already exists
        existing_customer = Customer.objects.filter(user__email=email).first()
        print("Existing User: ",existing_customer)

        if existing_customer:
            OrganizationCustomer.objects.get_or_create(organization=organization, customer=existing_customer)
            return Response({"message": "User registered successfully with the organization"}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "User not found. Proceed to full registration"}, status=status.HTTP_404_NOT_FOUND)


class CompleteRegistrationAPIView(APIView):
    def post(self, request, org_uuid):
        """Registers a new user with full details"""
        data = request.data
        email = data.get("email")

        # Verify the organization
        organization = Organization.objects.filter(api_url__contains=org_uuid).first()
        if not organization:
            return Response({"error": "Invalid organization"}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure user doesn't already exist
        if Customer.objects.filter(user__email=email).exists():  # Fix here
            return Response({"error": "User already exists, use Step One API"}, status=status.HTTP_400_BAD_REQUEST)

        # Create new user
        user = CustomUser.objects.create_user(
            username=data.get("username"), 
            email=email, 
            first_name=data.get("first_name"), 
            last_name=data.get("last_name"),
            gov_issued_number=data.get("gov_issued_number"),
            phone_number=data.get("phone_number"),
            address=data.get("address"),
            city=data.get("city"),
            nationality=data.get("nationality"),
            zip_code=data.get("zip_code"),
            kyc_verified=False
        )

        user.save()

        # Create a Customer profile & associate with the organization
        customer = Customer.objects.create(user=user)
        organization = Organization.objects.filter(api_url__contains=org_uuid).first()

        return Response({"message": "User fully registered"}, status=status.HTTP_201_CREATED)


