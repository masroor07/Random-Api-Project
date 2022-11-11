# Random-Api-Project

<h4>1. Write a program to GET random data of an user and write it in a File named
users.csv. Each GET request must have an interval time of 1 second and append the
information in a comma separated format. You can use any open source mock rest
api endpoints available on the internet or use Random Data API
(https://random-data-api.com/documentation). </h4>

<b>Soloution: </b>"main.py" is the module, I have used to fetch random user data using the Random Data API and have saved the the records in users.csv. I first convert the fetched data to json and then populate the json data to an empty array, which i use to load records into the csv filetitled as "users.csv".
We use "requests" library to make GET requestes to connect and retrieve data from the server. We also use "csv" to manipulate the the in csv files.


<h5>A. Write a program to read users.csv and create users-sorted.csv by applying
sorting algorithm on firstName / Name / Username (Field of your choice
based on your dataset)</h5>

<b>Soloution: </b> I have used pandas library to make it easy to sort the data we just fetched using the Random data API. We store the data into "usersSorted.csv". The "sort.py" module performs the following task..

<h5>B. Write a program to Input Id or Username of an user and return the details of
that user in the output of the program</h5>

<b>Soloution: </b> We just iterate throught the excel sheet and the data field we will be taking from the user is the person's "First Name". The program is in the module "sort.py" 

Trial case: 

1. You can run the module main.py to fetch the random records using the Random Api and the program will store the data into users.csv.
2. To verify, you can check the data in the csv file.
3. Try sorting the csv file by using the sort.py module. The program sorts the records according to their first names.
4. To perofrm the search operation, we can run search.py. The program will prompt you to enter a users id and will return the user record if the user with that id is pressent in the sheet.

The outputs of the program are in the following csv files:
1. The fetched data: "users.csv"
2. Sorted CSV: "usersSorted.csv"
