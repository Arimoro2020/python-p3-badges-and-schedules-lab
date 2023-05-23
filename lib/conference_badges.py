

def badge_maker(name):
    f_string = f"Hello, my name is {name}."
    return f_string

def batch_badge_creator(names):
    badges = [f"Hello, my name is {name}." for name in names]
    return badges

def assign_rooms(names):
    room_list =[]
    for name in names:
        name_index = (names.index(name)) + 1
        f_string = f"Hello, {name}! You'll be assigned to room {name_index}!"
        room_list.append(f_string)
    return room_list

def printer(names):
    badge_result = batch_badge_creator(names)
    for result in badge_result:
        print(result)
    room_results = assign_rooms(names)
    for room_result in room_results:
        print(room_result)
    
