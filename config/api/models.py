from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin

admin.site.site_header = "AM-HACK 5.0 Auth"
admin.site.site_title = "AM-HACK 5.0 Auth"
admin.site.index_title = "Welcome to Your Dashboard"

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    is_organization = models.BooleanField(default=False)
    organization_name = models.CharField(max_length=255, blank=True, null=True)

    # KYC & Authentication Details
    kyc_document = models.FileField(upload_to="kyc_documents/", blank=True, null=True)
    gov_issued_number = models.CharField(max_length=100, unique=True)
    kyc_verified = models.BooleanField(default=False)

    # Contact & Location
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    # Fix reverse accessor conflicts
    groups = models.ManyToManyField(
        "auth.Group", related_name="custom_users", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="custom_users_permissions", blank=True
    )

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"




class Organization(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="organization_profile")
    api_url = models.URLField(blank=True, null=True)
    official_domain = models.CharField(max_length=255, blank=True, null=True)
    customers = models.ManyToManyField("Customer", through="OrganizationCustomer", related_name="organizations_joined")
    
    def generate_api_url(self):
        import uuid
        domain_part = "http://127.0.0.1:7878"
        self.api_url = f"{domain_part}/auth/{uuid.uuid4()}"
        self.save()

    def __str__(self):
        return self.user.username  # Displays username instead of object reference
    
    class Meta:
        verbose_name = "Business Organization"
        verbose_name_plural = "Business Organizations"

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="customer_profile")
    associated_organizations = models.ManyToManyField(Organization, through="OrganizationCustomer", related_name="customers_enrolled")

    def __str__(self):
        return self.user.username  # Displays username instead of object reference

# Intermediate model to store additional details about the customer-organization relationship
class OrganizationCustomer(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    # shared_data = models.JSONField(default=dict)  # Track data shared with organization

    class Meta:
        verbose_name = "Customer of Organization"
        verbose_name_plural = "Customers of Organization"

# Signal to generate API URL for organizations on creation
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Organization)
def assign_api_url(sender, instance, created, **kwargs):
    if created:
        instance.generate_api_url()
