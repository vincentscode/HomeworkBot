import requests


def send(filename, overlay=False, api_key='acf7c56e6088957', language='ger', pdf=False):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isCreateSearchablePdf': pdf
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.json()


res = send(filename="C:\\Users\\vince\\Desktop\\iwas.jpg", language='ger', overlay=True, pdf=True)
file = open("C:\\Users\\vince\\Desktop\\resp.npp", "w")
file.write(str(res))
file.close()
'''
print("Response:", res)
if res["ParsedResults"][0]["FileParseExitCode"] == 1:
    print(res["ParsedResults"][0]["ParsedText"])
else:
    print("ERROR")
    print("Response:", res)
'''