import nexmo

client = nexmo.Client(key="ee474558", secret="VhqdlSlaU9zehhL1")

client.send_message({
    'from': "Nexmo",
    'to': "5561995578869",
    'text': "Hello from Nexmo",
})
