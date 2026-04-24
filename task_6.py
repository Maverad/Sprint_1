def delete_duplicates(data):
    clone_dict = data.copy()
    new_dict = {}
    already_used = set()
    for key, value in clone_dict.items():
        for ticket in range(len(value)):
            if len(new_dict) == 0:
                new_dict.update({key: [value[ticket]]})
                already_used.add(value[ticket])
            if value[ticket] not in already_used:
                if key not in new_dict:
                    new_dict.update({key: []})
                new_dict[key].append(value[ticket])
                already_used.add(value[ticket])
    return new_dict

def chain_tickets(types, tickets):
    tickets_dict = tickets.copy()
    types_dict = types.copy()
    tickets_dict = delete_duplicates(tickets_dict)
    tickets_by_type = {}
    for i in range(1, len(tickets_dict) + 1):
        tickets_by_type.update({types_dict[i]: tickets_dict[i]})
    return tickets_by_type

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 