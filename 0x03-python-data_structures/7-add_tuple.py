#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	l = []
	for i in range(2):
		try:
			l.append(tuple_a[i])
		except IndexError :
			l.append(0)
		try:
			l.append(tuple_b[i])
		except IndexError :
			l.append(0)
	return (l[0] + l[1], l[2] + l[3])
