import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def req(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass


target_url = "http://192.168.0.104/mutillidae/index.php?page=login.php"
response = req(target_url)
resp = response.content.decode('UTF-8')
parsed_html = BeautifulSoup(resp, features="html.parser")
forms_list = parsed_html.findAll('form')

for form in forms_list:
    action = form.get("action")
    post_url = urljoin(target_url, action)
    method = form.get("method")

    inputs_list = form.findAll("input")
    post_data = {}
    for inputs in inputs_list:
        input_name = inputs.get("name")
        input_type = inputs.get("type")
        input_value = inputs.get("value")
        if input_type == "text":
            input_value = "test"


        post_data[input_name] = input_value

    result = requests.post(post_url, data=post_data)
    res = result.content.decode('UTF-8')
    print(res)
