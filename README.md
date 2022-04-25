# URLs Shortener API

Django REST API which allows you to post a link and create it's shortened equivalent in the db.

In order to create new record in the db please send POST request to the http://127.0.0.1:8000/api
endpoint and provide the url you want to shorten as 'url' in the header. 

In order to see all the URL's stored in the db send GET request to http://127.0.0.1:8000/api

If you are looking for some specific URL or it's shortened version please provide it as a parameter
while sending the GET request.  