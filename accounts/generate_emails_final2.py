import openai
import json


def generate_sales_email(data):
    # openai.api_key = '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'
    # openai.api_key = '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'
    openai.api_key = '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'
    
    
    sales_rep_name = data["sales_rep_name"]
    sales_rep_email = data["sales_rep_email"]
    sales_rep_company_name = data["sales_rep_company_name"]
    sales_rep_company_Industry = data["sales_rep_company_Industry"]
    sales_rep_company_Specialties = data["sales_rep_company_Specialties"]
    sales_rep_company_Overview = data["sales_rep_company_Overview"]
    Prospect_Title_list = data["Prospect_Title_list"]
    Prospect_Company_name = data["Prospect_Company_name"]
    Prospect_Company_Industry = data["Prospect_Company_Industry"]
    Prospect_Company_Overview = data["Prospect_Company_Overview"]
    Prospect_Company_specialties = data["Prospect_Company_specialties"]
    Intent = data["Intent"]
    focus_area = data["focus_area"]
    Financial_Report = data.get("Financial_Report", None)
    Grant = data.get("Grant", None)
    print(focus_area)
    generated_emails_dict = {}
    results = []

    if Prospect_Company_specialties:
        first_line = f"You are {sales_rep_name}, a sales representative for {sales_rep_company_name} and your email address is {sales_rep_email}. {sales_rep_company_name} is categories in {sales_rep_company_Industry} industry having specialization in {sales_rep_company_Specialties}. A brief overview of {sales_rep_company_name} on there website is ({sales_rep_company_Overview}). You are targeting {Prospect_Company_name} which lies in {Prospect_Company_Industry} industry having specialization in {Prospect_Company_specialties}. A brief overview of {Prospect_Company_name} on there website is {Prospect_Company_Overview}."
    else:
        first_line = f"You are {sales_rep_name}, a sales representative for {sales_rep_company_name} and your email address is {sales_rep_email}. {sales_rep_company_name} is categories in {sales_rep_company_Industry} industry having specialization in {sales_rep_company_Specialties}. A brief overview of {sales_rep_company_name} on there website is ({sales_rep_company_Overview}). You are targeting {Prospect_Company_name} which lies in {Prospect_Company_Industry} industry. A brief overview of {Prospect_Company_name} on there website is {Prospect_Company_Overview}."

    generated_emails_dict = {}

    for i, Prospect_Title in enumerate(data["Prospect_Title_list"]):
        if Financial_Report and Grant:
            prompt = f"""
            {first_line} The financial report of {Prospect_Company_name} for current year is this: {Financial_Report}.

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {Intent}. The whole email must not cross 350 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {Prospect_Company_name}, before introducing yourself. Use 20% of words here.

            Second paragraph:
            Suggest {Prospect_Company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use 30% of words here.

            Third paragraph:
            Use that financial report data and facts for {Prospect_Company_name} to show how your company can help them. Use numbers from data to proof your point. Try to be on point and attractive with your suggestions. Also mention that we may apply for this grant ({Grant}). Use 40% of words here.

            Fourth paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use 10% of words here.

            """
        elif Financial_Report:
            prompt = f"""
            {first_line} The financial report of {Prospect_Company_name} for current year is this: {Financial_Report}.

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {Intent}. The whole email must not cross 350 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {Prospect_Company_name}, before introducing yourself. Use 20% of words here.

            Second paragraph:
            Suggest {Prospect_Company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use 30% of words here.

            Third paragraph:
            Use that financial report data and facts for {Prospect_Company_name} to show how your company can help them. Use numbers from data to proof your point. Try to be on point and attractive with your suggestions. Use 40% of words here.

            Fourth paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use 10% of words here.

            """

        elif Grant:
            prompt = f"""
            {first_line}

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {Intent}. The whole email must not cross 250 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {Prospect_Company_name}, before introducing yourself. Use 40% of words here.

            Second paragraph:
            Suggest {Prospect_Company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use 40% of words here.

            Third paragraph:
            Mention that we may apply for this grant ({Grant}). Use 10% of words here.

            Fourth paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use 10% of words here.

            """

        else:
            prompt = f"""
            {first_line}

            Keeping in mind your and targeting company information, compose a detailed email with attractive subject suggesting how your company can benefit them and have more profits. Writing context should be according to {Prospect_Title} and writing style must be {Intent}. The whole email must not cross 250 words in total. You must follow below instructions to structure the emails:

            First paragraph:
            Target {Prospect_Title} by saying dear {Prospect_Title}. Must start the email writing with telling {Prospect_Title} that how can {sales_rep_company_name} be benificial
            for {Prospect_Company_name}, before introducing yourself. Use 40% of words here.

            Second paragraph:
            Suggest {Prospect_Company_name} how there {focus_area} can be improved after collaborating with {sales_rep_company_name}. Use 45% of words here.

            Third paragraph:
            Give closing remarks and suggest a meeting or further discussion. Use 15% of words here.

            """

        # Generate the response using OpenAI's GPT-3.5 model
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700  # Adjust the desired length of the generated text
        )
        # Store the generated email in the dictionary
      # Store the generated email in the dictionary
        # generated_emails_dict[Prospect_Title] = {
        #     "Subject": response.choices[0].text.split("\n", 2)[1],  # Extract the first line as the subject
        #     "Body": response.choices[0].text.split("\n", 2)[2]  # Store the entire email body
        # }
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
