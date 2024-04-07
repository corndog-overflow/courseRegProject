# disclaimer
I was responsible for the frontend of the application.

## Building the project
To build this project you must have python and flutter installed on your system. To run the project go to the ui folder and type the command:

-   $flutter run lib/main.dart

(The backend is in Python, an interpreted language, so no building is required)

## Running the project

Open the flutter app and run the backend server.

Flutter
- open the built app available for Windows, Android, or iOS -- for developement, install Flutter and build main.dart, using `flutter pub get` to get dependencies

Backend
- `cd backend`
- `py main.py` or `nohup py main.py &`
See `backend\README.md` for more details on running the backend server

## Project Structure

### Frontend
Built in Flutter
  - User login page
  - Can search for and add courses, stored locally
  - Schedules registration, sent to Flask API on backend
### Backend
Built in Python with Flask to receive API info
  - Ability to send requests from backend to Student Link to make the registration requests
    - User, Semester, Course data structures and url param generator functions defined in `user.py` and `courses.py`
   - API using Flask
    - Async scheduler and Flask server in `main.py`
  - Storing all SelectIt IDs for every course
    - Course database handled via `coursedb.py`
    - Web scraping via Selenium
      - Scrapes from the value token of the input tag defining the checkbox i.e. we use the checkbox to get SelectIt info

## Application Demo
-   https://www.youtube.com/watch?v=ln91Cqp5xLY

## Team Members
-   Nathan Clark: nbclark@bu.edu
-   Sadman Kabir: kabirs@bu.edu
-   Oluwaseun Angelo Soyannwo: seun@bu.edu
-   Peter West: flibble@bu.edu
-   Cynthia Young: mcyoung@bu.edu
