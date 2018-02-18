import requests
import webbrowser

#****************************************
#function prints tickets in the terminal
#****************************************
def print_tickets_on_terminal():
    #keeps track of ticket number
    count = 0

    #format and display contents of the tickets into file
    for ticket in ticket_list:
        count += 1
        print('\nTicket', count, '\n')
        print('Subject:', ticket['subject'], '\n')
        print('Description:', ticket['description'], '\n')
        print('Tags:', ticket['tags'], '\n')

#*******************************************************************
# function writes ticket data into a txt file for easier readability
#*******************************************************************
def create_txt_file():
    #keeps track of ticket number
    count = 0

    #create text file to save and display tickets
    f = open('tickets.txt', 'w')

    #create text file to save and display tickets
    for ticket in ticket_list:
        count += 1
        f.write('\n\nTicket ' + str(count) + '\n')
        f.write('\nSubject: ' + str(ticket['subject']) + '\n')
        f.write('\nDescription: ' + str(ticket['description']) + '\n')
        f.write('\nTags: ' + str(ticket['tags']) + '\n')
    
    f.close()

#***********************************************
# functions that ask for credentials
#***********************************************
def ask_email():
    return input('Enter email: ')

def ask_pwd():
    return input('Enter password: ')

#**************************
#beginning of main program
#**************************
url = 'https://schong.zendesk.com/api/v2/tickets.json'

print('\nYou are signing into https://schong.zendesk.com \n')

#ask user for credentials
user = ask_email()
pwd = ask_pwd()

#HTTP get request
response = requests.get(url, auth=(user, pwd))

#print error if not successful
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

#decode json response and store in python dictionary data
data = response.json() 

#iterate the 100 tickets and display them
ticket_list = data['tickets']

#display ticket data on terminal
print_tickets_on_terminal()

#ticket data will be stored in tickets.txt 
create_txt_file()

print("Data has been saved to the file 'tickets.txt' and will be opened in notepad.")
print('The file should be located in your current working directory.')

#opens txt file in notepad
webbrowser.open('tickets.txt', new=2)

