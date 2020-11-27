import wlan_connector
wlan_connector.connect()

from oled91 import OLED91
oled = OLED91(scl=5, sda=4)

def reimu():
	oled.display_text(('', 'Hakurei Reimu', '', ''))

def marisa():
	oled.display_text(('', 'Kirisame Marisa', '', ''))

from url_listener import URL_LISTENER
server = URL_LISTENER(80)
server.add_route('/reimu', reimu)
server.add_route('/marisa', marisa)
server.start()
