import requests

def get_cookie():
    url = "https://fanyi.baidu.com"
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    req = requests.get(url, headers= headers)
    print(f'{req.status_code}')
    print(f'{req.cookies}\n')
    for item in req.cookies:  # cookie信息
        print(f'Name = {item.name}')
        print(f'Value = {item.value}')