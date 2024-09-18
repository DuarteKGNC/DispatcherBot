from .tickets import standard_ticket, non_dinfo_ticket
import csv
import io

def get_priority(priority):
    if priority.lower() == 'l':
        return "P3 :large_green_circle:"
    if priority.lower() == 'm':
        return "P2 :large_orange_circle:"
    elif priority.lower() == 'h':
        return "P1 :red_circle:"
    elif priority.lower() == 'inic':
        return ":alert: INCIDENT :alert:"
    else:
        return "Informative :information_source:"


def clean_debug_info(debug_info):
    links = {"view_link": "", "normal_link":"", "logrocket":""}
    user = ""
    v = ""
    info = ""
    filtered = debug_info.split("\n")[:-1]
    for index, i in enumerate(filtered):
        if index == 0:
            links["view_link"] = i.split(" ")[-1]
        elif index == 1:
            links['normal_link'] = i.split(" ")[-1]
        elif index == 2:
            user = i.split(" ")[0]
        elif index == 3:
            info = i
        elif index == 4:
            links['logrocket'] = i.split(" ")[-1]
        elif index == len(filtered)-1:
            v = i.split(" ")[-1]
    return links, user, v, info


def ticket_skeleton(data, goalkeeper, support_channel_id):
    priority = get_priority(data['author_name']['priority'])
    links = user = version = info = None
    if data['fields']['debug_info']:
        links, user, version, info = clean_debug_info(data["fields"]["debug_info"])
    steps_to_reproduce = ""
    for index, i in enumerate(data["fields"]["how_to_reproduce"]):
        steps_to_reproduce+=f"*{index + 1}*. {i}\n"
    debug_info_checker = [links, user, version, info]
    if None in debug_info_checker:
        ticket = non_dinfo_ticket(support_channel_id, data, priority, steps_to_reproduce, goalkeeper)
    else:
        ticket = standard_ticket(support_channel_id, data, priority, steps_to_reproduce, links, user, info, version, goalkeeper, debug_info=data['fields']['debug_info'])
    return ticket

def clean_csv(file):
    decoded_file = file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = csv.DictReader(io_string)
    csv_data_list = list(reader)
    csv_data = csv_data_list[0]
    ticket_id = csv_data['Ticket ID']
    ticket_name = csv_data["Ticket name"].split("-")[-1]
    ticket_description = csv_data["Ticket description"]
    debug_info = csv_data["Debug_Info"]
    return ticket_id, ticket_name, ticket_description, debug_info