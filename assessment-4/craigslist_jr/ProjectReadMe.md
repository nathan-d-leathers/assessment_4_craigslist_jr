To Run this project:

-create venv (craigslist_venv)
-pip install -r requirements.txt 
-brew services start postgres
-create database called assessment_four
-check db by entering $ psql assessment_four
-make migrations if necessacary 
-python manage.py runserver

There are no API keys to worry about


Notes:

Approach:
-Created a scheme that should how our class models would flow throughout the product. 
-I then build a dummy json file with fake posts which I migrated into my db to populate my website
-I build out individual html templates to show how the url links would flow (home, home/categories, home/categories/edit, home/categories/category) until I reached an individual post. At each stage you could Create, Read, Update, & Delete both the categories, or individual posts within the categories as well as individual posts. 
-My views acted at paths to perform CRUD operations which called on Axios and JavaScript functions to update the data base and redirect the webpage when necessary.

Takeaways:
I learned a lot about modeling and databases through this assignment as well as how the Frontend talks to the Backend and vice versa. I also learned a lot about control flow of urls and how web pages should be structured into categories.

Things to Improve:
The site works perfectly as designed. I would possible add some authentication and remove the @csrf_exempt decorators, perhaps add some css to dress the site up a notch.