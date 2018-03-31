list_card = []
list_date = []
while True:
        card_number = input("Enter card number: ")
        list_card = card_number.split(" ")
        if len(list(list_card)) == 4:
            try:
                list_card0 = int(list_card[0])
                list_card1 = int(list_card[1])
                list_card2 = int(list_card[2])
                list_card3 = int(list_card[3])
                if len(list_card[0]) == 4 and len(list_card[1]) == 4 and \
                        len(list_card[2]) == 4 and len(list_card[3]) == 4:
                    if list_card[0] == '5167':
                        print("You use PrivatBank credit card")
                        break
                    if list_card[0] == '5375':
                        print("You use Monobank credit card")
                        break
                    if list_card[0] != '5375' and list_card[0] != '5167':
                        print("You use credit card from the unknown bank")
                        break
            except ValueError:
                print("")
while True:
    date_number = input("Enter mm/yy: ")
    list_date = date_number.split("/")
    if len(list_date) == 2:
        try:
            list_date0 = int(list_date[0])
            list_date1 = int(list_date[1])
            print(list(list_date))
            if int(list_date[0]) >= 0 and int(list_date[0]) <= 12 and int(list_date[1]) > 18:
                break
        except ValueError:
            print("Try again")
while True:
    CVV_number = input("Enter CVV number: ")
    if len(CVV_number) == 3:
        break
print("Good job!!!")