from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACdfae18e7e527fad3d567292b0acc9c12"
# Your Auth Token from twilio.com/console
auth_token  = "10814c3aa277848e421850a9a28ed470"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5562991229290", 
    from_="+15188740539",
    body="Hello Alana =/.")

print(message.sid)
