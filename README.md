This is a python backend project of a Riddle Game.

The authentication is done with sqlalchemy and using this tutorial as a reference model.
https://pythonspot.com/login-authentication-with-flask/

The riddles are stored in a json file and download from https://riddle.solutions/

To install:
1. Install Flask
2. Install SQLAlchemy library
3. Run tabledef.py to setup the database
4. run riddle_server.py to run the application
5. (Optionally) run riddletest.py to test the application

TESTING:
I used a build it yourself testing suite I developed from the material in byotest.py. To build the tests, I started with the requirements of the application. I wanted to develop the functionality of the riddles. So, I designed my tests with this in mind. I firstly wanted a way to load the riddles from a file and then proceed to test if a riddle answer by the user was true or not, so I made that the first challenge. I decided a way to implement this test case was to get some riddles and place them in a json file, as json is a good structure to contain the riddles in. Then, I implemented retrieving a specific riddle and testing the answer against the user given answer, case insensitive. My second challenge was user authentication and for this I decided to use a database, to store the user information like username and password as well as that users correct answer score. I wrote tests to ensure that users could be added, retrieved and deleted. All tests work as expected. I went further and tested the functionality of the web application using manual steps.
Here are some further tests to do manually:

1. Testing the Register functionality
    a. Run the application
    b. Go to the login page
    c. Enter a new username and password
        i. If succeeded go to login page redirect and check your new name against leaderboard
        ii. If not succeeded read explanation why and redirect back to login page

2. Testing the Login functionality
    a. Follow steps in 1. to create a username
    b. On login page attempt to login with username and password provided.
    c. Attempt to login using a fake username or / and fake password and see if it works

3. Testing the Logout functionality
    a. Follow steps above to login.
    b. Go to the riddle page when you login and click logout.
    c. This should logout and redirect back to login page again.

3. Testing the Riddles
    a. Login to the System using your username and password.
    b. Test a Riddle against its matching answer in the riddles.json file
    c. Add a wrong answer and test if the riddle works against wrong answers

4. Testing the leaderboard
    a. Login to System and test no. 3 a few times and keep track of right answers.
    b. Hit Logout to go to Login page
    c. The leaderboard should display the right number of answers you got








