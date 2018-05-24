import requests


def send(filename, overlay=False, api_key='acf7c56e6088957', language='ger'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.json()


res = send(filename="C:\\Users\\vince\\Desktop\\15.jpg", language='ger', overlay=True)
print("Response:", res)
if res["ParsedResults"][0]["FileParseExitCode"] == 1:
    print(res["ParsedResults"][0]["ParsedText"])
else:
    print("ERROR")
    print("Response:", res)
