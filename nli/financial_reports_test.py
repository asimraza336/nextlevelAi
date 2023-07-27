from financial_reports import *

def test_generate_financial_insights():
    '''
    sample data and test case to check generate_financial_insights function
    '''
    assert True == True
    json_data = {
        "sales_rep_name": "John Smith",
        "sales_rep_company_name": "ABC Sales Inc.",
        "sales_rep_contact_number": "123-456-7890",
        "sales_rep_email": "john.smith@abc.com",
        "sales_rep_company_overview": "ABC Sales Inc. is a leading company in the sales industry.",
        "sales_rep_company_website": "www.abcsales.com",
        "sales_rep_company_industry": "Sales and Marketing",
        "sales_rep_company_headquarters": "New York, USA",
        "sales_rep_company_specialties": "Sales, Marketing, Business Development",
        "prospect_company_name": "XYZ Corporation",
        "prospect_company_overview": "XYZ Corporation is a global leader in manufacturing.",
        "prospect_company_industry": "Manufacturing",
        "prospect_company_headquarters": "Los Angeles, USA",
        "prospect_company_size": "1,001-5,000 employees",
        "prospect_company_founded": "1980",
        "prospect_company_specialties": "Product Development, Quality Assurance",
        
        "focus_area": "Show how T-Mobile for Business can offset their debt to liabilities. showcase how T-Mobile for Business can enhance their customer experience, CSAT, ERG sustainability score, and show how we can enhance the workforce using T-Mobile for Business Solutions.Also show case how T-Mobile for Business can enhance UC Health using IOT, and drive rural Healthcare initiatives.",
        
    "financial_raw_data":"Balance Sheet Period ending date	12/31/2021	12/31/2020	12/31/2019	12/31/2018	12/31/2017 Number of months in period	12	12	12	12	12 Cost report status	As Submitted	Reopened	As Submitted	Reopened	Reopened Assets	 	 	 	 	  Current Assets	$335,302,065	$283,899,480	$284,438,409	$268,217,357	$278,774,000 Fixed Assets	$950,056,514	$910,012,799	$836,368,294	$750,527,376	$673,568,489 Other Assets	$2,180,470,432	$1,997,670,063	$1,654,542,900	$1,532,263,018	$1,319,727,628 Total Assets	$3,465,829,011	$3,191,582,342	$2,775,349,603	$2,551,007,751	$2,272,070,117 Liabilities and Fund Balancec ... ",
    
    }

    data = generate_financial_insights(json_data)
    assert type(data["insights"]) == str
    
    
    
def test_generate_grants():
    '''
    sample data and test case to check generate_financial_insights function
    '''
    json_data = {
        "sales_rep_company_name": "ABC Sales Inc.",
        "sales_rep_company_overview": "ABC Sales Inc. is a leading company in the sales industry.",
        "sales_rep_company_industry": "Sales and Marketing",
        "sales_rep_company_headquarters": "New York, USA",
        "sales_rep_company_specialties": "Sales, Marketing, Business Development",
        "prospect_company_name": "XYZ Corporation",
        "prospect_company_overview": "XYZ Corporation is a global leader in manufacturing.",
        "prospect_company_industry": "Manufacturing",
        "prospect_company_headquarters": "Los Angeles, USA",
        "prospect_company_size": "1,001-5,000 employees",
        "prospect_company_founded": "1980",
        "prospect_company_specialties": "Product Development, Quality Assurance",
        "grants_raw_data":"FR-RRD-23-004	FY23 Short Line Safety Institute Program	DOT-FRA	Posted	07/21/2023	08/04/2023 TASHKENT-PDS-FY23-004	Grant Proposal Development and Writing Workshops	DOS-UZB	Posted	07/21/2023	08/28/2023 EPA-I-R3-CBP-23-11	Chesapeake Bay Program Office Fiscal Year 2023 Request for Applications for: Assessment and Methodology Development for Advanced Automated Techniques and Protocols to Map Chesapeake Bay Submerged Aquatic Vegetation from HighResolution Satellite Imagery	EPA	Posted	07/21/2023	09/06/2023 PSG-MBA-FY23-01	Community-Led Monitoring (CLM)	DOS-SWZ	Posted	07/21/2023	08/21/2023 PDS-COL-2023-YLS	Youth Forum Leadership Summit 2024	DOS-LKA	Posted	07/21/2023	08/20/2023 PDS-COL-2023-MED	Media Capacity Building	DOS-LKA	Posted	07/21/2023	08/20/2023 72051723RFA00004	Basic Education Recovery Activity	USAID-DOM	Posted	07/21/2023	09/06/2023 72061523RFA00008	Kenya Feed the Future Local Food Systems	USAID	Posted	07/21/2023	08/21/2023 DHS-23-NPD-007-00-99	Fiscal Year 2023 Homeland Security Preparedness Technical Assistance Program (HSPTAP)	DHS-DHS	Posted	07/21/2023	08/21/2023 W911KB-23-2-0012	Management, Species, Cook Inlet Beluga Whale Ice Conditions, Military Training Noise Impacts, and Acoustical Monitoring, Joint Base Elmendorf-Richardson, Alaska	DOD-COE-AK	Posted	07/21/2023	08/21/2023FR-6700-N-29L	HUDRD - Exploring Office to Residential Conversions (HUDRD-EORC)	HUD	Posted	07/21/2023	10/12/2023 72030623APS00001	COUNTERING TRAFFICKING IN PERSONS (CTIP III) IN AFGHANISTAN	USAID-AFG	Posted	07/21/2023	08/25/2023 OIA-BIL-ECOSYSTEMS-RESTORATION-2023	OIA Bipartisan Infrastructure Law (BIL) Funding	DOI	Posted	07/21/2023	09/30/2023 DOD-2024-APEX-ACCELERATOR	APEX Accelerator Option Period for existing award recipients	DOD-AMC-ACCAPGADA	Posted	07/21/2023	10/06/2023",
    }

    data = generate_grants(json_data)
    assert type(data["grant"]) == str
    assert type(data["title"]) == str    
    
