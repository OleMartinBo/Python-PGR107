import random


from bitarray import test

linebreak = "--------------------------"

choice = ["\n\nPress 1 for costumer service.",
            "\nPress 2 to speak with an agent.",
            "\nPress 3 to show FAQ.",
            "\nPress 4 to exit.\n"]

cs = ["\nPress 1 for account", 
      "\nPress 2 to show your subscription",
      "\nPress 3 for other",
      "\nPress 4 to exit"]

response = ["Hello, how are you?",
            "How can i help you?",
            "Hi, i'm chatbot. How can i be of service?"]

list = [response[0] + choice[0] + choice[1] + choice[2] + choice[3],
        response[1] + choice[0] + choice[1] + choice[2] + choice[3], 
         response[2] + choice[0] + choice[1] + choice[2] + choice[3]]

def display_costumer_service(): 
    print(cs[0] + cs[1] + cs[2] + cs[3])
    
    
while True:
    userInput = input("You: ")
    
    if userInput.lower() == "goodbye":
        
        print("Chatbot: Goodbye!")
        break
    
    else:
        print("Chatbot: " + random.choice(list))
        
        userInput = input("You: ")
        
        if userInput == "1":
            print("Chatbot: You chose costumer service.\n\nHello, tell us what we can help you with! ")
            display_costumer_service()
        
        elif userInput == "2":
            print("Chatbot: You chose to speak with an agent, please hold...")
        
        elif userInput == "3":
            print("Chatbot: You chose to show your subscription.")
        
        elif userInput == "4":
            print("Chatbot: You chose to exit. Have a nice day!")
            break
        
        else:
            print("Something went wrong.")
            
            
    
