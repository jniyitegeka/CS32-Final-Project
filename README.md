CS32-Final-Project

My CS32 final project

This directory contains everything about my CS32 final project.

Project: Creating people's Zodiac signs and their meaning identifier.

Socket.py, Check.py: Scripts we will use to create socket and eliminate errors any errors in our scripts for building the efficient networked signs'identifier. To execute this step I utlilised The Socket32.py and Check32.py from CS32 PSET 2.

Server.py: This file contains the scripts we will use to build the server. 

Our server.py will have scripts for connection( Socket& bind); list of zodiac signs,etc; listening the client.py scripts ;receiving information from the client scripts in terms of Dates or signs and compare the received information to our saved list of possible responses; sending the response to the client scripts; receiving (closing) message from the client script; closing scripts.

Client.py: This file contains the scripts we will use to build the client. 

Our client.py will have scripts for connection(Socket); prompting the user to input information scripts to be sent to the server; receiving back information from the server scripts; printing out \whatever message the client recieved scripts; closing scripts.

Goal for My CS32 final project

**Steps:

creating socket to connect client and the server

Creating client.py that prints to the user something like:

    >python3 client.py
    
    ###Know your Zodiac Sign###
    input your birth: mm/dd


Sending the input to the server which will return the following information, which will be printed on the users screen

    ###Know your Zodiac Sign###  
    Input your birthday: mm/dd
       Zodiac sign: Cancer
       Traits:
             1. Strengths: Persuasive,...
             2. Weakness: optimistic,...
             3. Cancer likes: soccer,...
             4. Cancer dislikes: heights,...
       Known people with this sign: Solange Knowlewless,...
**Note:** If the user input a birthday with a decimal number such january, 11.1 the server won't produce any results because we can't change a string floating number into an integer number.
