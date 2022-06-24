a='Hyderabad'
# print(a[-9:]) # Hyderabad (In negative slicing,it will take positive value in place of negative value)
# print(a[-8:]) # yderabad
# print(a[-7:]) # derabad
# print(a[-6:]) # erabad
# print(a[-5:]) # rabad
# print(a[-4:]) # abad
# print(a[-3:]) # bad
# print(a[-2:]) # ad
# print(a[-1:]) # d
# print(a[-10:]) # Hyderabad (In negative values,if the index value is not there it will take the next comming index number)

# print(a[-9:-6]) # Hyd
# print(a[-8:-6]) # yd
# print(a[-5:-2]) # rab
# print(a[-3:-1]) # ba

# print(a[-2:-3]) # blank line (left side value is greater than the right side it will show blank line)

'''slicing double colon syntax'''
'print(a[starting index value:ending index value:splitting times])'
# print(a[::])

# print(a[::]) # Hyderabad ( double colon with empty indicates,it will take default value as starting,ending index values & splitting times -1)

# print(a[::1]) # dabaredyH (double colon indicates the reverse order of string )
# print(a[::2]) # dbrdH
# print(a[::3]) # dad
# print(a[::4]) # drH
# print(a[::5]) # de
# print(a[::6]) # dd
# print(a[::7]) # dy
# print(a[::8]) # dH
# print(a[::9]) # d
# print(a[::10]) # d

# print(a[2:5:1]) # der
# print(a[1:6:2]) # yea

