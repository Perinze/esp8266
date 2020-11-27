class OLED91:

	def __init__(self, scl, sda):
		import ssd1306
		from machine import Pin, I2C

		i2c = I2C(scl=Pin(scl), sda=Pin(sda))
		self.oled = ssd1306.SSD1306_I2C(128, 32, i2c)

	def display_text(self, strings):
		self.oled.fill(0)
		for i in range(4):
			self.oled.text(strings[i], 0, i * 8)
		self.oled.show()

