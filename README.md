# Pantry Pal
This website was designed for Techpoint's S.O.S Challenge.  
It has three use cases; one for Food Banks, Donors, and Customers.  
### Food Banks
To create an account hit the 'Create an Account' button on the home page. Fill out the form to create an account. Once you are logged in you may use the 'Update Inventory' page to track inventory. On this page you can also find the button 'Send Notification to Donors', press this and fill out the form to automatically send an email to those that have signed up for notifications.  
When you are signed you can also hit the 'Edit Pantry' button in the top right corner to edit your pantry's name, address, website, hours, or needs.  
### Donors / Customers
As a donor or user use the Find a Pantry page to view all registered pantries. You may also see inventory for pantries if they have made this information public. Submit your Zip Code into the form to sort pantries by distance. To sign up for notifications for any pantry hit the 'Sign up' button and fill out the form. You will be automatically emailed when the selected pantry sends notifications out.  
## Installation (Ubuntu)
Hosting a website is best done on a virtual machine to keep your packages separate.  
First check what version of python you currently have with  
`python --version`  
If you do not have python 3 installed run the following commands  
`sudo apt update`  
`sudo apt install python3.8`  
Next we need to install and create a new virtual machine. If you run into errors you may need to enable virtualization in your machine's BIOS settings.  
`sudo apt-get install python3-venv`  
We are going to create a new machine named newenv  
`python3 -m venv newenv`  
Start the machine with  
`source newenv/bin/activate`  
Next we need to install our packages onto the newenv machine  
`pip3 install django django-crispy-forms django-filter mysqlclient`  
Now cd into the TechpointSOS directory and run the following command to start the server  
`python manage.py runserver`  
You can now access the website at `http://127.0.0.1:8000/`  
