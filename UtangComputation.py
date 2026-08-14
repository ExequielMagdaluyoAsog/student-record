
##############Dudu's Debt####################################
Dunkin_coffee = 95
Dunkin_coffee_and_donut = 135
Payment_to_ate_jovy = 500
Nespresso = 1215
Dinner_at_Shokudo = 1000
Grab_Jollibee_Chickenjoy= 237
Share_on_Borro_lunch = 1500
Coffee_at_Landers = 66
Landers_male_shampoo= 450
Mercury_drug = 1552
Gym_membership= 1000
Keanys_gift = 270
Pancake_House = 104
Paotsin = 145
Buko = 50
Grab_for_Blakes = 1642
Cash = 500

Dudu = Dunkin_coffee+Dunkin_coffee_and_donut+Payment_to_ate_jovy+Nespresso+Dinner_at_Shokudo+Grab_Jollibee_Chickenjoy \
+Share_on_Borro_lunch+Coffee_at_Landers+Landers_male_shampoo+Mercury_drug+ \
Gym_membership+Keanys_gift+Pancake_House+Paotsin+Buko+Grab_for_Blakes+Cash
print('#####################################')
print('Dudu\'s Debt = ' + str(Dudu))

################Bubu's Debt#################################
Pataya_tip = 50
Kuya_ice_cream_parking_etc = 250
Balot = 50
Load = 59
Horton_coffee = 190
Horton_coffee2 = 190
Cash = 600
Cash2 = 200

Bubu = Pataya_tip+Kuya_ice_cream_parking_etc+Balot+Load+Horton_coffee+Horton_coffee2+Cash+Cash2
Minus = Dudu - Bubu

print('Bubu\'s Debt = -' + str(Bubu))
print('            =  ' + str(Minus))
print('#####################################')
################CF paid by DUDU##################################
wifi = 1625
Massage = 2340
Keannys_bday_celeb = 3500
Saging = 115
Tita_paz = 3000
Gardenia_kamatis = 85
Turon_ = 126
Turon = 36
Saging2 = 130
Breakfast = 310
Cash = 2800

CF_Paid_Dudu = (wifi+Massage+Keannys_bday_celeb+Saging+Tita_paz+Gardenia_kamatis+ \
               Turon_+Turon+Saging2+Breakfast+Cash)/2

print('Paid by Dudu = ' + str(CF_Paid_Dudu))

################CF paid by BUBU##################################
Grocery_paid_by_bubu = 3782.3
Market_paid_by_bubu = 573
Berocca_paid_by_bubu = 1180
Grocery_paid_by_bubu_2 = 5222.01
Meals_at_Landers = 765.14
Electric_bill_paid_by_bubu = 1214
Feb_rent_paid_by_bubu = 10000
Grab_for_tita_paz_paid_by_bubu = 565
Tita_paz_transpo = 500
Grocery = 2482.42
Hazelnut_Syrup_SB = 250
Chooks_to_go = 170
Xevera_veggies = 40
Pampang = 1719
Hypermarket = 1317
Berocca = 3540
Grocery_2 = 698
Chooks_to_go_2 = 325
Tokyo_tokyo = 701.43
Hypermarket2 = 1037

CF_Paid_Bubu = (Grocery_paid_by_bubu+Market_paid_by_bubu+Berocca_paid_by_bubu+Grocery_paid_by_bubu_2+ \
Meals_at_Landers+Electric_bill_paid_by_bubu+Feb_rent_paid_by_bubu+Grab_for_tita_paz_paid_by_bubu+ \
Tita_paz_transpo+Grocery+Hazelnut_Syrup_SB+Chooks_to_go+Xevera_veggies+ \
Pampang+Hypermarket+Berocca+Grocery_2+Chooks_to_go_2+Tokyo_tokyo+Hypermarket2)/2
MinusCF = CF_Paid_Bubu - CF_Paid_Dudu

print('Paid by Bubu = ' + str(CF_Paid_Bubu))
print('             = ' + str(MinusCF))
print('\n')
print(Minus + MinusCF)
print('#####################################')







































