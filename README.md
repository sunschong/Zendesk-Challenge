# Ticket View

# Description
This python program will display 100 of your tickets from your Zendesk account. It will be run on the command line of either Mac or Windows operating systems. To run the Ticket Viewer program, download the file ticketview.py. 

# Note 
It is restricted to accessing the subdomain https://schong.zendesk.com only. To access your own domain, you would have to modify the url in ticketview.py to represent the subdomain you want to access (ex. https://{your-subdomain}.zendesk.com/api/v2/tickets.json). You would also need to modify the credentials needed, such as email, password, and/or API key.

# Setup
Python is needed to run the program. If you don't have python installed, visit https://www.python.org/downloads/ and download the latest version.

Save the file in a directory that you want to work from as you will need to connect to the directory in the terminal or command prompt in order to run it. 

# Instructions
1. Open up your terminal and make sure you are connected to the directory where ticketview.py is located. To change directories use the command cd. 

    Ex. if ticketview.py is in a folder called projects that's on your desktop, type cd desktop/projects to connect to the projects folder. 

    For Windows, use '\\' instead of '/' Ex. cd desktop\projects. 

2. Type in the command 'python ticketview.py' without the single quotes. It should tell you the domain you are signing into and prompt for an email. If it says "No such file is found," double check if you are in the directory where ticketview.py is located.

3. Type in 'sunshinechong@gmail.com.' It will then ask if you have an API token key. If you want to use the key, type y, and copy and paste this key: CCrC62RYbGfKsYFUkObKuR6aALgkhETP87yv244B. If you want to use the password, type n. Skip to step 5 if using API key.

4. Enter the password: zendeskchallenge

5. Wait as it will process the credentials and display the ticket data. The data will also be saved in a txt file called 'tickets.txt' and will be displayed in notepad once the program is finished.   

# Conclusion
I will include sample output of the program labeled as 'sample tests.txt.' It contains output of the program from test runs and what happens if a different email, password, or API key other than the ones I listed on this document was entered. If the wrong credentials are entered, it will simply return an error with the request.
