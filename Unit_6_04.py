# Created by: Khoa Le
# Created on December 5 2017
# Created for ICS3U
# This program shows the user's address.

from enum import Enum

street_type = Enum('Avenue', 'Boulevard', 'Crescent', 'Lane', 'Road')

print("Types of Streets: ")

for street_kinds in street_type:
    print(street_kinds)

print("")

Provinces = Enum('AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON','PE', 'QC', 'SK', 'YT')

print("Provinces: ")

for province_names in Provinces:
    print(province_names)

print("")

class MailAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type , city_name, province_initials, postal_code):
        
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province_initials = province_initials
        self.postal_code = postal_code

route_type = raw_input("Enter what type of street you live on: ")

if route_type not in street_type:
    route_type = raw_input("Invalid Street Type: ")
route_type = route_type

province_name = raw_input("Province (Enter in initials form. Example: ON) : ")

if province_name not in Provinces:
    province_name = raw_input("Invalid Province, make sure it's in initial form: ")
province_name = province_name

address_number = int(input("Enter your house number: "))

if address_number < 0:
    address_number = int(input("Invalid House Number: "))
address_number = address_number

mailing_address = MailAddress(raw_input("Enter your first name: "), raw_input("Enter your last name: "), address_number, raw_input("Enter your street name: "), route_type, raw_input("Enter your city name: "), province_name, raw_input("Enter your postal code: "))

print("\n" + mailing_address.first_name + " " + mailing_address.last_name + " " + str(mailing_address.house_number) + " " + mailing_address.street_name + " " + str(mailing_address.street_type) + " " + mailing_address.city_name + ", " + mailing_address.province_initials + " " + mailing_address.postal_code + " ")
