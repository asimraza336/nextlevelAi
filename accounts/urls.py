from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home, name='Home'),
    path('login', SignIn, name='SignIn'),
    path('register', SignUp, name='SignUp'),
    path('Pricing', Pricing, name='Pricing'),
    path('Learn', Learn, name='Learn'),
    
    
    path('Onboarding/<int:pk>', Onboarding, name='Onboarding'),
    
    path('dashboard', dashboard, name='dashboard'),
    path('linkedinCompanyData', linkedinCompanyData, name='linkedinCompanyData'),
    path('GenerateEmail', GenerateEmail, name='GenerateEmail'),
    path('GenerateFinancialReport', GenerateFinancialReport, name='GenerateFinancialReport'),
    path('ExtractGrantCsv', ExtractGrantCsv, name='ExtractGrantCsv'),
    path('GenerateGrant', GenerateGrant, name='GenerateGrant'),
    path('Settings', Settings, name='Settings'),
    path('checkout', checkout, name='checkout'),
    path('create-checkout-session', create_checkout_session, name='create-checkout-session'),
    #strip actual
    path('success', success, name='success'),
    path('cancel', cancel, name='cancel'),
    path('create-checkout', CreateCheckoutSessionView, name='create-checkout'),
    path('stripe_landing', stripe_landing, name='stripe_landing'),
    path('webhooks/stripe', stripe_webhook, name='stripe-webhook'),
    
    path('send_email_dashboard', send_email_dashboard, name='send_email_dashboard'),
    
    
    path('create-payment-intent', create_payment_intent, name='create-payment-intent'),
    
    
    
   
    
    
    
    
    
    
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    

]