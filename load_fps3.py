def view_poll(polls_data, poll_number):
    # Check if the poll_number is within the valid range
    if 1 <= poll_number <= len(polls_data):
        poll_entry = polls_data[poll_number - 1]
        question = poll_entry["Question"]
        option_votes = poll_entry["OptionVote"]
        tags = poll_entry["Tags"]

        # Display the question
        print(question)
        
        # Display options and votes
        for option, vote in option_votes.items():
            print(f"* {option}: {vote}")

        # Display tags
        print("\nTags:", ", ".join(tags))
    else:
        print(f"Invalid poll number. Please choose a number between 1 and {len(polls_data)}.")
