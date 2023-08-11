from langchain.output_parsers import StructuredOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import openai
import os
import json
# from config import *
# API = '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'
# API = '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'


os.environ['OPENAI_API_KEY'] = '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'

def generate_financial_insights(data):

    try:
        # sales_rep_name = data["sales_rep_name"]
        sales_rep_company_name = data["sales_rep_company_name"]
        # sales_rep_contact_number = data["sales_rep_contact_number"]
        # sales_rep_email = data["sales_rep_email"]
        #sales_rep_company_overview = data["sales_rep_company_overview"]
        # sales_rep_company_website = data["sales_rep_company_website"]
        sales_rep_company_industry = data["sales_rep_company_industry"]
        #sales_rep_company_headquarters = data["sales_rep_company_headquarters"]
        sales_rep_company_specialties = data["sales_rep_company_specialties"]

        prospect_company_name = data["prospect_company_name"]
        #prospect_company_overview = data["prospect_company_overview"]
        prospect_company_industry = data["prospect_company_industry"]
        #prospect_company_headquarters = data["prospect_company_headquarters"]
        #prospect_company_size = data["prospect_company_size"]
        #prospect_company_founded = data["prospect_company_founded"]
        #prospect_company_specialties = data.get("prospect_company_specialties", None)
        # data["prospect_company_specialties"]
        focus_areas = data["focus_area"]
        financial_raw_data = data["financial_raw_data"]
    except Exception as e:
        return e

    chat_insights = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    # setting up the output parser
    insights_schema = ResponseSchema(name="insights",
                                description="analyze the balance sheet of a prospect company and explain how your company can be beneficial for them,\
                                use digital amounts from balance sheet in answer as refrences,\
                                Answer in a form of string,\
                                empty dictionary if no data found")

    response_schemas = [insights_schema]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    insights_template = """You are an AI sales representative assistant. Your task is to analyze the balance sheet of a prospect company and explain how your company can be beneficial for them. also include references and digital amounts in dollars from balance sheet.
        {sales_rep_company_name} is an industry of {sales_rep_company_industry} with the following specialties {sales_rep_company_specialties}. There is a prospect company named {prospect_company_name} in the industry of {prospect_company_industry}. The balance sheet of {prospect_company_name} is given below. By analyzing the balance sheet, elaborate on how can {sales_rep_company_name} be beneficial for {prospect_company_name} in up to 250 words. And also make a statement on {focus_areas} and use digital amounts from balance sheet in answer as refrences.
        balance sheet: ```{financial_raw_data}```
        {format_instructions}
        """
    prompt_template = ChatPromptTemplate.from_template(insights_template)
    customer_messages = prompt_template.format_messages(
                    sales_rep_company_name=sales_rep_company_name,
                    sales_rep_company_industry=sales_rep_company_industry,
                    sales_rep_company_specialties=sales_rep_company_specialties,
                    prospect_company_name=prospect_company_name,
                    prospect_company_industry=prospect_company_industry,
                    focus_areas=focus_areas,
                    financial_raw_data=financial_raw_data,
                    format_instructions=format_instructions)
    response = chat_insights(customer_messages)
    try:
        output_dict = output_parser.parse(response.content)
        output_dict["message"] = "Success"
        return output_dict
    except Exception as e:
        return {"insights":"","message":"Fail"}


def generate_grants(data):
    sales_rep_company_name = data["sales_rep_company_name"]
    sales_rep_company_industry = data["sales_rep_company_industry"]
    sales_rep_company_specialties = data["sales_rep_company_specialties"]
    prospect_company_name = data["prospect_company_name"]
    prospect_company_industry = data["prospect_company_industry"]
    grants_raw_data = data.get("grants_raw_data", None)
    chat_insights = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    # setting up the output parser
    grants_schema = ResponseSchema(name="grants",
                                description="analyze the raw data of grants and extract grants which are relevant to both companies,\
                                show OPPORTUNITY NUMBER and OPPORTUNITY TITLE of upto 5 relevent grants,\
                                Answer in a form of list of dictionaries where each dictionary has OPPORTUNITY NUMBER and OPPORTUNITY TITLE ,\
                                empty dictionary if no relevant grant found")

    grants_response_schemas = [grants_schema]
    grants_output_parser = StructuredOutputParser.from_response_schemas(grants_response_schemas)
    grants_format_instructions = grants_output_parser.get_format_instructions()
    # setting up the prompt
    insights_template = """You are a language model tasked with finding relevant grants from a data. The data contains information about various grants,
their OPPORTUNITY NUMBER and OPPORTUNITY TITLE. Your goal is to filter and identify grants that are related to {sales_rep_company_industry}
and {prospect_company_industry}. Please use the provided data and your knowledge of these industries to suggest the most suitable grants for
further consideration.
raw data: ```{raw_data}```
{format_instructions}
"""
    prompt_template = ChatPromptTemplate.from_template(insights_template)
    customer_messages = prompt_template.format_messages(
                    sales_rep_company_industry=sales_rep_company_industry,
                    prospect_company_industry=prospect_company_industry,
                    raw_data=grants_raw_data,
                    format_instructions=grants_format_instructions)
    response = chat_insights(customer_messages)
    grants_output_dict = grants_output_parser.parse(response.content)
	
    new_list = []
    try:
        for x in grants_output_dict["grants"]:
            new_dict = {}
            new_dict["title"] = x["OPPORTUNITY NUMBER"]
            new_dict["grant"] = x["OPPORTUNITY TITLE"]
            new_list.append(new_dict)
        return new_list
    except Exception as e:
        return []




