def connect()
	import json
	f = open('wlan.json', 'r')
	data = f.read()

	conf = json.loads(data)
	ssid = conf['ssid']
	passwd = conf['passwd']

	import network
	sta_if = network.WLAN(network.STA_IF)
	ap_if = network.WLAN(network.AP_IF)
	
	if ap_if.active():
		ap_if.active(False)

	sta_if.active(True)
	sta_if.connect(ssid, passwd)
	while not sta_if.isconnected():
		pass
	print(sta_if.ifconfig())

	f.close()
	return sta_if
