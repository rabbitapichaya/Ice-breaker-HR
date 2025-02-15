import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/rabbitapichaya/7a1be7f964e4264accb2cb60f7658ddf/raw/eddd89a50c363fe3e0b1d3c07f059f238ffef081/Apichaya-macro-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        # ENROLL WITH COUPON CODE: EDENMARCO
        # For 20% Discount on all pricing
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("person")

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data



if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/apichaya-nivasabutr-2a6078341/" , mock=True
        ),
    )