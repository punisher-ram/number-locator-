import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+447415911585")
phone_number2 = phonenumbers.parse("+14844760153")
phone_number3 = phonenumbers.parse("+971 55 818 5468")

print("\nphone numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));

#lets go


