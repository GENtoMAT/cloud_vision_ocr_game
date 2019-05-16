
import requests

proxy_dict = {
    "http": "http://proxy.tv-asahi.co.jp:8080/"
}

req = requests.get("http://yahoo.co.jp/", proxies=proxy_dict)

print(req.text)

