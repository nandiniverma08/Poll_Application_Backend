def update_poll(polls_data, pollNumber, optionName):
    # Check if the pollNumber is valid
    if 1 <= pollNumber <= len(polls_data):      
        index = pollNumber - 1   
        if optionName in polls_data[index]["OptionVote"]:
    
            polls_data[index]["OptionVote"][optionName] += 1
            print(f"Vote for {optionName} in poll {pollNumber} incremented.")
        else:
            print(f"Option {optionName} not found in poll {pollNumber}.")
    else:
        print(f"Invalid poll number: {pollNumber}")

    return polls_data