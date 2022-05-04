'''Zodiac sign -- server'''

from Socket import create_new_socket




HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():


    with create_new_socket() as s:
        s.bind(HOST, PORT)
        s.listen()
        print("Provide your month of birth zodiac sign server started. Listening on", (HOST, PORT))

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            while True:
                birthday = conn.recv()
                dob= birthday.split(',')
                

                # checking first of all whether given date of birth makes sense
                # the length of dob should 2 only
                # if dob has a possible month do so more
                # however, before executing everything check whether days of the month make sense
                # if month or days don't make sense inform the user to put in the correct info

                if len(dob) != 2:
                    sign_traits= ("Date of birth should be in format month, day (e.g: January, 01) only ")
                    conn.sendall(sign_traits) 
                # print(f"dob[0] ={dob[0]}")
                elif dob[0] == "january" or dob[0] == "february" or dob[0] == "march" or dob[0] == "april" or dob[0] == "may" or dob[0] == "june" or dob[0] == "july" or dob[0] == "august" or dob[0] == "september" or dob[0] == "october" or dob[0] == "november" or dob[0] == "december":
                     # check  if days are integers number and greater than 1 before doing an more work
                    if type(int(dob[1]))== int and int(dob[1]) >=0:
                            if  dob[0] == "january":
                                if int((dob)[1]) < 32:
                                # print(int((dob)[1]))
                                    if int((dob)[1]) < 20:
                                        zodiac_sign= "Capricorn"
                                        # print(zodiac_sign)
                                        with open('zodiacsignscharacters.txt') as my_text:
                                            
                                            the_line= my_text.read()
                                            # looking for * in the text
                                
                                            character= the_line.split('*')
                                                    
                                            # searching for Capricorn
                                            sign_traits= character[12]
                                        conn.sendall(sign_traits)                     
                                                  
                                    else:
                                        zodiac_sign= "Aquarius"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                             
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                
                                                character= the_line.split('*')
                                                    # searching for Aquarius
                                                sign_traits= character[1]
                                        conn.sendall(sign_traits)        
            
                                else:
                                    sign_traits= ("Days in January should be no more than 31: ")
                                    conn.sendall(sign_traits)
                                    
                                        
                                    
                                    
                            elif dob[0]  == "february":
                                if int((dob)[1]) < 30:
                                    if int((dob)[1]) < 19:
                                
                                        zodiac_sign= "Aquarius" 
                                        with open('zodiacsignscharacters.txt') as my_text:
                                           
                                            the_line= my_text.read()
                                            # looking for * in the text
                                        
                                            character= the_line.split('*')
                                                    # searching for Aquarius
                                            sign_traits= character[1]
                                        conn.sendall(sign_traits)           
                                       
                                    else: 
                                        zodiac_sign= "Pisces"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                             
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Pisces
                                                sign_traits= character[2]
                                        conn.sendall(sign_traits)
                                        # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in February should be no more than 29"
                                    conn.sendall(sign_traits)
                                    
                            elif dob[0] =="march":
                                if int((dob)[1]) < 32:
                                    if int((dob)[1])< 21:
                                        zodiac_sign= "Pisces"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                
                                                character= the_line.split('*')
                                                    # searching for Pisces
                                                sign_traits= character[2]
                                        conn.sendall(sign_traits)        
                                                # else:
                                                #     break
                                        # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Aries"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Aries
                                                sign_traits= character[3]
                                        conn.sendall(sign_traits)        
                                                # else:
                                                #     break
                                        # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in March should be no more than 31"
                                    conn.sendall(sign_traits)
                                    
                            elif dob[0]  == "april":
                                if int((dob)[1]) < 31:
                                    if int((dob)[1]) < 20:
                                        zodiac_sign= "Aries"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                            
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Aries
                                                sign_traits= character[3]
                                        conn.sendall(sign_traits)        
                                                # else:
                                                #     break
                                        # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Taurus"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Taurius
                                                sign_traits= character[4]
                                        conn.sendall(sign_traits)        
                                                # else:
                                                #     break
                                        # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in April should be no more than 30"
                                    conn.sendall(sign_traits)
                            elif dob[0] == "may":
                                if int((dob)[1]) < 32:
                                    if int((dob)[1]) < 21:
                                        zodiac_sign= "Taurus"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Taurius
                                                sign_traits= character[4]
                                        conn.sendall(sign_traits)        
                                            # else:
                                            #     break
                                        # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Gemini"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Gemini
                                                sign_traits= character[5]
                                        conn.sendall(sign_traits)        
                                                # else:
                                                #     break
                                            # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in May should be no more than 31"
                                    conn.sendall(sign_traits)
                            elif dob[0]  == "june":
                                if int((dob)[1]) < 31:
                                    if int((dob)[0])< 21:
                                        zodiac_sign= "Gemini"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                            # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Gemini
                                                sign_traits= character[5]
                                        conn.sendall(sign_traits)        
                                                # else:
                                                #     break
                                            # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Cancer"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.read()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Cancer
                                                    sign_traits= character[6]
                                        conn.sendall(sign_traits)        
                                                    # else:
                                                    #     break
                    
                                            # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in June should be no more than 30"
                                    conn.sendall(sign_traits)
                                    
                            elif dob[0]  == "july":
                                if int((dob)[1]) < 32:
                                    
                                    if int((dob)[1]) < 23:
                                        zodiac_sign= "Cancer"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.read()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Cancer
                                                    sign_traits= character[6]
                                        conn.sendall(sign_traits)        
                                                    # else:
                                                #     break
                                        # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Leo"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.readline()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Leo
                                                    sign_traits= character[7]
                                        conn.sendall(sign_traits)        
                                                    # else:
                                                    #     break
                                            # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in July should be no more than 30"
                                    conn.sendall(sign_traits)
                                    
                            elif dob[0]  == "august":
                                if int((dob)[1]) < 32:
                                    if int((dob)[1]) < 23:
                                        zodiac_sign= "Leo"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.read()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Leo
                                                    sign_traits= character[7]
                                        conn.sendall(sign_traits) 
                                            # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Virgo"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.read()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Virgo
                                                    sign_traits= character[8]
                                        conn.sendall(sign_traits) 
                                            # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in September should be no more than 30"
                                    conn.sendall(sign_traits)
                                    
                            elif dob[0] == "september":
                                if int((dob)[1]) < 31:
                                    if int((dob)[1]) < 23:
                                        zodiac_sign= "Virgo"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.readline()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Virgo
                                                    sign_traits= character[8]
                                        conn.sendall(sign_traits) 
                                            # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Libra"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.read()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                # searching for Libra
                                                    sign_traits= character[9]
                                        conn.sendall(sign_traits) 
                                            # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in September should be no more than 30"
                                    conn.sendall(sign_traits)
                                    
                            elif dob[0] == "october":
                                if int((dob)[1]) < 31:
                                    if int((dob)[1]) < 23:
                                        zodiac_sign= "Libra"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.read()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Libra
                                                    sign_traits= character[9]
                                        conn.sendall(sign_traits) 
                                            # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Scorpio"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                    the_line= my_text.read()
                                                # looking for * in the text
                                                    character= the_line.split('*')
                                                        # searching for Scorpio
                                                    sign_traits= character[10]
                                        conn.sendall(sign_traits) 
                                            # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in October should be no more than 31"
                                    conn.sendall(sign_traits)
            
                            elif dob[0] == "november":
                                if int((dob)[1]) < 31:
                                    if int((dob)[1]) < 22:
                                        zodiac_sign= "Scorpio"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                                    # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Scorpio
                                                sign_traits= character[10]
                                        conn.sendall(sign_traits)
                                            # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Sagittarius"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                                    # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Sagittarius 
                                                sign_traits= character[11]
                                        conn.sendall(sign_traits)
                                        # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in November should be no more than 30"
                                    conn.sendall(sign_traits)
                                    
                            elif dob[0] == "december":
                                if int((dob)[1])< 32:
                                    if int((dob)[1])< 22:
                                        zodiac_sign= "Sagittarius"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                                    # looking for * in the text
                                                character= the_line.split('*')
                                                    # searching for Sagittarius 
                                                sign_traits= character[11]
                                        conn.sendall(sign_traits)
                                            # conn.sendall(zodiac_sign)
                                    else:
                                        zodiac_sign= "Capricorn"
                                        with open('zodiacsignscharacters.txt') as my_text:
                                                the_line= my_text.read()
                                                    # looking for * in the text
                                        
                                                character= the_line.split('*')
                                                    # searching for Capricon 
                                                sign_traits= character[12]
                                        conn.sendall(sign_traits)
                                            # conn.sendall(zodiac_sign)
                                else:
                                    sign_traits= "Days in December should be no more than 31"
                                    conn.sendall(sign_traits)
                                    
                                    
                            else:               
                                break
                        # else:
                        #     sign_traits= "days should be positive integer numbers like 1,2,10,..."
                        #     conn.sendall(sign_traits)
                            
                    else:
                        sign_traits= "days should be positive integer numbers like 1,2,10,..."
                        conn.sendall(sign_traits)
                else:
                    sign_traits= "months should be january, february, march, april, may, june, july, august, september, october, november, and december"
                    conn.sendall(sign_traits)
            print('Disconnected')

if __name__ == '__main__':
    main()
