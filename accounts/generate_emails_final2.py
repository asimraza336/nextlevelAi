import openai
import json
            # - Founded: {data["sales_rep_company_Founded"]}
            # - Founded: {data["sales_rep_company_Founded"]}

            # - Founded: {data["sales_rep_company_Founded"]}

def generate_sales_email(data):
    # openai.api_key = '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'
    # openai.api_key = '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'
    # openai.api_key = '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'
    # openai.api_key = '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'
    # openai.api_key = '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'
    openai.api_key = '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'
    
    
    
    
    
    
    

    sales_rep_company_name = data["sales_rep_company_name"]
    sales_rep_company_Industry = data["sales_rep_company_Industry"]
    sales_rep_company_Specialties = data["sales_rep_company_Specialties"]
    sales_rep_company_Overview = data["sales_rep_company_Overview"]
    Prospect_Title_list = data["Prospect_Title_list"]
    Prospect_Company_name = data["Prospect_Company_name"]
    Prospect_Company_Industry = data["Prospect_Company_Industry"]
    Prospect_Company_Overview = data["Prospect_Company_Overview"]
    Intent = data["Intent"]
    focus_area = data["focus_area"]
    Financial_Report = data.get("Financial_Report", None)
    Grant = data.get("Grant", None)

    generated_emails_dict = {}
    results = []
    
    for i, Prospect_Title in enumerate(data["Prospect_Title_list"]):
        if Financial_Report and Grant:
            prompt = f"""
            You are a sales representative for {sales_rep_company_name}, a leading provider of innovative solutions in the {sales_rep_company_Industry}. Your company
            specializes in {sales_rep_company_Specialties}. Overview of the company is that {sales_rep_company_Overview}.

            The Prospect is {Prospect_Title} at {Prospect_Company_name}. The company is in the industry of {Prospect_Company_Industry}.
            This is an overview of the Prospect's company {Prospect_Company_name} {Prospect_Company_Overview}.

            Compose a detailed email for {Prospect_Title} by saying dear {Prospect_Title} of up to 450 words (complete) as you introduce your company to the {Prospect_Title} of {Prospect_Company_name}, 
            highlighting your Specialties {sales_rep_company_Specialties} and suggesting a meeting or further discussion. Tone should be according to {Prospect_Title} and intent must be {Intent}.

            Use all the provided information to add details in the email and must generate an attractive subject of email, also focus on {focus_area} in the email.
            we are also providing financial report of {Prospect_Company_name} ({Financial_Report}), you analyse all the liabilities,aspects and financial state of {Prospect_Company_name}. Use its aspects in email.
            also mention this grant ({Grant}) in email.
            Information provided:
            Sales Representative:
            - Name: {data["sales_rep_name"]}
            - Company: {sales_rep_company_name}
            - Contact Number: {data["sales_rep_Contact_Number"]}
            - Email: {data["sales_rep_email"]}

            Sales Representative Company:
            - Overview: {sales_rep_company_Overview}
            - Website: {data["sales_rep_company_Website"]}
            - Industry: {sales_rep_company_Industry}
            - Headquarters: {data["sales_rep_company_Headquarters"]}
            - Specialties: {sales_rep_company_Specialties}

            Prospect:
            - Prospect Title: {Prospect_Title}

            Prospect Company:
            - Company Name: {Prospect_Company_name}
            - Overview: {Prospect_Company_Overview}
            - Industry: {Prospect_Company_Industry}
            - Headquarters: {data["Prospect_Company_Headquarters"]}
            - Company Size: {data["Prospect_Company_Size"]}
            - Founded Year: {data["Prospect_Company_founded"]}
            - Specialities: {data["Prospect_Company_specialties"]}

            """
        elif Financial_Report:
            prompt = f"""
            You are a sales representative for {sales_rep_company_name}, a leading provider of innovative solutions in the {sales_rep_company_Industry}. Your company
            specializes in {sales_rep_company_Specialties}. Overview of the company is that {sales_rep_company_Overview}.

            The Prospect is {Prospect_Title} at {Prospect_Company_name}. The company is in the industry of {Prospect_Company_Industry}.
            This is an overview of the Prospect's company {Prospect_Company_name} {Prospect_Company_Overview}.

            Compose a detailed email for {Prospect_Title} by saying dear {Prospect_Title} of up to 350 words (complete) as you introduce your company to the {Prospect_Title} of {Prospect_Company_name}, 
            highlighting your Specialties {sales_rep_company_Specialties} and suggesting a meeting or further discussion. Tone should be according to {Prospect_Title} and intent must be {Intent}.

            Use all the provided information to add details in the email and must generate an attractive subject of email, also focus on {focus_area} in the email.
            we are also providing financial report of {Prospect_Company_name} ({Financial_Report}), you analyse all the liabilities,aspects and financial state of {Prospect_Company_name}. Use its aspects in email.
            Information provided:
            Sales Representative:
            - Name: {data["sales_rep_name"]}
            - Company: {sales_rep_company_name}
            - Contact Number: {data["sales_rep_Contact_Number"]}
            - Email: {data["sales_rep_email"]}

            Sales Representative Company:
            - Overview: {sales_rep_company_Overview}
            - Website: {data["sales_rep_company_Website"]}
            - Industry: {sales_rep_company_Industry}
            - Headquarters: {data["sales_rep_company_Headquarters"]}
            - Specialties: {sales_rep_company_Specialties}

            Prospect:
            - Prospect Title: {Prospect_Title}

            Prospect Company:
            - Company Name: {Prospect_Company_name}
            - Overview: {Prospect_Company_Overview}
            - Industry: {Prospect_Company_Industry}
            - Headquarters: {data["Prospect_Company_Headquarters"]}
            - Company Size: {data["Prospect_Company_Size"]}
            - Founded Year: {data["Prospect_Company_founded"]}
            - Specialities: {data["Prospect_Company_specialties"]}

            """
        else:
            prompt = f"""
            You are a sales representative for {sales_rep_company_name}, a leading provider of innovative solutions in the {sales_rep_company_Industry}. Your company
            specializes in {sales_rep_company_Specialties}. Overview of the company is that {sales_rep_company_Overview}.

            The Prospect is {Prospect_Title} at {Prospect_Company_name}. The company is in the industry of {Prospect_Company_Industry}.
            This is an overview of the Prospect's company {Prospect_Company_name} {Prospect_Company_Overview}.

            Compose a detailed email for {Prospect_Title} by saying dear {Prospect_Title} of up to 350 words (complete) as you introduce your company to the {Prospect_Title} of {Prospect_Company_name}, 
            highlighting your Specialties {sales_rep_company_Specialties} and suggesting a meeting or further discussion. Tone should be according to {Prospect_Title} and intent must be {Intent}.

            Use all the provided information to add details in the email and must generate an attractive subject of email, also focus on {focus_area} in the email.
            Information provided:
            Sales Representative:
            - Name: {data["sales_rep_name"]}
            - Company: {sales_rep_company_name}
            - Contact Number: {data["sales_rep_Contact_Number"]}
            - Email: {data["sales_rep_email"]}

            Sales Representative Company:
            - Overview: {sales_rep_company_Overview}
            - Website: {data["sales_rep_company_Website"]}
            - Industry: {sales_rep_company_Industry}
            - Headquarters: {data["sales_rep_company_Headquarters"]}
            - Specialties: {sales_rep_company_Specialties}

            Prospect:
            - Prospect Title: {Prospect_Title}

            Prospect Company:
            - Company Name: {Prospect_Company_name}
            - Overview: {Prospect_Company_Overview}
            - Industry: {Prospect_Company_Industry}
            - Headquarters: {data["Prospect_Company_Headquarters"]}
            - Company Size: {data["Prospect_Company_Size"]}
            - Founded Year: {data["Prospect_Company_founded"]}
            - Specialities: {data["Prospect_Company_specialties"]}

            """
        # Generate the response using OpenAI's GPT-3.5 model
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.7,
            max_tokens=1000  # Adjust the desired length of the generated text
        )
        # Store the generated email in the dictionary
      # Store the generated email in the dictionary
        # generated_emails_dict[Prospect_Title] = {
        #     "Subject": response.choices[0].text.split("\n", 2)[1],  # Extract the first line as the subject
        #     "Body": response.choices[0].text.split("\n", 2)[2]  # Store the entire email body
        # }
        generated_emails_dict = {
            "title": Prospect_Title,
            "Subject": response.choices[0].text.split("\n", 2)[1],  # Extract the first line as the subject
            "Body": response.choices[0].text.split("\n", 2)[2]  # Store the entire email body
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
