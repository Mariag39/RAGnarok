"""
MOBSF REST API Python Requests
"""

import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

SERVER = "http://127.0.0.1:8000"
APIKEY = '6d4a6dac120defa899e7349df3deff5f2ab315aa532f4e377b04d8e0d8278873'


def upload(filemob):
    """Upload File"""
    print("Uploading file")
    multipart_data = MultipartEncoder(fields={'file': (filemob, open(filemob, 'rb'), 'application/octet-stream')})
    headers = {'Content-Type': multipart_data.content_type, 'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/upload', data=multipart_data, headers=headers)
    print(response.text)
    return response.text


def scan(data):
    """Scan the file"""
    print("Scanning file")
    post_dict = json.loads(data)
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/scan', data=post_dict, headers=headers)
    print(response.text)


def pdf(data):
    """Generate PDF Report"""
    print("Generate PDF report")
    headers = {'Authorization': APIKEY}
    data = {"hash": json.loads(data)["hash"]}
    response = requests.post(SERVER + '/api/v1/download_pdf', data=data, headers=headers, stream=True)
    with open("report.pdf", 'wb') as flip:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                flip.write(chunk)
    print("Report saved as report.pdf")


def json_resp(data):
    """Generate JSON Report"""
    print("Generate JSON report")
    headers = {'Authorization': APIKEY}
    data = {"hash": json.loads(data)["hash"]}
    response = requests.post(SERVER + '/api/v1/report_json', data=data, headers=headers)
    print(response.text)


def delete(data):
    """Delete Scan Result"""
    print("Deleting Scan")
    headers = {'Authorization': APIKEY}
    data = {"hash": json.loads(data)["hash"]}
    response = requests.post(SERVER + '/api/v1/delete_scan', data=data, headers=headers)
    print(response.text)


'''RESP = upload()
scan(RESP)
json_resp(RESP)
pdf(RESP)
delete(RESP)'''