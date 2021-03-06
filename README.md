# Ticket View

# Description
This python program will display 100 of your tickets from your Zendesk account. It will be run on the command line of either Mac or Windows operating systems. To run the Ticket Viewer program, download the file ticketview.py. 

# Note 
{Edit} My subdomain does not work anymore for testing. 
It is restricted to accessing the subdomain https://schong.zendesk.com only. To access your own domain, you would have to modify the url in ticketview.py to represent the subdomain you want to access (ex. https://{your-subdomain}.zendesk.com/api/v2/tickets.json). You would also need to modify the credentials needed, such as email or password.

# Setup
Python is needed to run the program. If you don't have python installed, visit https://www.python.org/downloads/ and download the latest version. Run it to install on your computer. 

Save the file in a directory that you want to work from as you will need to connect to the directory in the terminal or command prompt in order to run it. 

# Instructions
1. Open up your terminal and make sure you are connected to the directory where ticketview.py is located. To change directories use the command cd. 

    Ex. if ticketview.py is in a folder called projects that's on your desktop, type cd desktop/projects on the command line to connect to the projects folder. 

    For Windows, use '\\' instead of '/' Ex. cd desktop\projects. 

2. Type in the command 'python ticketview.py' without the single quotes. It should tell you the domain you are signing into and prompt for an email. If it says "No such file is found," double check if you are in the directory where ticketview.py is located.

3. Type in email. It will then prompt you for a password.

4. Enter the password.

5. Wait as it will process the credentials and display the ticket data on the terminal window. The data will also be saved in a txt file called 'tickets.txt' and will be displayed in notepad as well once the program is finished.   

# Conclusion
I will include sample output of the program labeled as 'sample tests.txt.' It contains output of the program from test runs and what happens if a different email or password other than the ones I listed on this document was entered. If the wrong credentials are entered, it will simply return an error with the request.
