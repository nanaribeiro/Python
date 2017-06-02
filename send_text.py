from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "10814c3aa277848e4218CCCCCCCCC"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5562991229290", 
    from_="+15188740539",
    body="Hello Alana =D.")

print(message.sid)
