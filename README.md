# disclaimer
I, Sadman Kabir, am only responsible for the Registration Page of the frontend. (and the pixel art of our wonderful school mascot Rhett)

# registration-magic
Automate BU Registration


## Running the project

Open the flutter app and run the backend server.

Flutter
- open the built app available for Windows, Android, or iOS -- for developement, install Flutter and build main.dart, using `flutter pub get` to get dependencies

Backend
- `cd backend`
- `py main.py`
See `backend\README.md` for more details on running the backend server

## Project Structure

parenthesis = optional

- Flutter frontend
  - Ability to search for and add courses, stored locally (or to a server)
  - Ability to schedule registration (when does your registration open?)
  - Ability to send this data to the backend
  - (User login page)
- Python backend
  - Ability to send requests from backend to Student Link to make the registration requests
  - Storing all SelectIt IDs for every course
    - web scraping
    - ** can scrape from value token of the input tag defining the checkbox TL;DR use the checkbox to get SelectIt info **
- (Firebase database, or MongoDB -- can decide later for storing user data through authentication)

