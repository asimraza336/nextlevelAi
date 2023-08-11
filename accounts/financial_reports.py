import openai
import json
# from config import *
# API = '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'
# API = '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'
API = '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'



openai.api_key = API

#FINANCIAL_INSIGHTS_PROMPT = "Providing you with sales representative company inofrmation. Name of the company is {} and company work in industry of {} and company head Headquarters are located at {} with Specialties in {}. Sales representative company overview is as following {}. Now I am gonna provide you Prospect company information.Name of the prospect company is {} and company work in industry of {} and company head Headquarters are located at {} with Specialties in {} with company size of {} founded in {}. prospect company overview is as following {}. The Financial data of the prospect company is {}.Show how {} can offset their debt to liabilities of {}. showcase how {} can enhance {} customer experience, CSAT, ERG sustainability score, and show how {} can enhance the workforce of {} using {} Specialties. Make sure to use facts and numbers. Also consider the following points {}"

FINANCIAL_INSIGHTS_PROMPT = '''{} is an industry of {} with following specialities {}.
there is prospect company named {} and is industry of {}.
The balance sheet of {} is given below .
Balance Sheet:
{}

By analysing balance sheet, elaborate how can {} be beneficial for {} in upto 300 words, Must add refrences and digital amounts in dollers from given balance sheet. Make a statement on {}.

'''


GRANTS_PROMPT = '''Taking into cosideration the sales representative (SR) company information
SR comapny Name as {}
company Overview as {}
company Industry as {}
company Headquarters as {}
company Specialties as {}

and prospect company information

Prospect Company name as {}
Prospect Company Overview as {}
Prospect Company Industry as {}
Prospect Company Headquarters as {}
Prospect Company Size as {}
Prospect Company founded as {}
Prospect Company specialties as {}

Taking into consideration how sales representaive company can enhance the propespect company bussiness. Look from the following grants that can help in the colaboration between sales representative company and Prospect company. {}


'''

FINANCIAL_INSIGHTS_MAX_TOKEN = 500
FINANCIAL_INSIGHTS_TEMPERATURE = 0.7
MODEL = "gpt-3.5-turbo"

def generate_financial_insights(data):
    '''
    takes in a json data and uses that to generate a financial insights using chatgpt
    params:
    data: json
    	schema: {
    		"sales_rep_name": string,
    		"sales_rep_company_name": string,
    		"sales_rep_contact_number": string,
    		"sales_rep_email": string,
    		"sales_rep_company_overview": string,
    		"sales_rep_company_website": string,
    		"sales_rep_company_industry": string,
    		"sales_rep_company_headquarters": string,
   		    "sales_rep_company_specialties": string,
    		"prospect_company_name": string,
    		"prospect_company_overview": string,
    		"prospect_company_industry": string,
    		"prospect_company_headquarters":string,
    		"prospect_company_size": string,
    		"prospect_company_founded": string,
    		"prospect_company_specialties": string,
    		"focus_area":string,
		"financial_raw_data":string,
   		}
    return:
    output: json
    	schema: {"insights":string}

    '''

    try:
        # sales_rep_name = data["sales_rep_name"]
        sales_rep_company_name = data["sales_rep_company_name"]
        # sales_rep_contact_number = data["sales_rep_contact_number"]
        # sales_rep_email = data["sales_rep_email"]
        sales_rep_company_overview = data["sales_rep_company_overview"]
        # sales_rep_company_website = data["sales_rep_company_website"]
        sales_rep_company_industry = data["sales_rep_company_industry"]
        sales_rep_company_headquarters = data["sales_rep_company_headquarters"]
        sales_rep_company_specialties = data["sales_rep_company_specialties"]

        prospect_company_name = data["prospect_company_name"]
        prospect_company_overview = data["prospect_company_overview"]
        prospect_company_industry = data["prospect_company_industry"]
        prospect_company_headquarters = data["prospect_company_headquarters"]
        prospect_company_size = data["prospect_company_size"]
        prospect_company_founded = data["prospect_company_founded"]
        prospect_company_specialties = data.get("prospect_company_specialties", None)
        # data["prospect_company_specialties"]
        focus_area = data["focus_area"]
        financial_raw_data = data["financial_raw_data"]
    except Exception as e:
        return e

    # PROMPT = FINANCIAL_INSIGHTS_PROMPT.format(
    #             sales_rep_company_name,
    #             sales_rep_company_industry,
    #             sales_rep_company_headquarters,
    #             sales_rep_company_specialties,
    #             sales_rep_company_overview,
    #             prospect_company_name,
    #             prospect_company_industry,
    #             prospect_company_headquarters,
    #             prospect_company_specialties,
    #             prospect_company_size,
    #             prospect_company_founded,
    #             prospect_company_overview,
    #             financial_raw_data,
    #             sales_rep_company_name,
    #             prospect_company_name,
    #             sales_rep_company_name,
    #             prospect_company_name,
    #             sales_rep_company_name,
    #             prospect_company_name,
    #             sales_rep_company_name,
    #             focus_area
    #             )

    PROMPT = FINANCIAL_INSIGHTS_PROMPT.format(
                sales_rep_company_name,
                sales_rep_company_industry,
                sales_rep_company_specialties,
                prospect_company_name,
                prospect_company_industry,
                prospect_company_name,
                financial_raw_data,
                sales_rep_company_name,
                prospect_company_name,
                focus_area,
                )
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": PROMPT}
            ],
            temperature=FINANCIAL_INSIGHTS_TEMPERATURE,
            max_tokens=FINANCIAL_INSIGHTS_MAX_TOKEN  # Adjust the desired length of the generated text
        )

        # response = {'insights': 'Dom can help Arthrex offset their debt to liabilities by providing a range of services and products. Dom can help Arthrex improve their customer experience by providing data-driven insights into customer behaviour and preferences, which can be used to create tailored customer experiences. Dom can also help Arthrex improve their CSAT (Customer Satisfaction) score by providing the right tools and resources to monitor customer feedback and resolve issues quickly. Dom can also help Arthrex enhance their ERG (Environmental, Social and Governance) sustainability score by providing strategies and tools to reduce their carbon footprint and improve their ESG policies. Finally, Dom can help Arthrex enhance their workforce by providing the right training, resources, and technologies to ensure their employees are well equipped to perform their roles and tasks.', 'message': 'Success'}
        insights = response.choices[0].message.content.strip("\n")
        output = {"insights":insights, "message": "Success"}
        return output
    except Exception as e:
        return e


def generate_grants(data):
    '''
    takes in a json data and uses that to extract what grants work best
    params:
    data: json
    	schema: {
    		"sales_rep_company_name": string,
    		"sales_rep_company_overview": string,
    		"sales_rep_company_industry": string,
    		"sales_rep_company_headquarters": string,
   		    "sales_rep_company_specialties": string,
    		"prospect_company_name": string,
    		"prospect_company_overview": string,
    		"prospect_company_industry": string,
    		"prospect_company_headquarters":string,
    		"prospect_company_size": string,
    		"prospect_company_founded": string,
    		"prospect_company_specialties": string,
		    "grants_raw_data":string,
   		}
    return:
    output: json
    	schema: {"grant":string, "title":string}

    '''

    try:
        sales_rep_company_name = data["sales_rep_company_name"]
        sales_rep_company_overview = data["sales_rep_company_overview"]
        sales_rep_company_industry = data["sales_rep_company_industry"]
        sales_rep_company_headquarters = data["sales_rep_company_headquarters"]
        sales_rep_company_specialties = data["sales_rep_company_specialties"]
        prospect_company_name = data["prospect_company_name"]
        prospect_company_overview = data["prospect_company_overview"]
        prospect_company_industry = data["prospect_company_industry"]
        prospect_company_headquarters = data["prospect_company_headquarters"]
        prospect_company_size = data["prospect_company_size"]
        prospect_company_founded = data["prospect_company_founded"]
        prospect_company_specialties = data["prospect_company_specialties"]
        grants_raw_data = data["grants_raw_data"]
    except Exception as e:
        return e

    PROMPT = GRANTS_PROMPT.format(
             sales_rep_company_name,
             sales_rep_company_overview,
             sales_rep_company_industry,
             sales_rep_company_headquarters,
             sales_rep_company_specialties,
             prospect_company_name,
             prospect_company_overview,
             prospect_company_industry,
             prospect_company_headquarters,
             prospect_company_size,
             prospect_company_founded,
             prospect_company_specialties,
             grants_raw_data)

    output = '''
The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":
```json
{
	"grants": string  // a list of dictionaries where each dictionary consists of opportunity_title and opportunity_grant_number . should be a empty list if no grants found.
}
```
'''
    PROMPT = PROMPT+output
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": PROMPT}
            ],
            temperature=FINANCIAL_INSIGHTS_TEMPERATURE,
            max_tokens=1000  # Adjust the desired length of the generated text
        )
        output_dt = (response.choices[0].message.content)
        res = ''.join(output_dt.split("```json")[1].split("```")[0])
        res = json.loads(res)

        new_list = []
        for x in res["grants"]:
            new_dict = {}
            new_dict["title"] = x["opportunity_grant_number"]
            new_dict["grant"] = x["opportunity_title"]
            new_list.append(new_dict)
        print(new_list)
        return new_list
    except Exception as e:
        print(e)
        return []




