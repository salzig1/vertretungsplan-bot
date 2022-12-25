from twilio.rest import Client 
from weather import Weather
import time
import sys


weather = Weather("127ce0a3aad14f238e6193830222112", 
                  "47.68768451708976,11.576040434014303")

twilio_sid = sys.argv[1]
twilio_token = sys.argv[2]

client = Client(twilio_sid, twilio_token)

processed_message_sids = []
messages = client.messages.list()
for m in messages:
    processed_message_sids.append(m.sid)

while True:
    time.sleep(3)
    messages = client.messages.list()
    messages.sort(key=lambda x: x.date_sent, reverse=True)
    message = messages[0]

    if message.direction == "inbound" and message.sid not in processed_message_sids:
        processed_message_sids.append(message.sid)
        if message.body == "wetter":
            current_temperatur = weather.get_current_temperatur()

            message = client.messages \
                            .create(
                                body= ("Die Temperatur in Lenggries beträgt "
                                        f"{current_temperatur} Grad Celsius"),
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+4915170849221'
                            )