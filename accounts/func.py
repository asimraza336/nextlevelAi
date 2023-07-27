import requests
import json

def get_linkedin_company_info(linkedin_url):
    url = "https://linkedin-company-data.p.rapidapi.com/linkedInCompanyDataJson"
    
    payload = {"liUrls": [linkedin_url]}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "fc8b0b9406msh7dbbe0dba4a12d6p17b93ejsne5ef74022b9a",
        "X-RapidAPI-Host": "linkedin-company-data.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    # with open('/content/uchealth_data_RapidAPI.json') as json_file:
    #   data = json.load(json_file)

    json_data = json.dumps(data)
    # print(json_data)
    with open("arthrex_data_companiesAPI.json", "w") as file:
        file.write(json_data)
    message = data['message']
    try:
      status_code = data['status_code']
    except:
      status_code = ''
    if 'results' in data and len(data['results']) > 0:
        company_data = data['results'][0]
        
        company_info = {
            'Prospect_Company_logo': company_data.get('logo', ''),
            'Prospect_Company_name': company_data.get('company_name', ''),
            'Prospect_Company_Overview': company_data.get('description', ''),
            'Prospect_Company_Industry': company_data.get('industries', ''),
            'Prospect_Company_HQ': f"{company_data['headquarters']['address'].get('street', '')}, {company_data['headquarters']['address'].get('city', '')}, {company_data['headquarters']['address'].get('state', '')} {company_data['headquarters']['address'].get('country', '')}",
            'Prospect_Company_Size': company_data.get('company_size', ''),
            'Prospect_Company_specialties': company_data.get('specialties', ''),
            'Prospect_Company_founded': company_data.get('founded', '')
        }
    else:
      company_info = {}
    my_dict = {
      "message": message,
      "status_code": status_code,
      "results": [company_info]
    }
    return my_dict


# Example usage:
# linkedin_url = "https://www.linkedin.com/company/arthrex"
# linkedin_url = "https://www.linked.com/company/arthrex"

# company_info_final = get_linkedin_company_info(linkedin_url)
# print(company_info_final)
