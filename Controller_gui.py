from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import serial

# serl = serial.Serial()
# serl.baudrate = 250000
# serl.port = 'COM3'
# serl.open()
# ram=457

class MyApp(App):
	def __init__(self, **kwargs):
		super(MyApp, self).__init__(**kwargs)
		self.pitch_kp = 0.0
		self.pitch_ki = 0.0
		self.pitch_kd = 0.0
		self.roll_kp =  0.0
		self.roll_ki = 0.0
		self.roll_kd = 0.0
		self.yaw_kp = 4.0
		self.yaw_ki = 0.00525
		self.yaw_kd = 0.00
		self.pitch_offset = 0.00
		self.roll_offset = 0.00
		self.yaw_offset = 0.00

		self.pitch_kp_margin = 0.05
		self.pitch_ki_margin = 0.003
		self.pitch_kd_margin = 0.5
		self.roll_kp_margin = 0.05
		self.roll_ki_margin = 0.003
		self.roll_kd_margin = 0.5
		self.yaw_kp_margin = 0.05
		self.yaw_ki_margin = 0.003
		self.yaw_kd_margin = 0.5
		self.pitch_offset_margin = 1.0
		self.roll_offset_margin = 1.0
		self.yaw_offset_margin = 1.0

		self.pitch_kp_value = Label(text = str(self.pitch_kp))
		self.pitch_ki_value = Label(text = str(self.pitch_ki))
		self.pitch_kd_value = Label(text = str(self.pitch_kd))
		self.pitch_offset_value = Label(text = str(self.pitch_offset))

		self.roll_kp_value = Label(text = str(self.roll_kp))
		self.roll_ki_value = Label(text = str(self.roll_ki))
		self.roll_kd_value = Label(text = str(self.roll_kd))
		self.roll_offset_value = Label(text = str(self.roll_offset))

		self.yaw_kp_value = Label(text = str(self.yaw_kp))
		self.yaw_ki_value = Label(text = str(self.yaw_ki))
		self.yaw_kd_value = Label(text = str(self.yaw_kd))
		self.yaw_offset_value = Label(text = str(self.yaw_offset))

	def build(self):
		layout = BoxLayout(spacing = 20, orientation = 'vertical')


		pitch_inner_layout = BoxLayout(orientation = 'horizontal')
		pitch_constants_inc_dec = BoxLayout(orientation = 'vertical')
		pitch_constants_values = BoxLayout(orientation = 'vertical')
		pitch_offset_inc_dec = BoxLayout(orientation = 'vertical')

		pitch_label = Label(text = 'Pitch')
		pitch_kp_increase = Button(text = 'Increase Pitch kp', on_press = self.increase_pitch_kp)
		pitch_kp_decrease = Button(text = 'Decrease Pitch kp', on_press = self.decrease_pitch_kp)
		pitch_ki_increase = Button(text = 'Increase Pitch ki', on_press = self.increase_pitch_ki)
		pitch_ki_decrease = Button(text = 'Decrease Pitch ki', on_press = self.decrease_pitch_ki)
		pitch_kd_increase = Button(text = 'Increase Pitch kd', on_press = self.increase_pitch_kd)
		pitch_kd_decrease = Button(text = 'Decrease Pitch kd', on_press = self.decrease_pitch_kd)

		pitch_offset_increase = Button(text = 'Increase Pitch offset', on_press = self.increase_pitch_offset)
		pitch_offset_decrease = Button(text = 'Decrease Pitch offset', on_press = self.decrease_pitch_offset)

		pitch_constants_inc_dec.add_widget(pitch_kp_increase)
		pitch_constants_inc_dec.add_widget(pitch_kp_decrease)
		pitch_constants_inc_dec.add_widget(pitch_ki_increase)
		pitch_constants_inc_dec.add_widget(pitch_ki_decrease)
		pitch_constants_inc_dec.add_widget(pitch_kd_increase)
		pitch_constants_inc_dec.add_widget(pitch_kd_decrease)

		pitch_offset_inc_dec.add_widget(pitch_offset_increase)
		pitch_offset_inc_dec.add_widget(pitch_offset_decrease)

		pitch_constants_values.add_widget(self.pitch_kp_value)
		pitch_constants_values.add_widget(self.pitch_ki_value)
		pitch_constants_values.add_widget(self.pitch_kd_value)

		pitch_inner_layout.add_widget(pitch_label)
		pitch_inner_layout.add_widget(pitch_constants_inc_dec)
		pitch_inner_layout.add_widget(pitch_constants_values)
		pitch_inner_layout.add_widget(pitch_offset_inc_dec) #
		pitch_inner_layout.add_widget(self.pitch_offset_value)

		layout.add_widget(pitch_inner_layout)



		roll_inner_layout = BoxLayout(orientation = 'horizontal')
		roll_constants_inc_dec = BoxLayout(orientation = 'vertical')
		roll_constants_values = BoxLayout(orientation = 'vertical')
		roll_offset_inc_dec = BoxLayout(orientation = 'vertical')

		roll_label = Label(text = 'Roll')
		roll_kp_increase = Button(text = 'Increase roll kp', on_press = self.increase_roll_kp)
		roll_kp_decrease = Button(text = 'Decrease roll kp', on_press = self.decrease_roll_kp)
		roll_ki_increase = Button(text = 'Increase roll ki', on_press = self.increase_roll_ki)
		roll_ki_decrease = Button(text = 'Decrease roll ki', on_press = self.decrease_roll_ki)
		roll_kd_increase = Button(text = 'Increase roll kd', on_press = self.increase_roll_kd)
		roll_kd_decrease = Button(text = 'Decrease roll kd', on_press = self.decrease_roll_kd)

		roll_offset_increase = Button(text = 'Increase roll offset', on_press = self.increase_roll_offset)
		roll_offset_decrease = Button(text = 'Decrease roll offset', on_press = self.decrease_roll_offset)

		roll_constants_inc_dec.add_widget(roll_kp_increase)
		roll_constants_inc_dec.add_widget(roll_kp_decrease)
		roll_constants_inc_dec.add_widget(roll_ki_increase)
		roll_constants_inc_dec.add_widget(roll_ki_decrease)
		roll_constants_inc_dec.add_widget(roll_kd_increase)
		roll_constants_inc_dec.add_widget(roll_kd_decrease)

		roll_offset_inc_dec.add_widget(roll_offset_increase)
		roll_offset_inc_dec.add_widget(roll_offset_decrease)

		roll_constants_values.add_widget(self.roll_kp_value)
		roll_constants_values.add_widget(self.roll_ki_value)
		roll_constants_values.add_widget(self.roll_kd_value)

		roll_inner_layout.add_widget(roll_label)
		roll_inner_layout.add_widget(roll_constants_inc_dec)
		roll_inner_layout.add_widget(roll_constants_values)
		roll_inner_layout.add_widget(roll_offset_inc_dec) #
		roll_inner_layout.add_widget(self.roll_offset_value)

		layout.add_widget(roll_inner_layout)



		yaw_inner_layout = BoxLayout(orientation = 'horizontal')
		yaw_constants_inc_dec = BoxLayout(orientation = 'vertical')
		yaw_constants_values = BoxLayout(orientation = 'vertical')
		yaw_offset_inc_dec = BoxLayout(orientation = 'vertical')

		yaw_label = Label(text = 'Yaw')
		yaw_kp_increase = Button(text = 'Increase yaw kp', on_press = self.increase_yaw_kp)
		yaw_kp_decrease = Button(text = 'Decrease yaw kp', on_press = self.decrease_yaw_kp)
		yaw_ki_increase = Button(text = 'Increase yaw ki', on_press = self.increase_yaw_ki)
		yaw_ki_decrease = Button(text = 'Decrease yaw ki', on_press = self.decrease_yaw_ki)
		yaw_kd_increase = Button(text = 'Increase yaw kd', on_press = self.increase_yaw_kd)
		yaw_kd_decrease = Button(text = 'Decrease yaw kd', on_press = self.decrease_yaw_kd)

		yaw_offset_increase = Button(text = 'Increase yaw offset', on_press = self.increase_yaw_offset) #
		yaw_offset_decrease = Button(text = 'Decrease yaw offset', on_press = self.decrease_yaw_offset) #

		yaw_constants_inc_dec.add_widget(yaw_kp_increase)
		yaw_constants_inc_dec.add_widget(yaw_kp_decrease)
		yaw_constants_inc_dec.add_widget(yaw_ki_increase)
		yaw_constants_inc_dec.add_widget(yaw_ki_decrease)
		yaw_constants_inc_dec.add_widget(yaw_kd_increase)
		yaw_constants_inc_dec.add_widget(yaw_kd_decrease)

		yaw_offset_inc_dec.add_widget(yaw_offset_increase) #
		yaw_offset_inc_dec.add_widget(yaw_offset_decrease) #

		yaw_constants_values.add_widget(self.yaw_kp_value)
		yaw_constants_values.add_widget(self.yaw_ki_value)
		yaw_constants_values.add_widget(self.yaw_kd_value)

		yaw_inner_layout.add_widget(yaw_label)
		yaw_inner_layout.add_widget(yaw_constants_inc_dec)
		yaw_inner_layout.add_widget(yaw_constants_values)
		yaw_inner_layout.add_widget(yaw_offset_inc_dec) #
		yaw_inner_layout.add_widget(self.yaw_offset_value)

		layout.add_widget(yaw_inner_layout)


		return layout


	def give_serial_output(self):
		serl.write(str(int(100 * self.pitch_kp)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(10000 * self.pitch_ki)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(100 * self.pitch_kd)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(100 * self.roll_kp)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(10000 * self.roll_ki)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(100 * self.roll_kd)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(100 * self.yaw_kp)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(10000 * self.yaw_ki)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(100 * self.yaw_kd)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(self.pitch_offset)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(self.roll_offset)).encode())
		serl.write(str('\n').encode())
		serl.write(str(int(self.yaw_offset)).encode())
		serl.write(str('\n').encode())

	def increase_pitch_kp(self, obj):
		self.pitch_kp = self.pitch_kp + self.pitch_kp_margin
		self.pitch_kp_value.text = str(self.pitch_kp)
		self.give_serial_output()
		print (self.pitch_kp)

	def decrease_pitch_kp(self, obj):
		self.pitch_kp = self.pitch_kp - self.pitch_kp_margin
		self.pitch_kp_value.text = str(self.pitch_kp)
		self.give_serial_output()
		print (self.pitch_kp)

	def increase_pitch_ki(self, obj):
		self.pitch_ki = self.pitch_ki + self.pitch_ki_margin
		self.pitch_ki_value.text = str(self.pitch_ki)
		self.give_serial_output()
		print (self.pitch_ki)

	def decrease_pitch_ki(self, obj):
		self.pitch_ki = self.pitch_ki - self.pitch_ki_margin
		self.pitch_ki_value.text = str(self.pitch_ki)
		self.give_serial_output()
		print (self.pitch_ki)

	def increase_pitch_kd(self, obj):
		self.pitch_kd = self.pitch_kd + self.pitch_kd_margin
		self.pitch_kd_value.text = str(self.pitch_kd)
		self.give_serial_output()
		print (self.pitch_kd)
		

	def decrease_pitch_kd(self, obj):
		self.pitch_kd = self.pitch_kd - self.pitch_kd_margin
		self.pitch_kd_value.text = str(self.pitch_kd)
		self.give_serial_output()
		print (self.pitch_kd)

	def increase_roll_kp(self, obj):
		self.roll_kp = self.roll_kp + self.roll_kp_margin
		self.roll_kp_value.text = str(self.roll_kp)
		self.give_serial_output()
		print (self.roll_kp)

	def decrease_roll_kp(self, obj):
		self.roll_kp = self.roll_kp - self.roll_kp_margin
		self.roll_kp_value.text = str(self.roll_kp)
		self.give_serial_output()
		print (self.roll_kp)
		

	def increase_roll_ki(self, obj):
		self.roll_ki = self.roll_ki + self.roll_ki_margin
		self.roll_ki_value.text = str(self.roll_ki)
		self.give_serial_output()
		print (self.roll_ki)

	def decrease_roll_ki(self, obj):
		self.roll_ki = self.roll_ki - self.roll_ki_margin
		self.roll_ki_value.text = str(self.roll_ki)
		self.give_serial_output()
		print (self.roll_ki)

	def increase_roll_kd(self, obj):
		self.roll_kd = self.roll_kd + self.roll_kd_margin
		self.roll_kd_value.text = str(self.roll_kd)
		self.give_serial_output()
		print (self.roll_kd)

	def decrease_roll_kd(self, obj):
		self.roll_kd = self.roll_kd - self.roll_kd_margin
		self.roll_kd_value.text = str(self.roll_kd)
		self.give_serial_output()
		print (self.roll_kd)

	def increase_yaw_kp(self, obj):
		self.yaw_kp = self.yaw_kp + self.yaw_kp_margin
		self.yaw_kp_value.text = str(self.yaw_kp)
		self.give_serial_output()
		print (self.yaw_kp)

	def decrease_yaw_kp(self, obj):
		self.yaw_kp = self.yaw_kp - self.yaw_kp_margin
		self.yaw_kp_value.text = str(self.yaw_kp)
		self.give_serial_output()
		print (self.yaw_kp)

	def increase_yaw_ki(self, obj):
		self.yaw_ki = self.yaw_ki + self.yaw_ki_margin
		self.yaw_ki_value.text = str(self.yaw_ki)
		self.give_serial_output()
		print (self.yaw_ki)

	def decrease_yaw_ki(self, obj):
		self.yaw_ki = self.yaw_ki - self.yaw_ki_margin
		self.yaw_ki_value.text = str(self.yaw_ki)
		self.give_serial_output()
		print (self.yaw_ki)

	def increase_yaw_kd(self, obj):
		self.yaw_kd = self.yaw_kd + self.yaw_kd_margin
		self.yaw_kd_value.text = str(self.yaw_kd)
		self.give_serial_output()
		print (self.yaw_kd)

	def decrease_yaw_kd(self, obj):
		self.yaw_kd = self.yaw_kd - self.yaw_kd_margin
		self.yaw_kd_value.text = str(self.yaw_kd)
		self.give_serial_output()
		print (self.yaw_kd)

#Offset Events
	def increase_pitch_offset(self, obj):
		self.pitch_offset = self.pitch_offset + self.pitch_offset_margin
		self.pitch_offset_value.text = str(self.pitch_offset)
		self.give_serial_output()
		print (self.pitch_kp)

	def decrease_pitch_offset(self, obj):
		self.pitch_offset = self.pitch_offset - self.pitch_offset_margin
		self.pitch_offset_value.text = str(self.pitch_offset)
		self.give_serial_output()
		print (self.pitch_offset)

	def increase_roll_offset(self, obj):
		self.roll_offset = self.roll_offset + self.roll_offset_margin
		self.roll_offset_value.text = str(self.roll_offset)
		self.give_serial_output()
		print (self.roll_offset)

	def decrease_roll_offset(self, obj):
		self.roll_offset = self.roll_offset - self.roll_offset_margin
		self.roll_offset_value.text = str(self.roll_offset)
		self.give_serial_output()
		print (self.roll_offset)

	def increase_yaw_offset(self, obj):
		self.yaw_offset = self.yaw_offset + self.yaw_offset_margin
		self.yaw_offset_value.text = str(self.yaw_offset)
		self.give_serial_output()
		print (self.yaw_offset)

	def decrease_yaw_offset(self, obj):
		self.yaw_offset = self.yaw_offset - self.yaw_offset_margin
		self.yaw_offset_value.text = str(self.yaw_offset)
		self.give_serial_output()
		print (self.yaw_offset)

if __name__ == '__main__':
	MyApp().run()