# HotZone

Models:
There are two models in the project.
1.	Location is the model to store every GeoData location(s) added by user after searching.
2.	Search Result is the model to temporarily store a single GeoData location searched by the user. When the search is done successfully and the app waits for user to decide to add it to HotZone database or not, the Search Result instance will be created. Once the user has decided (no matter add it or not), the instance will be deleted, so that every time before a new search is performed, there is no instance of Search Result in the database. 

Website Access:
‘/’: To get the list of all GeoData location(s) added to HotZone database
‘/admin’: To log in as an admin
‘/find’: To search a GeoData location
‘/results’: To view the result of search of location name according to the user’s input
‘/save’: To receive a confirmation message of adding the result of search successfully to HotZone database

Limitation:
The user cannot delete a case or change the details of a case after addition.
