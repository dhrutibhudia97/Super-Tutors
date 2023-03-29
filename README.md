# Super Tutors
[insert image of different screens on different devices...]

This project "Super Tutors" was to build a platform for teenagers to book sessions for science tuition. This allows the user to booking tuition sessions that take place at a tuition system in Wembley. They can book their sessions by choosing the tuition type, date and time. They can only book sessions that are available within the next two weeks and are unable to edit their appointments last minute (within 2 days of the appointment). The user able to booking, read, edit and cancel their booking sessions. The admin user is able to see all of the tuition books that have been made by the different users and is also able to edit and delete them.

## User Stories

### As a User
- [x] See the services available
- [x] See the location of the tutor
- [x] Submit a query and receive an email response
- [x] Create an account
- [x] Log in and Log out of my account
- [x] Book a tuition session
- [x] Cancel my tuition session
- [x] Edit my previously booked tuition session
- [ ] Only see my future booked sessions

### As an Admin User
- [x] Log in and Log out of my account
- [x] View all tuition sessions booked by all users
- [x] Edit other peoples tuition sessions
- [x] Delete other peoples tuition sessions
- [x] Receive queries that website viewers have submitted. They should receive an automated response.
- [ ] Only see the future sessions that are booked (not past sessions)

### Project Board

I used the project board on GitHub to help plan for this project and documented all user and admin stories as issues and added it to the board to help give structure to this project.

![projectboard](https://user-images.githubusercontent.com/107180641/228549958-cb9d1aa9-f1b0-4967-81c3-88ee13e0ece0.png)

 
## Testing 
1. User able to view the websites homepage and contact page without logging in.
2. User able to find location of the tuition centre using google maps
3. User able to send a query to the tutors through the submit your queries section and receive an automated reply.
4. User is able to sign up for an account
5. User able to log in to their existing account
6. User able to log out of their account.
7. User able to book a tuition session
8. User able to view the sessions they have booked
9. User able to Edit their tuition sessions (if it is not within the next 2 days)
10. User able to Delete their tuition sessions
11. User notified if they cannot book a session for a certain date or time.
12. Admin able to login in and access database
13. Admin able to see all users and bookings
14. Admin able to delete and edit anyones bookings


## Validators

CSS Validator
![css validator](https://user-images.githubusercontent.com/107180641/228589071-ce2a7b25-0375-4ebf-8d39-57e8c79b674e.png)

JavaScript Validator 
![javascript map validator](https://user-images.githubusercontent.com/107180641/228591567-678e8123-ba2a-4063-8f3d-70bed138b113.png)

![javascript emailjs validator](https://user-images.githubusercontent.com/107180641/228591683-2d93a6d2-e291-46e4-9f8b-ffea4616a53d.png)


Python Validator
![python validators merged](https://user-images.githubusercontent.com/107180641/228680256-17dce3c4-0468-408f-8721-f37fb175cedd.png)

HTML Validator
![html validator merged](https://user-images.githubusercontent.com/107180641/228687233-fa1e427e-98a3-403f-a43d-7b659c2735c9.png)


## Languages
- HTML
- CSS
- Javascript
- Python
- Django

## Technologies
- GitHub
- Gitpod
- Bootstrap
- Django
- Heroku
- ElephantSQL
- Font Awesome
- Google Maps
- Email.js
- HTML Validator - https://validator.w3.org/
- CSS Validator - https://jigsaw.w3.org/css-validator/
- Javascript Validator JShint - https://jshint.com/
- Code Institute Python Linter Validator - https://pep8ci.herokuapp.com/#
- https://www.pexels.com/ - photo credit


## Deployment


## Cloning


## Known Errors
- Issues about deployment. knowingly deployed with config vars "DISABLE_COLLECTSTATIC = 1" as CSS and javascript were not loading otherwise.
- Python validator 
  - Errors due to code line > 79, code put through formatter and some lines could not be shortened.
  - Error in views.py file, "!=" used instead of "is not" as a comparison as this raised a syntax error.
- HTML errors, mainly due to formatting of static files {% static css/stylesheet.css %}, but this is how you connect the files so nothing can be done.
- User issue, Even though you cannot edit your appointment within two days of the appointment, you can delete the appointment.


## Credits
- Code institute modules for the javascript functionality of the map and email.js
- Mentor Sandeep Aggarwal for help with the logic of the functions
- python str function - https://www.geeksforgeeks.org/python-strftime-function/  
- For help with the python logic of the booking app. - https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78




