# Django

```bash
pip install Django==4.0.5
```
```bash
https://docs.djangoproject.com/en/4.0/
https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
```
# ![image](https://user-images.githubusercontent.com/87818153/174537745-a81d83aa-20c0-4781-9749-3c7c8209bac5.png)
## Django is a free and open source web application framework witten in python,
## Django offers a big collection of mocules which you can use in your own projects.

** 2003 − Started by Adrian Holovaty and Simon Willison as an internal project at the Lawrence Journal-World newspaper.

** 2005 − Released July 2005 and named it Django, after the jazz guitarist Django Reinhardt.

## MVC, MVT
* Both are software design pattern
##  MVC : Model View Controller

![image](https://user-images.githubusercontent.com/87818153/174538441-dd3f0488-e7a2-4545-ac5b-12deefda35da.png)

 
* Model : The model is responsible for managing the data of the application. It responds to the request from the view and it also responds to instructions from the controller to update itself But, it contains no logic describing how to present the data to a user.

* View : The View deals with how the data will be displayed to the user and provides various data representation components. View tells how the user data will be presented.

* Controller : The Controller manipulates the Model and renders the view by acting as a bridge between both of them. MVC has controller that drives both Model and View.

## MVT : Model View Template

![image](https://user-images.githubusercontent.com/87818153/174537697-940f7d24-88e6-4bf9-b208-29b038dd19d4.png)

 * Model : it helps to handle database. It is a data access layer, which contains the required fields and behaviors of the data you’re storing. There’s hardly an application without a database. A model is a Python class, and it does not know anything about other Django layers.  Models help developers to create, read, update, and delete objects (CRUD operations) in the original database. Also, they hold business logic, custom methods, properties, and other things related to data manipulation.

 * View : it is used to execute the business logic and interact with a model to carry data and renders a template. Views for receiving HTTP request and returning HTTP response.

 * Template : it is a presentation layer that handles the User Interface part completely. These are files with HTML code, which is used to render data. The contents of these files can be static or dynamic. A template is used only to present data since there’s no business logic in it.

* The main difference between the two patterns is that Django itself takes care of the Controller part (Software Code that controls the interactions between the Model and View), leaving us with the template. The template is an HTML file mixed with Django Template Language (DTL).

![image](https://user-images.githubusercontent.com/87818153/174538761-70ea7354-15fa-4fbb-a725-f52ef3aa1ac6.png)















