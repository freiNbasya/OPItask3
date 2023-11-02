import requests

def check_Url(base_url):
    api_url = base_url + "?offset=1"
    try:
        response = requests.get(api_url)
        if 200 <= response.status_code < 300:
            return base_url
        else:
            print(f"Connection to {api_url} failed.")
    except requests.exceptions.RequestException:
            print(f"Connection to {api_url} failed.")

