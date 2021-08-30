## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_price_range_send_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "Rs. 300 to 700"}
    - slot{"price_range": "Three00To700"}    
    - action_search_restaurants
    - utter_ask_email
* send_email{"cust_email":"Yes on mlengineernamrata@gmail.com"}
    - slot{"cust_email": "mlengineernamrata@gmail.com"}
    - action_send_mail
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - utter_ask_price_range
* restaurant_search{"price_range": "LessThan300"}
    - slot{"price_range": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_price_range
* restaurant_search{"price_range": "LessThan300"}
    - slot{"price_range": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price_range": "LessThan300"}

* restaurant_search{"cuisine": "China", "location": "China"}
    - slot{"cuisine": "China"}
    - slot{"location": "China"}
    - utter_ask_price_range
* restaurant_search{"price_range": "LessThan300"}
    - slot{"price_range": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "China"}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_price_range
* send_email
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "China"}
    - slot{"price_range": "LessThan300"}
    - action_slot_reset
    - reset_slots
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - utter_ask_price_range
* restaurant_search{"price_range": "MoreThan700"}
    - slot{"price_range": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email
* send_email{"cust_email": "deepakgupta0021@gmail.com"}
    - slot{"cust_email": "deepakgupta0021@gmail.com"}
    - action_send_mail
    - slot{"cust_email": "deepakgupta0021@gmail.com"}
    - action_slot_reset
    - reset_slots
* restaurant_search{"cuisine": "Mexican", "location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Delhi"}
    - utter_ask_price_range
* restaurant_search{"price_range": "MoreThan700"}
    - slot{"price_range": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price_range": "MoreThan700"}

* restaurant_search{"cuisine": "Mexican", "location": "Bhutan"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Bhutan"}
    - utter_ask_price_range
* restaurant_search{"price_range": "MoreThan700"}
    - slot{"price_range": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Bhutan"}
    - action_search_restaurants
    - slot{"location": "Bhutan"}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_price_range
* restaurant_search{"price_range": "MoreThan700"}
    - slot{"price_range": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price_range": "MoreThan700"}
    - utter_ask_email
* send_email{"cust_email": "deepakgupta0021@gmail.com"}
    - slot{"cust_email": "deepakgupta0021@gmail.com"}
    - action_send_mail
    - slot{"cust_email": "deepakgupta0021@gmail.com"}
    - action_slot_reset
    - reset_slots
    - utter_ask_howcanhelp
    - utter_ask_howcanhelp
* affirm
* goodbye
