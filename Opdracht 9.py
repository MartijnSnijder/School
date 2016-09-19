Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L1 = [1,4,5,16,61,77]
>>> L2 = [2,4,5,6]
>>> def merge(L1, L2):
	L3 = []
	while (L1 and L2):
		if (L1[0] <= L2[0]):
			item = L1.pop(0)
			L3.append(item)
		else:
			item = L2.pop(0)
			L3.append(item)
	L3.extend(L1 if L1 else L2)
	return L3

>>> merge(L1, L2)
[1, 2, 4, 4, 5, 5, 6, 16, 61, 77]
>>> merge(L1, L2)



