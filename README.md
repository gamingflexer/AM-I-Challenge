# AM-I-Challenge

Development of a Mobile App using which the end-user can, by pressing a button submit his/her current location (latitude and longitude) to a backend server located at the Security Section.  At the back-end, on receipt of this latitude and longitude (query location) along with the time, the feeds of all the cameras at increasing distances from the query location must be made available for viewing through a select menu.  The deadline for the demonstration of this App, both front-end and back-end, will be scheduled in the first week of December 2022. 

# Path to the project

- App with Login Feature with Firebase Authentication
- App with a button to submit the current location and time to the "Firebase"
- Flask Server take data and use google map api to find information about the location [Basic Info and Distances between 2 points]
- Get the camera cordinates nearest to the person by calculating the distance between the person and the camera
- Use the camera feed using flask server and start calculating the distance between the person and each camera
- Web App to show the camera feed and the distance with the menu to select the camera feed


# Api Endpoints

- login - Firebase Authentication
- \Get the current location and time after pressing the button ["Beta" keep 1 user id]
    - Preprocessing the data and applying the google map api to get the basic info about the location
    - Get the camera cordinates nearest to the person by calculating the distance between the person and the camera
    - Save relaveant data to the firebase [Nearst_camera, cordinates, distance, time, location]
- \POST Web for a user
    - Display the user name on Web Page 
    - Display the camera feed and the distance with the menu to select the camera feed
