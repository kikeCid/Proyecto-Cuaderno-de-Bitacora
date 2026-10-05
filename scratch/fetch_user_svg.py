import urllib.request

url = "https://www.lineadirecta.com/o/lda-webcomercial-theme/images/icon-user.svg"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        print("Success! icon-user.svg:")
        print(content)
        with open('01_Proyectos/assets/img/icon-user.svg', 'w', encoding='utf-8') as f:
            f.write(content)
except Exception as e:
    print("Error:", e)
