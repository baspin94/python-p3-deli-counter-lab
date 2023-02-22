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

def take_a_number():
    pass

def now_serving():
    pass

""" ipdb.set_trace() """