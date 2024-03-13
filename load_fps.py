from pprint import pprint

def load_fps(filepath):
    poll_data = []

    with open(filepath, 'r') as file:
        lines = file.readlines()

        # Skip the header line if present
        if lines[0].startswith("Questions :: Options :: Votes :: Tags"):
            lines = lines[1:]

        for line in lines:
            # Split the line into Question, Options, Votes, and Tags
            data = line.strip().split(" :: ")

            # Print the data for debugging
            # print("Current Data:", data)

            # Check if the line has enough parts
            if len(data) != 4:
                print(f"Skipping line due to insufficient parts: {line}")
                continue

            # Extracting individual components
            question = data[0]
            options = data[1].split(" | ")

            # Handle the case where the third part contains non-numeric characters
            votes_str = data[2].split(" | ")
            votes = [int(vote) if vote.isdigit() else vote for vote in votes_str]

            tags = data[3].split(" | ")

            # Create a dictionary for the current question
            question_dict = {
                "Question": question,
                "OptionVote": dict(zip(options, votes)),
                "Tags": tags
            }

            # Append the dictionary to the list
            poll_data.append(question_dict)

    return poll_data

# Example usage:
filepath = 'polldata.fps'
result = load_fps(filepath)
pprint(result)



from pprint import pprint
from load_fps2 import filter_by_tags 
from load_fps3 import view_poll
from load_fps4 import update_poll
from load_fps5 import save_poll

def load_fps(filepath):
    poll_data = []

    with open(filepath, 'r') as file:
        lines = file.readlines()

        # Skip the header line if present
        if lines[0].startswith("Questions :: Options :: Votes :: Tags"):
            lines = lines[1:]

        for line in lines:
            # Split the line into Question, Options, Votes, and Tags
            data = line.strip().split(" :: ")

            # Check if the line has enough parts
            if len(data) != 4:
                print(f"Skipping line due to insufficient parts: {line}")
                continue

            # Extracting individual components
            question = data[0]
            options = data[1].split(" | ")
            votes_str = data[2].split(" | ")
            votes = [int(vote) if vote.isdigit() else vote for vote in votes_str]
            tags = data[3].split(" | ")

            # Create a dictionary for the current question
            question_dict = {
                "Question": question,
                "OptionVote": dict(zip(options, votes)),
                "Tags": tags
            }

            # Append the dictionary to the list
            poll_data.append(question_dict)

    return poll_data

# Example usage:
if __name__ == "__main__":
    filepath = 'polldata.fps'
    updated_filepath = 'updated_polldata.fps'

    # Load initial data
    polls_data = load_fps(filepath)
    

    # filtered_result = filter_by_tags(polls_data, ["phones", "cricket"])
    # pprint(filtered_result)

    # poll_number = 4 # Replace with the desired poll number
    # view_poll(polls_data, poll_number)

    
    polls_data = update_poll(polls_data, 4, "puma")
    polls_data = update_poll(polls_data, 4, "reebok")
    polls_data = update_poll(polls_data, 3, "C++")
    polls_data = update_poll(polls_data, 6, "Bekal Fort")

    # Print the updated data
    # pprint(polls_data)


    # Save the modified data to a new file
    # save_poll(polls_data, updated_filepath)




