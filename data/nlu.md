## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- Goodbye
- Nothing thank you

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [Lesser than Rs. 300](price_range)
- [Rs. 300 to 700](price_range)
- [More than 700](price_range)
- [Mexican](cuisine) restaurant in [Mumbai](location)
- [LessThan300](price_range)
- [Mexican](cuisine) Restro in [China](cuisine)[]{"entity": "location", "value": "China"}
- Find a restaurant in [Mumbai](location) then
- Find me a [chinese](cuisine) restaurant in [Delhi](location)
- [MoreThan700](price_range)
- [Mexican](cuisine) restro in [Delhi](location)
- [Mexican](cuisine) in [Bhutan](location)
- Chnage the city to [Delhi](location)

## intent:send_email
- Yes, My email address is [namratabafna14@gmail.com](cust_email)
- Yup, My email-id is [deepakgupta0021@gmail.com](cust_email)
- My mail address is [mlengineernamrata@gmail.com](cust_email)
- abc@gmail.com
- abc123@gmail.com
- My email id is [namratabafna14@gmail.com](cust_email)
- Yes it's [namratabafna14@gmail.com](cust_email)
- Three00To700
- Yes please send it on [deepakgupta0021@gmail.com](cust_email)
- Please send it to [deepakgupta0021@gmail.com](cust_email)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:cust_email
- ^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
