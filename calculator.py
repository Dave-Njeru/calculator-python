import numpy as np
import sys, traceback, logging
from tkinter import *

top = Tk()
top.geometry("230x196")
 
list1 = []
def onButtonClick(val):
	entry.insert(END, val)
def dotOnClick():
	entry.insert(END, ".")
def undoOnClick():
	k = 0
	for x in entry.get():
		k = k + 1
	l = k - 1	
	entry.delete(l)
def clearOnClick():
	list1.clear()
	entry.delete(0, END)
def operators(sign):
	entry.insert(END, sign)
def insert(val):
	entry.insert(END, val)
def equals():
	list1.clear()
	for x in entry.get():
		list1.append(x)
	try:
		if('+' in list1 and list1[0] != '+'):
			calculation('+')
		elif('-' in list1 and list1[0] != '-'):
			calculation('-')
		elif('x' in list1):
			calculation('x')
		elif('/' in list1):
			calculation('/')
		elif('%' in list1):
			calculation('%')
		elif('+' in list1 and list1[0] == '+'):
			del list1[0]
			calculation('+')
		elif('-' in list1 and list1[0] == '-'):
			del list1[0]
			calculation('-')
	except:
		valueGot = entry.get()
		entry.insert(END, valueGot)
def calculation(val):
	list1.clear()
	for x in entry.get():
		list1.append(x)
	try:
		if (list1[0] == '+'):
			del list1[0]
			get = calculation_2(val)
			getValue1 = get[0]
			getValue2 = get[1]
			if(val == 'x'):
				total = getValue1 * getValue2
			elif(val == '/'):
				total = getValue1 / getValue2
			elif(val == '+'):
				total = getValue1 + getValue2
			elif(val == '-'):
				total = getValue1 - getValue2
			else:
				total = getValue1 % getValue2
			entry.delete(0, END)
			entry.insert(END, total)
		elif (list1[0] == '-'):
			del list1[0]
			get = calculation_2(val)
			getValue1 = -get[0]
			getValue2 = get[1]
			if(val == 'x'):
				total = getValue1 * getValue2
			elif(val == '/'):
				total = getValue1 / getValue2
			elif(val == '+'):
				total = getValue1 + getValue2
			elif(val == '-'):
				total = getValue1 - getValue2
			else:
				total = getValue1 % getValue2
			entry.delete(0, END)
			entry.insert(END, total)
		else:
			a = list1[:list1.index(val)]
			
			if('.' in a):
				a_float_final = float("".join(map(str, a)))
			else:
				a_float_list = list(map(float, a))
				a_float = ("".join(map(str, a_float_list)))
				
				count = 1
				numberOfTimes = a_float.count('.')
				
				while count < numberOfTimes:
					j  = a_float.index('.')
					i = a_float.index('.') + 1
					b = bytearray(a_float, encoding='utf8')
					del b[i]
					del b[j]
					
					a_float = str(b, encoding='utf8')
					count = count + 1
					
				a_float_final = float("".join(map(str, a_float)))
				
			#get the second value
			
			b = list1[list1.index(val) + 1:]
			
			if('.' in b):
				b_float_final = float("".join(map(str, b)))
			else:
				b_float_list = list(map(float, b))
				b_float = ("".join(map(str, b_float_list)))
				
				count = 1
				numberOfTimes_2 = b_float.count('.')
				
				while count < numberOfTimes_2:
					q  = b_float.index('.')
					w = b_float.index('.') + 1
					e = bytearray(b_float, encoding='utf8')
					del e[w]
					del e[q]
					
					b_float = str(e, encoding='utf8')
					count = count + 1
					
				b_float_final = float("".join(map(str, b_float)))
				
			if(val == '+'):
				total = a_float_final + b_float_final
			elif(val == '-'):
				total = a_float_final - b_float_final
			elif(val == 'x'):
				total = a_float_final * b_float_final
			elif(val == '/'):
				total = a_float_final / b_float_final
			elif(val == '%'):
				total = a_float_final % b_float_final
				
			entry.delete(0, END)
			entry.insert(END, total)
	except:
		entry.delete(0, END)
		entry.insert(END, "Syntax Error")
		logging.exception("An error occurred")
def calculation_2(val):
	try:
		a = list1[:list1.index(val)]
			
		if('.' in a):
			a_float_final = float("".join(map(str, a)))
		else:
			a_float_list = list(map(float, a))
			a_float = ("".join(map(str, a_float_list)))
				
			count = 1
			numberOfTimes = a_float.count('.')
				
			while count < numberOfTimes:
				j  = a_float.index('.')
				i = a_float.index('.') + 1
				b = bytearray(a_float, encoding='utf8')
				del b[i]
				del b[j]
					
				a_float = str(b, encoding='utf8')
				count = count + 1
					
			a_float_final = float("".join(map(str, a_float)))
				
		#get the second value
			
		b = list1[list1.index(val) + 1:]
			
		if('.' in b):
			b_float_final = float("".join(map(str, b)))
		else:
			b_float_list = list(map(float, b))
			b_float = ("".join(map(str, b_float_list)))
				
			count = 1
			numberOfTimes_2 = b_float.count('.')
				
			while count < numberOfTimes_2:
				q = b_float.index('.')
				w = b_float.index('.') + 1
				e = bytearray(b_float, encoding='utf8')
				del e[w]
				del e[q]
					
				b_float = str(e, encoding='utf8')
				count = count + 1
					
			b_float_final = float("".join(map(str, b_float)))
		return [a_float_final, b_float_final]
	except:
		logging.exception("An error occurred")
#Design entry
entry = Entry(top, bd=4, width=24, justify="right")
entry.place(x=10, y=10)
#Design buttons
btn7 = Button(top, text="7", command = lambda: onButtonClick(7))
btn7.place(x=10, y=50)
	
btn8 = Button(top, text="8", command = lambda: onButtonClick(8))
btn8.place(x=50, y=50)
	
btn9 = Button(top, text="9", command = lambda: onButtonClick(9))
btn9.place(x=90, y=50)
	
btnplus = Button(top, text="+", height=1, width=1, command = lambda: operators('+'))
btnplus.place(x=130, y=50)

btnclear = Button(top, text="Undo", height=1, width=2, command = lambda: undoOnClick())
btnclear.place(x=170, y=50)
	
btnequals = Button(top, text="=", height=3, width=2, command = lambda: equals())
btnequals.place(x=170, y=120)
	
btn4 = Button(top, text="4", command = lambda: onButtonClick(4))
btn4.place(x=10, y=85)
	
btn5 = Button(top, text="5", command = lambda: onButtonClick(5))
btn5.place(x=50, y=85)
	
btn6 = Button(top, text="6", command = lambda: onButtonClick(6))
btn6.place(x=90, y=85)
	
btnmult = Button(top, text="x", height=1, width=1, command = lambda: operators('x'))
btnmult.place(x=130, y=85)

btnclear = Button(top, text="Clear", height=1, width=2, command = lambda: clearOnClick())
btnclear.place(x=170, y=85)
	
btn1 = Button(top, text="1", command = lambda: onButtonClick(1))
btn1.place(x=10, y=120)
	
btn2 = Button(top, text="2", command = lambda: onButtonClick(2))
btn2.place(x=50, y=120)
	
btn3 = Button(top, text="3", command = lambda: onButtonClick(3))
btn3.place(x=90, y=120)
	
btnminus = Button(top, text="-", height=1, width=1, command = lambda: operators('-'))
btnminus.place(x=130, y=120)
	
btn0 = Button(top, text="0", command = lambda: onButtonClick(0))
btn0.place(x=10, y=155)
 
btndot = Button(top, text=".", height=1, width=1, command = lambda: dotOnClick())
btndot.place(x=50, y=155)
	
btnmodulus = Button(top, text="%", height=1, width=1, command = lambda: operators('%'))
btnmodulus.place(x=90, y=155)
	
btndiv = Button(top, text="/", height=1, width=1, command = lambda: operators('/'))
btndiv.place(x=130, y=155)
	
top.mainloop()
