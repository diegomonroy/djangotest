import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxcc01264646364147b771514d6cc87e0f.mailgun.org/messages",
        auth=("api", "key-c77133775487ac4908ae629cb028ed25"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxcc01264646364147b771514d6cc87e0f.mailgun.org>",
              "to": "Diego Monroy <gn4@gaitannicholls.com>",
              "subject": "Hello Diego Monroy",
              "text": "Congratulations Diego Monroy, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})

send_simple_message()