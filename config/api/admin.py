from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Organization, Customer, OrganizationCustomer

# Custom User Admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("profile_picture", "is_organization", "organization_name",
                       "kyc_document", "gov_issued_number", "kyc_verified",
                       "phone_number", "address", "city", "nationality", "zip_code")
        }),
    )

# Inline for Customers under Organization
class CustomerInline(admin.TabularInline):
    model = OrganizationCustomer
    extra = 1

# Organization Admin with Customers Inline
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("user", "api_url")
    inlines = [CustomerInline]


class OrganizationCustomerInline(admin.TabularInline):
    model = OrganizationCustomer
    extra = 1

# Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "phone_number", "email", "address", "city", "nationality", "zip_code", "kyc_verified")
    search_fields = ("user__username", "user__email", "user__gov_issued_number")
    # list_filter = ("kyc_verified", "city", "nationality")
    
    def username(self, obj):
        return obj.user.username
    
    def full_name(self, obj):
        return obj.user.get_full_name()
    
    def email(self, obj):
        return obj.user.email

    def phone_number(self, obj):
        return obj.user.phone_number
    
    def address(self, obj):
        return obj.user.address
    
    def city(self, obj):
        return obj.user.city
    
    def nationality(self, obj):
        return obj.user.nationality
    
    def zip_code(self, obj):
        return obj.user.zip_code
    
    def kyc_verified(self, obj):
        return obj.user.kyc_verified

    # Allow filtering and searching based on KYC and identification number
    # list_filter = ("kyc_verified", "city", "nationality")
    search_fields = ("user__username", "user__email", "user__gov_issued_number")


# Organization-Customer Relation Admin
@admin.register(OrganizationCustomer)
class OrganizationCustomerAdmin(admin.ModelAdmin):
    list_display = ("organization", "customer", "date_joined")
    
    # Sort organization and customer alphabetically
    ordering = ("organization__user__organization_name", "customer__user__username")

    # Filters for better navigation
    list_filter = ("organization", "date_joined")

    # Search functionality for organization and customer
    search_fields = ("organization__user__organization_name", "customer__user__username")
