# Example 1

import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/domain.com/messages",
        auth=("api", "key-5891601XXXXXXXXXXXXXXXf"),
        data={"from": "Mailgun Sandbox <postmaster@domain.com>",
              "to": "Customer 1 <customer1@gmail.com>",
              "subject": "Hello Customer 1",
              "text": "Congratulations Customer 1, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})

send_simple_message()

# Example 2

import requests

def send_simple_message(API_BASE_URL, API_KEY):
    return requests.post(
        API_BASE_URL,
        auth=("api", API_KEY),
        data={"from": "Developer contact@narenarya.in",
              "to": ["customer1@gmail.com", "customer2@gmail.com"],
              "subject": "Hello!",
              "text": "Thanks for signing up with us!."})

send_simple_message("https://api.mailgun.net/v3/narenarya.in/messages",
                    "key-5891601XXXXXXXXXXXXXXXf")