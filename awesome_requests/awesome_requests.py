import urllib.request
import json

def cool_dog_facts():
    """
    Fetches a random dog fact from the Dog API.
    """
    try:
        resp = urllib.request.urlopen("https://dogapi.dog/api/v2/facts?limit=1")
        data_json = resp.read().decode("utf-8")
        data = json.loads(data_json)
        fact_info = data["data"][0]["attributes"]["body"]
    except Exception as e:
        fact_info = f"Could not retrieve dog fact: {e}"
    return fact_info


