def second_cc_int(n):
	b = ''
	while n > 0:
		b = str(n % 2) + b
		n //= 2
	return b

def eight_cc_int(n):
	b = ''
	while n > 0:
		b = str(n % 8) + b
		n //= 8
	return b

def second_cc_float(n, count):
	b = ''
	m = int(n) - n
	while count > 0:
		rez = m * 2 
		b = (str(int(rez)) + b)
		m = int(rez) - rez
		count -= 1
	b = b.replace('-', '')
	return b

def eight_cc_float(n, count):
	b = ''
	m = int(n) - n
	while count > 0:
		rez = m * 8 
		b = (str(int(rez)) + b)
		m = int(rez) - rez
		count -= 1
	b = b.replace('-', '')
	return b
	
try:
	b = int(input('Какое число вы хотите перевести? Введите (без "") "1" - целое, "2" - если дробное: '))
	if b == 1 or b == 2:
		if b == 1:
			n = int(input('Введите целое число: '))
			a = int(input('Введите целевую систему счисления: '))
			if a == 2 or a == 8:
				if a == 2:
					if n < 0:
						n *= -1
						print(-n, '->', -int(second_cc_int(n)))
					else:
						print(n, '->', second_cc_int(n))
				if a == 8: 
					if n < 0:
						n *= -1
						print(-n, '->', -int(eight_cc_int(n)))
					else:
						print(n, '->', eight_cc_int(n))
			else:
				print('Простите, но данная программа может переводить только в 2сс и 8сс!')
		if b == 2:
			n = float(input('Введите дробное число (например 35.5): '))
			a = int(input('Введите целевую систему счисления: '))
			count = int(input('С какой точностью вывести результат? (кол-во знаков после ","): '))
			if a == 2 or a == 8:
				if a == 2:
					if n < 0:
						n *= -1
						res = second_cc_float(n, count)[::-1]
						print(-n, '->', '-' + second_cc_int(int(n)) + '.' + res)
					else:
						res = second_cc_float(n, count)[::-1]
						print(n, '->', second_cc_int(int(n)) + '.' + res)
				if a == 8: 
					if n < 0:
						n *= -1
						res = eight_cc_float(n, count)[::-1]
						print(-n, '->', '-' + eight_cc_int(int(n)) + '.' + res)
					else:
						res = eight_cc_float(n, count)[::-1]
						print(n, '->', eight_cc_int(int(n)) + '.' + res)
			else:
				print('Простите, но данная программа может переводить только в 2сс и 8сс!')
	else:
		print('Введите 1 или 2')
except ValueError:
	print('Ошибка')