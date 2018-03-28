import sys
card_number = input("Please enter card number:")
mm_yy = input("Please enter mm/yy:" )
CVV = input ("Please enter CVV:" )
mm_yy1 == int(mm_yy)
try:
    var = mm_yy1 == int(mm_yy)
except: #ValueError:
    print ("OK")
if len(card_number) != 16:
    sys.exit(1)
if len(CVV)  < 3:
    sys.exit("Error!!!")
if int(card_number) == 1234567812345678:
            print ("Ha-ha-ha.Now I will use your credit card!")



