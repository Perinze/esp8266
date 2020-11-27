class URL_LISTENER:

	def __init__(self, wlan, port):
		import socket, re

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind(('0.0.0.0', port))
		self.server.listen(2)
		print("Server listen at {}:{}".format('0.0.0.0', port))
		
		self.route = {}

	def add_route(self, url, func):
		self.route[url] = func
	
	def start(self):
		while True:
			conn, addr = self.server.accept()
			request = conn.recv(1024)

			if len(request) > 0:
				request = request.decode()
				result = re.search("(.*?) (.*?) HTTP/1.1", request)
				if result:
					method = result.group(1)
					url = result.group(2)
					
					if method == "POST":
						postdata = re.search(".*?\r\n\r\n(.*)", request).group(1)
						if postdata:
							lists = postdata.split("&")
							payload = {}
							for pair in lists:
								key, value = pair.split("=")
								payload[key] = value

					self.route[url]()

					conn.send("HTTP/1.1 200 OK\r\n")
            		conn.send("Server: Esp8266\r\n")
       				     conn.send("Content-Type: text/html;charset=UTF-8\r\n")
		            conn.send("Connection: close\r\n")
            		conn.send("\r\n")

				else:
					print("URL not found")
			else:
				print("No request")

			conn.close()
