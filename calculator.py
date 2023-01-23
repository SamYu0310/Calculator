import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty 
from kivy.lang import Builder 
from kivy.core.window import Window 

Window.size = (500, 700)

Builder.load_file("calculator.kv")

class MyLayout(Widget): 

	def clear(self): 
		self.ids.calc_input.text = '0'

	def remove(self): 
		prior = self.ids.calc_input.text
		if "Error" not in prior: 
			if len(prior) >= 1: 
				prior = prior[:-1]
				self.ids.calc_input.text = prior
		else: 
			pass

	def button_press(self, button): 
		prior = self.ids.calc_input.text 
		if "Error" in prior: 
			self.ids.calc_input.text = f'{button}'
		elif prior = '': 
			self.ids.calc_input.text = f'{button}' 
		elif prior == "0" or prior[0] == ' ':
			self.ids.calc_input.text = f'{button}'
		else: 
			self.ids.calc_input.text = f'{prior}{button}'

	def percent(self): 
		prior = self.ids.calc_input.text
		pre = ""
		if prior != "Error": 
			if prior[0] == " ": 
				if prior[1] == "-": 
					pre = "-"
					prior = prior[2:]
				else: 
					prior = prior[1:]
			if prior[0] == "-": 
				pre = "-"
				prior = prior[1:]
			if "." in prior: 
				num_list = prior.split(".")
				if len(num_list[0]) > 2: 
					self.ids.calc_input.text = f'{pre}{num_list[0][:-2]}.{num_list[-2:]}{num_list[1]}'
				if len(num_list[0]) == 2: 
					self.ids.calc_input.text = f'{pre}0.{num_list[0]}{num_list[1]}'
				if len(num_list[0]) == 1: 
					self.ids.calc_input.text = f'{pre}0.0{num_list[0]}{num_list[1]}'
				if len(num_list[0]) == 0: 
					self.ids.calc_input.text = f'{pre}0.00{num_list[1]}'
			else: 
				if len(prior) > 2: 
					self.ids.calc_input.text = f'{pre}{prior[:-2]}.{prior[-2:]}'
				if len(prior) == 2: 
					self.ids.calc_input.text = f'{pre}0.{prior}'
				if len(prior) == 1: 
					self.ids.calc_input.text = f'{pre}0.0{prior}'
				if len(prior) == 0: 
					self.ids.calc_input.text = ""

	def dot(self): 
		prior = self.ids.calc_input.text
		if prior != "Error":
			if prior[0] == " ": 
				prior = f'0.'
			add_list = prior.split("+")
			multiply_list = prior.split("*")
			subtract_list = prior.split("-")
			divide_list = prior.split("/")
			if "+" in prior and "." not in add_list[-1]: 
				prior += f'.'
			if "*" in prior and "." not in multiply_list[-1]: 
				prior += f'.'
			if "-" in prior and "." not in subtract_list[-1]: 
				prior += f'.'
			if "/" in prior and "." not in divide_list[-1]: 
				prior += f'.'
			if "." in prior: 
				pass 
			else: 
				prior += f'.'
			self.ids.calc_input.text = prior

	def pos_neg(self): 
		prior = self.ids.calc_input.text
		if prior != "Error": 
			if "-" in prior: 
				self.ids.calc_input.text = f'{prior.replace("-", "")}'
			else: 
				self.ids.calc_input.text = f'-{prior}'

	def math_sign(self, sign): 
		prior = self.ids.calc_input.text 
		if prior != "Error": 
			if prior[0] == " ": 
				prior = prior[1:]
			self.ids.calc_input.text = f'{prior}{sign}'

	def equals(self): 
		prior = self.ids.calc_input.text
		try: 
			answer = eval(prior)
			if int(answer) == float(answer): 
				answer = str(int(answer))
			else: 
				answer = str(eval(prior))
			if len(answer) > 10: 
				answer = answer[:11]
			self.ids.calc_input.text = f' {answer}' 
		except: 
			self.ids.calc_input.text = "Error"

class CalculatorApp(App): 
	def build(self): 
		return MyLayout()

if __name__ == "__main__": 
	CalculatorApp().run()
