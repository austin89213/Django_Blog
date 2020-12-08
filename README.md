# Description:
A Django Blog built with basic CRUD, Asynchronous and D3.js

# Functions:
- User:
  - Register
  - Login
  - Admin Links (For superuer only)
- Posts:
  - Make a Post(Login required)
  - Edit and Delet(User must be the author of the post)
  - Record the times posts viewd
  - The "Analysis" button would show the related chart drawed by D3.js
- Comments:
  - Leave comments under posts
  - Author will be the user (anonymous if not logged in)
  - Asynchronous (comments will show after adding without refreshing the page)
- NAVBAR:
  - Link of the current path will be darker to improve user experience

# Tech & Tools
- Backend:
   - Django (2.1.7) (https://www.djangoproject.com/)
- Frontend:
   - Bootstrap (4) (https://getbootstrap.com/)
   - jQuery (3.5) (https://jquery.com/)
   - D3.js (6.2) (https://d3js.org/)

# To use:
- 1. Run git clone https://github.com/austin89213/Django_Blog in terminal / cmd to stroe or download the file
- 2. Create an venv with Python 3 and Django 2.1.7
- 3. Run terminal / cmd and cd to the directory
- 4. Run python manage.py createsuperuser for the logging in
- 5. Run python manage.py runserver
- 6. Open the url provided (http://127.0.0.1:8000/)
