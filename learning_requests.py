import requests
import random


url = 'https://icanhazdadjoke.com'
try:
    get_response = requests.get(url)
    print(get_response)
except requests.Exception.Connection.Error:
        pass

def get_jokes():
    search_term = input("Which type of jokes you want : ")
    response = requests.get(url, headers = {"Accept" : "Application/json"}, params = {"term" : search_term})
    resp = response.content.decode('UTF-8')
    data = response.json()
    #print(data)
    rand_jokes = random.choice(list(data.values()))
    total = len(data)

    if total == 1 :
        print(f"I have got one joke about {search_term}.")
        print(data[0]["joke"])

    elif total >1:
        print(f"I have got {total} jokes about {search_term}")
        rand_num = random.randint(0, total -1)
        print(f"showing one of them :- {data['joke']}.")

    else:
        print(f"no jokes found")

get_jokes()
