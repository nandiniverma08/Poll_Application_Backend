

def filter_by_tags(polls_data, list_of_tags):
    filtered_data = []

    for poll_entry in polls_data:
        tags = poll_entry.get("Tags", [])

        # Check if any tag in the list_of_tags is present in the current entry's tags
        if any(tag.lower() in map(str.lower, tags) or tag.capitalize() in map(str.capitalize, tags) for tag in list_of_tags):
            filtered_data.append(poll_entry)

    return filtered_data