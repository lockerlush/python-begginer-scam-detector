#choosing purchase type
print("choose purchase type")
print("1 food/drinks")
print("2 ride/entretaiment")
print("3 service(example: taxi or car ride app)")
choice_purchase = input("choose a number: ")


#choosing country development level


print("choose country developement level: ")
print("1 developed country")
print("2 developing country")
choice_country = input("choose developement level: ")
#if elif and else statments to check and 
# calclulate the final price and determine if its a
#scam or a genuinine price


if choice_purchase == "1" and choice_country == "1":
     print("you bought something to eat in a developed country")
elif choice_purchase == "2" and choice_country == "1":
	print("you bought a ride or entretaiment in a developed country")
elif choice_purchase == "3" and choice_country == "1":
	print("you bought services in a developed country")
elif choice_purchase =="1" and choice_country == "2":
	print("you food or drinks in a developing country")
elif choice_purchase =="2" and choice_country =="2":
	print("you got bought entretaiment in a developing country")
elif choice_purchase == "3" and choice_country == "2":
	print("you bought a service in a developing country")
if choice_purchase == "1":
    purchase_type = input("click enter to continue: ")
elif choice_purchase == "2":
    purchase_type  = input("click enter to continue: ")
elif choice_purchase == "3":
    purchase_type = input("click enter to continue: ")
print(purchase_type)
#calculations to check if a scam


amount_payed = int(input("input cost: "))
if amount_payed <= 100 and choice_purchase == "1":
    print("the purchase is safe to make,you may eat")
    print("thank you for using scam detector")
elif amount_payed <= 120 and choice_purchase =="2":
    print("you may choose a service to help you")
    print("thank you for using scam detector")
elif amount_payed <= 150 and choice_purchase =="3":
    print("you may take a ride as for the price is cheap")
    print("thank you for using scam detector")
else:
    print("danger!!!!")
    print("be wary as this may be a scam ")
    print("thank you for using scam detector")
#rating system


print("would you like to print my app?")
choice_rate =input("yes or no: ")
if choice_rate == "yes":
    print("nice thanks")
    print("what would you rate it out of 10?")
    think = input("type what you think: ")
    if think == "10":
        print("wow!! 10 thanks this is still a begginer project")
    elif think == "9":
        print("thanks 9 is really solid")
    elif think == "8":
        print("thanks for 8")
    elif think == "7":
        print("thanks for 7")
    elif think == "6":
        print("thanks for 6")
    elif think == "5":
        print("not bad or good, thanks")
    elif think == "4":
        print("4, i should improve")
    elif think =="3":
        print("3,i should improve")
    elif think == "2":
        print("2,i should improve")
    elif think == "1":
        print("1,i should really improve")
    elif think == "0":
        print("hey now 0 really dont be harsh i am doing my best")
    else:
        print("you need to input 1-10")
elif choice_rate == "no":
    print("understandable dont want to waste time")
else:
    print("type yes or no jessus")