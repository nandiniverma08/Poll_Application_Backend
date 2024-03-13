def save_poll(polls_data, filepath):
    with open(filepath, 'w') as file:
        # Write the header line
        file.write("Questions :: Options :: Votes :: Tags\n")

        # Iterate through each poll in polls_data
        for poll in polls_data:
            # Write the data for each poll
            file.write(f"{poll['Question']} :: ")
            
            # Write options
            options_str = " | ".join(poll['OptionVote'].keys())
            file.write(f"{options_str} :: ")

            # Write votes
            votes_str = " | ".join(str(vote) for vote in poll['OptionVote'].values())
            file.write(f"{votes_str} :: ")

            # Write tags
            tags_str = " | ".join(poll['Tags'])
            file.write(f"{tags_str}\n")

    print(f"Poll data saved to {filepath}")