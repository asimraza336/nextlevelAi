from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from django.contrib.sessions.models import Session
# from django.db.models import Q
from .forms import SignUpForm, SignInForm
from .models import *
from .func import get_linkedin_company_info
from django.contrib.auth.decorators import login_required, user_passes_test
# from .func_email import generate_sales_email
# from .func_email_final import generate_sales_email
from .generate_emails_final2 import generate_sales_email

USA_STATES = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'District of Columbia', 'Delaware',
 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana',
 'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York',
 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']


def Home(request):
    return render(request, 'main/home.html')

@login_required
def dashboard(request):
    context ={"user": request.user }
    quotes = Quotes.objects.all()
    print(quotes[0])
    # if datetime.today().date()
    context['quotation'] = quotes[0]
    if quotes[0]:
        if quotes[0].id:
            obj = Quotes.objects.get(id=quotes[0].id)
            obj.displayed_status = True
            obj.save()     
    return render(request, 'main/dashboard.html', context)
    
from django.http import JsonResponse, HttpResponse, Http404

def SignIn(request):
    # return render(request, 'accounts/SignIn.html')
    
    if request.user.is_authenticated:
        avatar_exist =Avatar.objects.filter(user=request.user).exists()
        if not avatar_exist:
            return redirect('Onboarding', pk=request.user.id)
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            # and not user.is_superuser
            if user is not None :
                login(request,user)
                # messages.success(request, 'successfully login')
                avatar_exist =Avatar.objects.filter(user=request.user).exists()
                if not avatar_exist:
                    return redirect('Onboarding', pk=request.user.id)
                
                return redirect('dashboard')
            else:
                # messages.error(
                    # request, 'Please enter correct username and password combination')
                return redirect('/')
        else:
            print(form.errors)
    else:
        form = SignInForm()
    context = {'form': form}
    return render(request, 'accounts/SignIn.html',context)

@login_required
def linkedinCompanyData(request):
    if request.is_ajax():
        # print(request.POST.get('linkedInCompany', None))
        linkedin_url = request.POST.get('linkedInCompany', None)
        # linkedin_url = "https://www.linkedin.com/company/arthrex"
        # linkedin_url = "https://www.linken.com/company/arthrex"

        company_info_final = get_linkedin_company_info(linkedin_url)
        # print(company_info_final)
        if company_info_final['message'] == 'Success':
            return JsonResponse(
                {
                    "success": True, 
                    "status_code": company_info_final['status_code'],
                    "results": company_info_final['results'][0],
                
                }
            ) # return the json response to ajax request.
        elif company_info_final['status_code'] == 500:
            return JsonResponse(
                {
                    "success": False, 
                    "status_code": 500,
                    "results": "Link not found, kindly check the link"
                
                }
            )

@login_required
def GenerateEmail(request):
    data = {}
    # print(request.POST)
    
    # if request.is_ajax():
    EmailCalls = request.POST.get('EmailCalls', None)
    
    data['sales_rep_name'] = request.user.first_name
    data['sales_rep_company_name'] = request.user.company
    data['sales_rep_Contact_Number'] = request.user.phone_number
    data['sales_rep_email'] = request.user.email
    data['sales_rep_company_Overview'] = request.user.user_avatar.overview
    data['sales_rep_company_Website'] = request.user.user_avatar.website if request.user.user_avatar.website else None
    data['sales_rep_company_Industry'] = request.user.user_avatar.industry
    data['sales_rep_company_Headquarters'] = request.user.user_avatar.headquaters if request.user.user_avatar.headquaters else None
    # data['sales_rep_company_Founded'] = "missing"
    data['sales_rep_company_Specialties'] = request.user.user_avatar.specialities
    
    
    data['Prospect_Company_name'] = request.POST.get('Prospect_Company_name', None)
    data['Prospect_Company_Overview'] = request.POST.get('Prospect_Company_Overview', None)
    data['Prospect_Company_Industry'] = request.POST.get('Prospect_Company_Industry', None)
    
    data['Prospect_Company_Headquarters'] = request.POST.get('Prospect_Company_Headquarters', None)
    data['Prospect_Company_Size'] = request.POST.get('Prospect_Company_Size', None)
    data['Prospect_Company_founded'] = request.POST.get('Prospect_Company_founded', None)
    
    data['Prospect_Company_specialties'] = request.POST.get('Prospect_Company_specialties', None)
    data['focus_area'] = request.POST.get('focus_area', None)
    
    data['Intent'] = request.POST.get('Intent', None)
    data['Prospect_Title_list'] = request.POST.getlist('Prospect_Title_list[]', None)
    data['Financial_Report'] = "Financial Report"
    # data['Financial_Report'] = """Analyzing the provided balance sheet and income statement, the EBITDA (Earnings Before Interest, Taxes, 
    # Depreciation, and Amortization) can be calculated. However, the balance sheet and income statement provided 
    # lacks details on Interest and Taxes. Based on the available information, we can compute EBITDA as follows: 
    # EBITDA = Operating Income + Depreciation Expense.For 2021: EBITDA = $277,926,767 (Operating Income) + $81,884,594 
    # (Depreciation Expense) = $359,811,361.To drive costs out, T-Mobile for Business can offer IoT solutions that can
    # help automate various processes, reduce manual labor, and improve efficiency, thus reducing overall operational costs.
    # For example, IoT can be used in inventory management, equipment maintenance, and energy management. Further, T-Mobile
    # can provide cost-effective rural internet solutions, which can help in reducing IT infrastructure costs. T-Mobile for
    # Business can help offset debt and liabilities by providing cost-effective solutions that can increase net income, thus
    # enhancing the company's ability to service its debts. Additionally, T-Mobile can offer bundled services, which can
    # provide better value and potentially generate more revenue.By implementing IoT and rural internet, T-Mobile for Business
    # can enhance CareSource's service delivery, especially in rural areas. This can lead to improved patient experience,
    # which can result in increased memberships and revenue. Moreover, IoT can be used to improve healthcare initiatives such
    # as remote patient monitoring, telemedicine, and smart medical devices, leading to better healthcare outcomes.From a
    # medical devices perspective, T-Mobile for Business can support CareSource by providing connectivity solutions for
    # medical devices, making them smarter and more efficient. This can lead to improved patient care, operational efficiency,
    # and cost savings.Electronic Visit Verification (EVV) is a technology that verifies when caregiver visits occur and documents
    # the precise time services begin and end. T-Mobile for Business can enhance EVV for CareSource by providing robust, reliable,
    # and secure connectivity solutions that can ensure seamless data transmission, thus improving the accuracy and reliability of EVV.
    # Please note that the 
    # effectiveness of these strategies would depend on various factors and would require thorough feasibility and impact analysis."""
    # print(request.POST.getlist('Prospect_Title_list[]', None))
    data['Grant'] = "EPA-G2023-STAR-H1"
    # print(data)
    # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++=')
    # print(data['Prospect_Company_name'])
    # print(data['Prospect_Company_Overview'])
    
    # print(data['Prospect_Company_Industry'])
    # print(data['Prospect_Company_Headquarters'])
    # print(data['Prospect_Company_Size'])
    # print(data['Prospect_Company_founded'])
    
    # print(data['Prospect_Company_specialties'])
    # print(data['focus_area'])
    # print(data['Intent'])
    print('ajksnkjans')
    print('ajksnkjans')
    
    generated_emails = generate_sales_email(data)
    # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=')
    # print(generated_emails)
    # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=')
    

    # print(generated_emails['results'])
    if generated_emails['message'] == 'Success':
        avatar_object = Avatar.objects.get(user= request.user)
        
        if avatar_object.remaing_email_request > 0:
            EmailCalls_int = int(EmailCalls)
            avatar_object.remaing_email_request -= EmailCalls_int
            email_count = avatar_object.remaing_email_request
            avatar_object.save()
        return JsonResponse(
            {
                "success": True, 
                "status_code": generated_emails['status_code'],
                "results": generated_emails['results'],
                "Email_Count": email_count 
            
            }
        ) # return the json response to ajax request.
    elif generated_emails['status_code'] == 500:
        return JsonResponse(
            {
                "success": False, 
                "status_code": 500,
                "results": "Link not found, kindly check the link"
            
            }
        )



    
from csv import reader
from .financial_reports import generate_financial_insights, generate_grants
@login_required
def ExtractGrantCsv(request):
    
    data = {}
    csvfile = request.FILES.get('file', None)
    result = ''
    decoded_file = csvfile.read().decode('utf-8')
    return JsonResponse(
            {
                "success": True, 
                "status_code": 200,
                "result": decoded_file
            
            })

@login_required
def GenerateGrant(request):
    data = {}
    data['sales_rep_company_name'] = request.user.company
    data['sales_rep_company_overview'] = request.user.user_avatar.overview
    data['sales_rep_company_industry'] = request.user.user_avatar.industry
    data['sales_rep_company_headquarters'] = request.user.user_avatar.headquaters if request.user.user_avatar.headquaters else None
    data['sales_rep_company_specialties'] = request.user.user_avatar.specialities
    
    data['prospect_company_name'] = request.POST.get('Prospect_Company_name', None)
    data['prospect_company_overview'] = request.POST.get('Prospect_Company_Overview', None)
    data['prospect_company_industry'] = request.POST.get('Prospect_Company_Industry', None)
    data['prospect_company_headquarters'] = request.POST.get('Prospect_Company_Headquarters', None)
    data['prospect_company_size'] = request.POST.get('Prospect_Company_Size', None)
    data['prospect_company_founded'] = request.POST.get('Prospect_Company_founded', None)
    data['prospect_company_specialties'] = request.POST.get('Prospect_Company_specialties', None)
    data['grants_raw_data'] = request.POST.get('grants_raw_data', None)
    
    grants = generate_grants(data)
    print(grants)
    # print(grants[0])
    avatar_object = Avatar.objects.get(user= request.user)
        
    if avatar_object.remaing_grant_request > 0:
        avatar_object.remaing_grant_request -= 1
        GrantCalls_count = avatar_object.remaing_grant_request
        avatar_object.save()
    return JsonResponse(
        {
            "success": True, 
            "status_code": 200,
            "grantsResult": grants,
            "GrantCalls_count": GrantCalls_count if GrantCalls_count else None 
        
        }
    ) 
    

@login_required
def GenerateFinancialReport(request):
    data = {}
    # print(request.POST)
    
    # if request.is_ajax():
    data['sales_rep_company_name'] = request.user.company
    data['sales_rep_company_overview'] = request.user.user_avatar.overview
    data['sales_rep_company_industry'] = request.user.user_avatar.industry
    data['sales_rep_company_headquarters'] = request.user.user_avatar.headquaters if request.user.user_avatar.headquaters else None
    data['sales_rep_company_specialties'] = request.user.user_avatar.specialities
    
    
    data['prospect_company_name'] = request.POST.get('Prospect_Company_name', None)
    data['prospect_company_overview'] = request.POST.get('Prospect_Company_Overview', None)
    data['prospect_company_industry'] = request.POST.get('Prospect_Company_Industry', None)
    
    data['prospect_company_headquarters'] = request.POST.get('Prospect_Company_Headquarters', None)
    data['prospect_company_size'] = request.POST.get('Prospect_Company_Size', None)
    data['prospect_company_founded'] = request.POST.get('Prospect_Company_founded', None)
    
    data['prospect_company_specialties'] = request.POST.get('Prospect_Company_specialties', None)
    data['focus_area'] = request.POST.get('focus_area', None)
    
    data['financial_raw_data'] = request.POST.get('financial_raw_data', None)
    
    generate_financial_insight = generate_financial_insights(data)
    print(generate_financial_insight)

    # print(generate_financial_insight['results'])
    if generate_financial_insight['message'] == 'Success':
        avatar_object = Avatar.objects.get(user= request.user)
        
        if avatar_object.remaing_financial_request > 0:
            avatar_object.remaing_financial_request -= 1
            FinancialCalls_count = avatar_object.remaing_financial_request
            avatar_object.save()
            
        return JsonResponse(
            {
                "success": True, 
                "status_code": 200,
                "insights": generate_financial_insight['insights'],
                "FinancialCount": FinancialCalls_count 
                # if FinancialCalls_count else None
            }
        ) # return the json response to ajax request.
    # elif generated_emails['status_code'] == 500:
    #     return JsonResponse(
    #         {
    #             "success": False, 
    #             "status_code": 500,
    #             "results": "Link not found, kindly check the link"
            
    #         }
    #     )
    
@login_required
def Settings(request):
    if request.method == "POST":
        # print(request.POST)
        
        avatar_option = request.POST.getlist('avatar_option', None)
        if avatar_option == 'Other':
            avatar_option = avatar_option[0] + ', ' + avatar_option[1] 
        else:
            avatar_option = avatar_option[0]
        
        
        
        fullName = request.POST.get('fullName', None)
        companyName = request.POST.get('companyName', None)
        jobTitle = request.POST.get('jobTitle', None)
        # email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        role = request.POST.get('role', None)
        salesArea = request.POST.getlist('salesArea', None) 
        Industries = request.POST.get('Industries', None)
        Territories = request.POST.getlist('Territories', None) 
        overview = request.POST.get('overview', None)
        specialities = request.POST.get('specialities', None)
        website = request.POST.get('website', None)
        industry_type = request.POST.get('industry_type', None)
        headquarters = request.POST.get('headquarters', None)
        company_size = request.POST.get('company_size', None)
        
        gmail = request.POST.get('gmail', None)
        gmail_password = request.POST.get('gmail_password', None)
        
        
        user_object = User.objects.get( id=request.user.id)
        avatar_object = Avatar.objects.get( user=user_object)

        
        user_object.first_name = fullName
        # user_object.email = email
        user_object.company = companyName
        user_object.job_title = jobTitle
        user_object.phone_number = phone
        user_object.job_title = jobTitle
        
        user_object.save()
        
        # avatar_object.name
        
        
        sale_result =''
        for sale in salesArea:
            if sale:
                if sale_result: 
                    sale_result = sale_result + ',' + sale
                else:
                    sale_result = sale_result + sale
        Territory_result = ''       
        for terr in Territories:
            if terr:
                if Territory_result: 
                    Territory_result = Territory_result + ',' + terr
                else:
                    Territory_result = Territory_result + terr
                
        avatar_val = avatar_option
        if avatar_val:
            avatar_object.name = avatar_val
        
        avatar_object.role = role
        avatar_object.industry = Industries
        avatar_object.sale_area = sale_result
        avatar_object.territory = Territory_result
        avatar_object.overview = overview
        avatar_object.website = website
        avatar_object.industry_type = industry_type
        avatar_object.specialities = specialities
        avatar_object.company_size = company_size
        avatar_object.headquaters = headquarters
        
        avatar_object.gmail = gmail
        avatar_object.gmail_password = gmail_password
        avatar_object.save()
        
        print('accounts user updated -------------------------------')
        print('accounts user updated -------------------------------')
        return redirect('dashboard')
        
    context = {
        "user": request.user, 'USA_STATES': USA_STATES
    }
    return render(request, 'main/Settings.html', context)    
       
       
       


def SignUp(request):

    if request.method == 'POST':
        print(type(request.POST))
        
        print(request.POST)
        changed_data = request.POST.copy()
        print(type(changed_data))
        
        # changed_data['username'] = changed_data['email'] 
        
        print(changed_data)
        data = request.POST

        # set to mutable
        data._mutable = True

        # modify the values in data 
        # data[modified_field] = new_value
        data['username'] = data['email'] 
        

        # set mutable flag back (optional)
        data._mutable = False
        print(data)
        form = SignUpForm(data = data)
        
        if form.is_valid():
            user = form.save()
            # return redirect('SignIn')
            return render(request, 'avatar/new_avatar.html', {'user_id': user.id, 'USA_STATES': USA_STATES})
            
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'accounts/SignUp.html', {'form': form})

import json
import os
import stripe
Publishable_key = "pk_test_51NSnLkCMWfx6SbqWJuSj1Rrnz4TCcfWtl7B570QtRrnhxFdWwKpbzz1tD9XKX2EIeyDmCRYFehrUSPbeTJTkALDZ00PbSQaA4x"
stripe.api_key = "sk_test_51NSnLkCMWfx6SbqWiP16PTWjAvaZspeDyuPqO5Wmb58M2LnwKKbmwQVzfpez0ifqjznq0FJr5pYtPsjHLT8yxZdL00xrlOnkoS"

def Pricing(request):
    if request.method == 'POST':
        membership = "MONTHLY"
        amount = 10
        # if membership == "YEARLY":
        #     amount = 100
        customer = stripe.Customer.create(
            email = request.user.email,
            source = request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer = customer,
            amount = 10,
            currency = 'usd',
            description = "membership",
            # metadata={'integration_check': 'accept_a_payment'},
        )
        # intent = stripe.PaymentIntent.create(
        #     amount=1099,
        #     currency='usd',
        #     # Verify your integration in this guide by including this parameter
        #     metadata={'integration_check': 'accept_a_payment'},
        # )
    return render(request, 'main/Pricing.html')

@login_required
def stripe_landing(request):

    return render(request, 'main/stripe_landing.html')

@login_required
def CreateCheckoutSessionView(request):
    if request.method == 'POST':
        print(request.POST)
        price = request.POST.get('price')
        payment_plan = request.POST.get('payment_plan', None)
        print(price)
        print(price)        
        print(price)        
                
        print(type(price))
        price_in_float = float(price)
        print(price_in_float)
        price_in_cents = price_in_float * 100
        # price = Price.objects.get(id=self.kwargs["pk"])
        domain = "http://127.0.0.1:8000/"
        # if settings.DEBUG:
        #     domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    # 'price': 20,
                    'price_data':{
                        'currency': 'usd',
                        'unit_amount': int(price_in_cents),
                        'product_data':{
                            'name': 'abc'
                        }
                    },
                    'quantity': 1,
                },
            ],
            metadata={
              "user_id": request.user.id,
              "payment_type": payment_plan
            },
            mode='payment',
            success_url=domain + 'success',
            cancel_url=domain + 'cancel',
            automatic_tax={'enabled': True}
        )
        print(checkout_session)
        return redirect(checkout_session.url)
        # return JsonResponse({
        #     'id': checkout_session.url
        # })
        # return JsonResponse({
        #     'clientSecret': intent['client_secret']
        # })
import smtplib
import os


from django.conf import settings



from django.core.mail import EmailMessage, send_mail

# email = EmailMessage(
#     'Hello',
#     'Body goes here',
#     settings.EMAIL_HOST_USER,
#     ['asimraza336@gmail.com',],
#     ['asimraza336@gmail.com'],
# ).send()


from django.core import mail

# from django.core.mail import get_connection
# from django.core import mail
# connection = get_connection(
#     host='smtp.gmail.com',
#     port=587,
#     # username='asimraza336@gmail.com',
#     # password='bkhkixuovsmegjgc'
# )
# connection = get_connection(username='asimraza336@gmail.com', password='bkhkixuovsmegjgc', fail_silently=True)

    # .send()
    # mail.EmailMessage(
    #     "ABC",
    #     "XYZ HIII HELLO",
    #     "asimraza336@gmail.com",
    #     ["asimraza336@gmail.com"],
    #     auth_user="asimraza336@gmail.com",
    #     auth_password="bkhkixuovsmegjgc",
    #     connection=connection,
    # ).send()

# email = EmailMessage(
#     'Hello',
#     'Body goes here',
#     settings.EMAIL_HOST_USER,
#     ['asimraza336@gmail.com',],
#     ['asimraza336@gmail.com'],
#     # auth_user="asimraza336@gmail.com",
#     # auth_password="bkhkixuovsmegjgc",
#     connection=connection
# ).send()

from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
# import datetime
# import data
from datetime import datetime
from dateutil.relativedelta import relativedelta
@csrf_exempt
def stripe_webhook(request):

    # For now, you only need to print out the webhook payload so you can see
    # the structure.
    # print(payload.json())
    print('webhook   webhook   webhook   webhook   webhook   webhook   ')
    print('webhook   webhook   webhook   webhook   webhook   webhook   ')
    print('webhook   webhook   webhook   webhook   webhook   webhook   ')
    print('webhook   webhook   webhook   webhook   webhook   webhook   ')
    print('webhook   webhook   webhook   webhook   webhook   webhook   ')
    
    payload = request.body
    # result = json.loads(request.body)
    # print(json.loads(payload))
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, "whsec_950530349f955878e0280a9b1a9d1c680bf8207933cec995c985174d3cf36faa"
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
    # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )
        # print(session)
        line_items = session.line_items
        # Fulfill the purchase...
        print(session['payment_status'])
        # print(event['type'])
        customer_email = session['customer_details']['email']
        user_id = session['metadata']['user_id']
        payment_type = session['metadata']['payment_type']
        user_instance = User.objects.get(id=user_id)
        user_avatar_instance = Avatar.objects.get(user=user_instance)
        user_avatar_instance.membership_type = payment_type
        user_avatar_instance.paid_date = datetime.today().date()
        user_avatar_instance.is_not_expired = True
        
        
        

        if payment_type == 'monthly':
            print("monthly   monthly   monthly   monthly   monthly   monthly   monthly")
            user_avatar_instance.remaing_email_request = 1000
            user_avatar_instance.remaing_financial_request = 20
            user_avatar_instance.remaing_grant_request = 30    
            date_after_month = datetime.today()+ relativedelta(months=1)
            user_avatar_instance.expire_membership_date = date_after_month.strftime('%Y-%m-%d')
            # user_avatar_instance.remaing_request = ?

        if payment_type == 'yearly':
            print('YEarly   YEarly   YEarly   YEarly   YEarly   YEarly   YEarly   YEarly   YEarly   ')
            user_avatar_instance.remaing_email_request = 1000 * 12
            user_avatar_instance.remaing_financial_request = 20 * 12
            user_avatar_instance.remaing_grant_request = 30 * 12
            date_after_year = datetime.today()+ relativedelta(years=1)
            #  ['“27/08/2023” value has an invalid date format. It must be in YYYY-MM-DD format.']
            user_avatar_instance.expire_membership_date = date_after_year.strftime('%Y-%m-%d')
            # user_avatar_instance.remaing_request = ?
            
        user_avatar_instance.save()
        # print(customer_email)
        # send_mail(
        #     subject="here is your",
        #     message="Thanks for your purchase",
        #     recipient_list = ["asimraza336@gmail.com"],
        #     from_email="matt@test.com"
        # )
    # Passed signature verification
    return HttpResponse(status=200)

def send_email_dashboard(request):
    # User.objects.get(id=)
    email_receiver = request.POST.get('email_rec', None)
    email_body = request.POST.get('email_body', None)
    
    avatar_obj = Avatar.objects.get(user=request.user)
    
    
    with mail.get_connection() as connection:
        mail.send_mail(
            subject="NextLevelAi",
            message= email_body,
            from_email = avatar_obj.gmail,
            recipient_list =[email_receiver],
            # auth_user="asimraza336@gmail.com",
            # auth_password="bkhkixuovsmegjgc",
            auth_user=avatar_obj.gmail,
            auth_password=avatar_obj.gmail_password,
            # auth_password="Anonymous1$",
            fail_silently=True,
            connection=connection,
        )
        return JsonResponse({
            'emailSent': True,
            'Success': True 
        })

def create_payment_intent(request):
    try:
        pass
        # data = json.loads(request.data)
        # print(request.data)
        print(request.POST)
        # print(data)
        print('----------------------------')
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            payment_method_types = ['card'],
            amount=20,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        print('----------------------------')
        print('----------------------------')
        
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
        # return jsonify({
        #     'clientSecret': intent['client_secret']
        # })
    except Exception as e:
        print(e)
        pass
        # return jsonify(error=str(e)), 403
def checkout(request):
    return render(request, 'main/check2.html')

def create_checkout_session(request):
    try:
        print('ajkndkjans')
        print('ajkndkjans')
        print('ajkndkjans')
        print('ajkndkjans')
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    # 'price': '{{prod_OKs0hoWOF2BucV}}',
                    'price': 'price_1NYCGRCMWfx6SbqWHp1hfdPB',
                    
                    # "",
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="http://127.0.0.1:8000/" + 'success',
            cancel_url="http://127.0.0.1:8000/" + 'cancel',
            automatic_tax={'enabled': True},
        )
        print('byeeeeeeeeeeeeeeeeeeeeeeee')
        print('byeeeeeeeeeeeeeeeeeeeeeeee')
        print('byeeeeeeeeeeeeeeeeeeeeeeee')
        print('byeeeeeeeeeeeeeeeeeeeeeeee')
        
    except Exception as e:
        print('heloo')
        print('heloo')
        print('heloo')
        print('heloo')
        print('heloo')
        print(e)
        
        return str(e)

    return redirect(checkout_session.url, code=303)
def success(request):
    return render(request, 'main/success.html')

def cancel(request):
    return render(request, 'main/cancel.html')

def Learn(request):
    return render(request, 'main/learn.html')


def Onboarding(request, pk):
    
    if request.method == 'POST':
        avatar_option = request.POST.getlist('avatar_option')
        role = request.POST.get('role')
        salesArea = request.POST.getlist('salesArea')
        Industries = request.POST.get('Industries')
        Territories = request.POST.getlist('Territories')
        Overview = request.POST.get('Overview')
        Industry_type = request.POST.get('Industry_type')
        Specialities = request.POST.get('Specialities')
        Company_size = request.POST.get('Company_size')
        Website = request.POST.get('Website', None)
        Headquarters = request.POST.get('Headquarters', None)
        if avatar_option == 'Other':
            avatar_option = avatar_option[0] + ', ' + avatar_option[1] 
        else:
            avatar_option = avatar_option[0]
        sale_result =''
        for sale in salesArea:
            if sale:
                if sale_result: 
                    sale_result = sale_result + ',' + sale
                else:
                    sale_result = sale_result + sale
        Territory_result = ''       
        for terr in Territories:
            if terr:
                if Territory_result: 
                    Territory_result = Territory_result + ',' + terr
                else:
                    Territory_result = Territory_result + terr
        try:
            user = User.objects.get(id=pk)
            Avatar.objects.create(
                    user = user,
                    name = avatar_option,
                    role = role,
                    industry = Industries,
                    sale_area = sale_result,
                    territory = Territory_result,
                    overview = Overview,
                    website = Website if Website else None,
                    industry_type = Industry_type,
                    specialities = Specialities,
                    company_size = Company_size,
                    headquaters = Headquarters if Headquarters else None
            )
            return redirect('SignIn')
            
        except Exception as e:
            print(e)
    return render(request, 'avatar/new_avatar.html', {'user_id': pk, 'USA_STATES': USA_STATES})

# checkoxes
# headquaters
# website



