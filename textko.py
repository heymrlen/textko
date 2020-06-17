import requests
from bs4 import BeautifulSoup

to = '09613402477'
message = 'hello. how are you doing today?'

with requests.Session() as session:
    url = 'https://textko.com/send'
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    token = soup.find("meta", {"name":"csrf-token"})['content']
    print(token)
    cookies = r.cookies.get_dict()
    cookie_string = "; ".join([str(x)+"="+str(y) for x,y in cookies.items()])
    print(cookie_string)
    headers = {'cookie': cookie_string}
    data = {'_token': token, 'to': to, 'text': message}
    req = session.post(url=url, headers=headers, data=data)
    if req.status_code == 200:
        print(req.status_code)
        print('Message Sent!')
    else:
        print('Sorry. Something went wrong. Please try again...')
    session.close()