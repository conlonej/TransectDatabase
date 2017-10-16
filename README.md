# TransectDatabase

In this Django project, manage.py configures the interface for commands made from the Terminal, the TransectDatabase folder contains a file where settings for the app are specified (settings.py) and urls.py, which organizes the webpage structure for the project.

The dbViz folder contains most of the code for the app itself. models.py contains a schema for all tables within the database (not finished yet), urls.py organizes web pages within the app, and views.py provides a framework to organize the front-end of the app. admin.py, apps.py, and tests.py are not heavily used at the moment but will be expanded upon later. The migrations folder contains bookkeeping information about migrations from the app to the mySQL database.
