import sys
card_number = input("Please enter card number:")
mm_yy = input("Please enter mm/yy:" )
CVV = input ("Please enter CVV:" )
try:
int(expire_date)
except: #ValueError:
    print ("OK")
if len(card_number) != 16:
    sys.exit(1)
if len(CVV)  < 3:
    sys.exit("Error!!!")
if int(card_number) == 1234567812345678:
            print ("Ha-ha-ha.Now I will use your credit card!")



