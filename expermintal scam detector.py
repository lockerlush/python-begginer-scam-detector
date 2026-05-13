print("choose purchase type")
print("1 food/drinks")
print("2 ride/entretaiment")
print("3 service(example: taxi or car ride app)")
choice_purchase = input("choose a number: ")
print("choose country developement level: ")
print("1 developed country")
print("2 developing country")
choice_country = input("choose developement level: ")
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
