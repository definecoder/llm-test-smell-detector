import requests

def get_final_url(url):
    response = requests.get(url, allow_redirects=True)
    return response.url

# original_url = "https://github.com/vmware/admiral"
# final_url = get_final_url(original_url)
# print("Final URL:", final_url)
