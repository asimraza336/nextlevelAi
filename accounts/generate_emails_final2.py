import openai
import json


def generate_sales_email(data):
    #print(data.keys())
    openai.api_key  = ''

    sales_rep_name = data["sales_rep_name"]
    sales_rep_email = data["sales_rep_email"]
    sales_rep_Contact_Number = data["sales_rep_Contact_Number"]

    sales_rep_company_name = data["sales_rep_company_name"]
    sales_rep_company_industry = data["sales_rep_company_Industry"]
    sales_rep_company_specialties = data["sales_rep_company_Specialties"]
    sales_rep_company_overview = data["sales_rep_company_Overview"]
    sales_rep_company_Website = data["sales_rep_company_Website"]


    prospect_company_name = data["Prospect_Company_name"]
    prospect_company_industry = data["Prospect_Company_Industry"]
    prospect_company_overview = data["Prospect_Company_Overview"]
    prospect_company_specialties = data["Prospect_Company_specialties"]


    focus_area = data["focus_area"]
    intent = data["Intent"]
    prospect_title_list = data["Prospect_Title_list"]
    financial_raw_data = data.get("Financial_Report", None)
    grants_raw_data = data.get("Grant", None)


    if prospect_company_specialties:
        first_line = f"You are {sales_rep_name}, a sales representative for {sales_rep_company_name} and your email address is {sales_rep_email} and your phone number is {sales_rep_Contact_Number}. {sales_rep_company_name} is categories in {sales_rep_company_industry} industry having specialization in {sales_rep_company_specialties}. A brief overview of {sales_rep_company_name} is ({sales_rep_company_overview}) and there website is {sales_rep_company_Website}. You are targeting {prospect_company_name} which lies in {prospect_company_industry} industry having specialization in {prospect_company_specialties}. A brief overview of {prospect_company_name} is ({prospect_company_overview})."
    else:
        first_line = f"You are {sales_rep_name}, a sales representative for {sales_rep_company_name} and your email address is {sales_rep_email} and your phone number is {sales_rep_Contact_Number}. {sales_rep_company_name} is categories in {sales_rep_company_industry} industry having specialization in {sales_rep_company_specialties}. A brief overview of {sales_rep_company_name} is ({sales_rep_company_overview}) and there website is {sales_rep_company_Website}. You are targeting {prospect_company_name} which lies in {prospect_company_industry} industry. A brief overview of {prospect_company_name} is ({prospect_company_overview})."

    generated_emails_dict = {}
    results = []

    for i, Prospect_Title in enumerate(prospect_title_list):
        if financial_raw_data and grants_raw_data:
            tokens = 550
            prompt = f"""
            {first_line} The financial report of {prospect_company_name} for current year is this: {financial_raw_data}.

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {intent}. The whole email must not cross 350 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {prospect_company_name}, before introducing yourself. Use 20% of words here.

            Second paragraph:
            Suggest {prospect_company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use 30% of words here.

            Third paragraph:
            Use that financial report data and facts for {prospect_company_name} to show how your company can help them. Use numbers from data to proof your point. Try to be on point and attractive with your suggestions. Also mention that we may apply for this grant ({grants_raw_data}). Use 40% of words here.

            Fourth paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use 10% of words here.

            """

        elif financial_raw_data:
            tokens = 500
            prompt = f"""
            {first_line} The financial report of {prospect_company_name} for current year is this: {financial_raw_data}.

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {intent}. The whole email must not cross 330 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {prospect_company_name}, before introducing yourself. Use 20% of words here.

            Second paragraph:
            Suggest {prospect_company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use 30% of words here.

            Third paragraph:
            Use that financial report data and facts for {prospect_company_name} to show how your company can help them. Use numbers from data to proof your point. Try to be on point and attractive with your suggestions. Use 40% of words here.

            Fourth paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use 10% of words here.

            """

        elif grants_raw_data:
            tokens = 365
            prompt = f"""
            {first_line}

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {intent}. The whole email must not cross 200 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {prospect_company_name}, before introducing yourself. Use upto 65 words here.

            Second paragraph:
            Suggest {prospect_company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use upto 65 words here.

            Third paragraph:
            Mention that we may apply for this grant ({grants_raw_data}). Use upto 25 words here.

            Fourth paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use upto 20 words here.

            """

        else:
            tokens = 340
            prompt = f"""
            {first_line}

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {intent}. The whole email must not cross 190 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {prospect_company_name}, before introducing yourself. Use upto 85 words here.

            Second paragraph:
            Suggest {prospect_company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use upto 85 words here.

            Third paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use upto 30 words here.

            """
        # Generate the response using OpenAI's GPT-3.5 model
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=tokens  # Adjust the desired length of the generated text
        )


        generated_emails_dict = {
            "title": Prospect_Title,
            "Subject": response.choices[0].message.content.split("\n")[0],  # Extract the first line as the subject
            "Body": "\n".join(response.choices[0].message.content.split("\n")[1:]).strip("\n")  # Store the entire email body
        }
        results.append(generated_emails_dict)
        # generated_emails_dict =generated_emails_dict
    if results:
        final_data = {"message": "Success", "status_code": 200, "results": results}
        # final_data
    # return generated_emails_dict
    return final_data

# Load data from JSON file
# with open('dummy_data.json') as json_file:
#     data = json.load(json_file)

# # Generate emails and store in a dictionary
# generated_emails = generate_sales_email(data)
# print(generated_emails)
