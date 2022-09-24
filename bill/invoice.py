def invoice(name,phone_no,BID,RID,Seats_required,Time):
    print("-"*78)
    print("|                          Personal details                                  |")
    print("-"*78)
    print("|             Name               |        Phno.                              |")
    print("-"*78)
    n=len("             Name               ")
    pn=len("        Phno.                              ")
    print("|"+name+(" "*int(n-len(name)))+"|"+phone_no+(" "*int(pn-len(phone_no)))+"|")
    print("-"*78)
    print("|     Booking details                                                        |")
    print("-"*78)
    print("|      BID      |      RID       |      Seats_Required      |      Time      |")
    print("-"*78)
    b=len("      BID      ")
    r=len("      RID       ")
    s=len("      Seats_Required      ")
    t=len("      Time      ")
    print("|"+BID+(" "*int(b-len(BID)))+"|"+RID+(" "*int(r-len(RID)))+"|"+Seats_required+(" "*int(s-len(Seats_required)))+"|"+Time+(" "*int(t-len(Time)))+"|")
    print("-"*78)
#Note that all the arguments must be strings
#Note that this is a void function,so never put in print
#invoice("hrithvikshakatshali","1","2","3","4","5")  
#It should be like x=select  ....... raghav from that databse should come  and then subsequently u enter in the function
#Dont think about the logic,its of no use to think so  
    
    
def dinvoice(name,phone_no,DID,RID,area):
    print("-"*78)
    print("|                         Personal details                                   |")
    print("-"*78)
    print("|             Name               |                  Phno.                    |")
    print("-"*78)
    n=len("             Name               ")
    pn=len("        Phno.                              ")
    print("|"+name+(" "*int(n-len(name)))+"|"+phone_no+(" "*int(pn-len(phone_no)))+"|")
    print("-"*78)
    print("|                         Booking details                                    |")
    print("-"*78)
    print("|      DID      |      RID       |                    Area                   |")
    print("-"*78)
    b=len("      BID      ")
    r=len("      RID       ")
    a=len("                    Area                   ")

    print("|"+DID+(" "*int(b-len(DID)))+"|"+RID+(" "*int(r-len(RID)))+"|"+area+(" "*int(a-len(area)))+"|")          
    print("-"*78)
#Note that all the arguments must be strings
#Note that this is a void function,so never put in print

#It should be like x=select  ....... raghav from that databse should come  and then subsequently u enter in the function
#Dont think about the logic,its of no use to think so  
#This is the delivery invoice so its name is dinvoice