# Riddle Game

This is a python backend project of a Riddle Game. The Riddle game allows a user to login, and then the riddle game proceeds to ask the user riddles. For each riddle the user gets right, he gets a score. The score is stored against his username, should he want to continue at a later date. The riddle game allows multiple users to run the game simultaneously.
 
## UX
 
 I designed some wireframes on paper to how the web site should look, and then transferred them digitally using the app Pencil. I wanted the interface to be as simple as possible, as this was a backend project.

- A user should be able to login and register a new username and password. That functionality and display is illustrated on the intro UX wireframe in the UX folder.
- A user should also be able to view the current leaderboard. That functionalty is also illustrated in the intro UX wireframe.
- A user is asked one question at a time and is given a form to submit the answer. Once the answer is submitted, it is acknowledged and indicated whether it is right or wrong.  This is illustrated in the question UX wireframe.
- A user is able to view his score in the header at any time and is illustrated in the question UX wireframe.

## Features

 
### Existing Features
- User can register a new username and password
- User can login using existing username and password
- Their score is persisted for them, should they want to continue at a later date
- There are 100 riddles for the user to explore

### Features Left to Implement
- Another feature would be the support for riddles including different kinds of media, like images or videos.

## Technologies Used

- [Flask] (http://flask.pocoo.org/)
    - The project uses flask, a backend python framework
- [Flask-Login] (https://flask-login.readthedocs.io/en/latest/)
    - The authentication is done with sqlalchemy and using this tutorial as a reference model.
   
- [Bootstrap 4] (https://getbootstrap.com/)
    - Used for responsiveness

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

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

## Deployment

To install:
1. Install Flask and Flash-Login
2. Install SQLAlchemy library
3. Run tabledef.py to setup the database
4. run riddle_server.py to run the application
5. (Optionally) run riddletest.py to test the application


Heroku Deployment: https://riddleproj.herokuapp.com


## Credits

### Content

The riddles are stored in a json file and downloaded from https://riddle.solutions/


### Acknowledgements

-  https://pythonspot.com/login-authentication-with-flask/ for help with login library


















