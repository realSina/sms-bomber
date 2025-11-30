<h1 align="center">SMS Bomber</h1>

<p align="center">
A fast multi-request tool for testing SMS/OTP endpoints in parallel.<br>
Automatically normalizes Iranian phone numbers and sends all requests simultaneously.
</p>

---

## Features
-  **Auto phone-number normalization**  
  Accepts any Iranian format and converts it into a valid 10-digit mobile number.

-  **Parallel request execution**  
  All API calls are fired at the same time using threads.

-  **High-performance request handling**  
  Powered by `ThreadPoolExecutor` for maximum speed.

-  **Easy to expand**  
  Add or remove endpoints directly inside `requests_data`.

---

##  Installation
```bash
git clone https://github.com/realSina/sms-bomber.git
cd sms-bomber
pip install -r requirements.txt
```

---

##  Usage
```bash
python3 main.py 09123456789
```

The script will:
1. Normalize the phone number  
2. Send all OTP/SMS-related requests in parallel  
3. Print status and response-time for each request  

---

##  Project Structure
```
.
├── main.py
├── requirements.txt
└── README.md
```

---

##  Disclaimer
This tool is intended **solely for educational purposes, debugging, and API load-testing**.  
Use only with **explicit permission** of the phone number owner.  
The author is not responsible for any misuse.

---

##  License
MIT License
