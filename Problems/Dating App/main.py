def select_dates(potential_dates):
    names = []
    for item in potential_dates:
        if item["age"] > 30 and "art" in item["hobbies"] and item["city"] == "Berlin":
            names.append(item["name"])
    return ', '.join(names)
