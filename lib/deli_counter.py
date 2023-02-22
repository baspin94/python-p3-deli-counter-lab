""" import ipdb """

katz_deli = []

def line(katz_deli):
    line_readout = "The line is currently:"
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        for i in range(1, len(katz_deli) + 1):
            index = i - 1
            line_readout += f" {i}. {katz_deli[index]}"
        print(line_readout)

def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    person_index = katz_deli.index(new_person) + 1
    print(f"Welcome, {new_person}. You are number {person_index} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print ("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)

    # i = len(katz_deli)
    # while i > 0:
    #     head_of_line = katz_deli.pop(0)
    #     print(f"Currently serving {head_of_line}.")
    #     i -= 1
    

""" ipdb.set_trace() """