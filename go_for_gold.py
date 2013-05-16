"""
go_for_gold.py
=====
Translate an athlete's finishing placement (1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal.  Do this by asking for user input.  For example:

What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!

"""
medal = raw_input('What number should I translate into a medal?\n')

if  int(medal) == 1:
	print('gold')
elif int(medal) == 3:
	print ('bronze')
elif int(medal) == 2:
	print ('silver')
else:
	print('No medal for you!')