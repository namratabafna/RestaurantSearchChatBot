from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rasa_sdk.events import AllSlotsReset

ZomatoData = pd.read_csv("zomato.csv", encoding="cp1252")
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = [
    "New Delhi",
    "Gurgaon",
    "Noida",
    "Faridabad",
    "Allahabad",
    "Bhubaneshwar",
    "Mangalore",
    "Mumbai",
    "Ranchi",
    "Patna",
    "Mysore",
    "Aurangabad",
    "Amritsar",
    "Puducherry",
    "Varanasi",
    "Nagpur",
    "Vadodara",
    "Dehradun",
    "Vizag",
    "Agra",
    "Ludhiana",
    "Kanpur",
    "Lucknow",
    "Surat",
    "Kochi",
    "Indore",
    "Ahmedabad",
    "Coimbatore",
    "Chennai",
    "Guwahati",
    "Jaipur",
    "Hyderabad",
    "Bangalore",
    "Nashik",
    "Pune",
    "Kolkata",
    "Bhopal",
    "Goa",
    "Chandigarh",
    "Ghaziabad",
    "Ooty",
    "Gangtok",
    "Shimla",
]


def RestaurantSearch(City, Cuisine, PriceRange):

    if PriceRange == "LessThan300":
        print("PriceRange ", PriceRange)
        # Price Range Lesser than Rs. 300
        TEMP = ZomatoData[
            (ZomatoData["Cuisines"].apply(lambda x: Cuisine.lower() in x.lower()))
            & (ZomatoData["City"].apply(lambda x: City.lower() in x.lower()))
            & ZomatoData["Average Cost for two"].between(0, 299)
        ]

    elif PriceRange == "Three00To700":
        print("PriceRange ", PriceRange)
        # Price is between 300 and 700
        TEMP = ZomatoData[
            (ZomatoData["Cuisines"].apply(lambda x: Cuisine.lower() in x.lower()))
            & (ZomatoData["City"].apply(lambda x: City.lower() in x.lower()))
            & ZomatoData["Average Cost for two"].between(300, 700)
        ]
    elif PriceRange == "MoreThan700":
        print("PriceRange ", PriceRange)
        # Price is greater than 700
        TEMP = ZomatoData[
            (ZomatoData["Cuisines"].apply(lambda x: Cuisine.lower() in x.lower()))
            & (ZomatoData["City"].apply(lambda x: City.lower() in x.lower()))
            & (ZomatoData["Average Cost for two"] > 700)
        ]
    else:
        # Price is not specified
        TEMP = ZomatoData[
            (ZomatoData["Cuisines"].apply(lambda x: Cuisine.lower() in x.lower()))
            & (ZomatoData["City"].apply(lambda x: City.lower() in x.lower()))
        ]
    # Sort by Rating
    TEMP = TEMP.sort_values("Aggregate rating", ascending=False)
    return TEMP[
        ["Restaurant Name", "Address", "Average Cost for two", "Aggregate rating"]
    ]


class ActionSearchRestaurants(Action):
    def name(self):
        return "action_search_restaurants"

    def run(self, dispatcher, tracker, domain):
        print("Action Search Restaurant is excecuting..")
        loc = tracker.get_slot("location")

        # Check if Zomato operates in specified location
        loc_exists = len(ZomatoData[ZomatoData["City"].str.contains(loc)]) > 0
        if loc_exists == False:
            print("Location exists ", loc_exists)
            dispatcher.utter_message(
                "-----Sorry, we don’t operate in this city. Can you please specify some other location"
            )
            return [SlotSet("location", loc)]
        cuisine = tracker.get_slot("cuisine")
        price_range = tracker.get_slot("price_range")
        results = RestaurantSearch(City=loc, Cuisine=cuisine, PriceRange=price_range)
        global response
        response = ""
        if results.shape[0] == 0:
            response = "Sorry! There are no restaurants matching the search criteria"
        else:
            response = response + f"-----Found {len(results)} restaurants----- \n"
            response = response + f"-----Showing Top 10 matching results----- \n"
            for restaurant in results.iloc[:10].iterrows():
                restaurant = restaurant[1]
                response = (
                    response
                    + f"{restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two'] } \n"
                    + f"**Rating {restaurant['Aggregate rating']} \n\n"
                )

        dispatcher.utter_message("-----" + response)
        return [
            SlotSet("location", loc),
            SlotSet("cuisine", cuisine),
            SlotSet("price_range", price_range),
        ]


class ActionSendMail(Action):
    def name(self):
        return "action_send_mail"

    def run(self, dispatcher, tracker, domain):
        receiver_address = tracker.get_slot("cust_email")
        if receiver_address:
            print("email ", receiver_address)
            try:
                print("Mail Content ", response)
                mail_content = response
                sender_address = "namratabafna14@gmail.com"
                sender_pass = ""
                print("Setup account")
                # Setup the MIME
                message = MIMEMultipart()
                message["From"] = sender_address
                message["To"] = receiver_address
                message[
                    "Subject"
                ] = "Here are the details of the top restaurants from Zomato search - Upgrad"  # The subject line
                # The body and the attachments for the mail
                message.attach(MIMEText(mail_content, "plain"))
                # Create SMTP session for sending the mail
                session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
                session.starttls()  # enable security
                session.login(
                    sender_address, sender_pass
                )  # login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                print("Mail sent successfully to - ", receiver_address)
                dispatcher.utter_message(
                    "-----Mail sent successfully to - ", receiver_address
                )
            except Exception as e:
                dispatcher.utter_message(
                    "-----Failed email sending to - ", receiver_address
                )
                print("Failed to send an email to ", receiver_address)
                print(e)
        else:
            dispatcher.utter_message("-----You will not receive an email")
        return [SlotSet("cust_email", receiver_address)]


class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]
