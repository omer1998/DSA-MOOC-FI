
def find_rule(char, state, rules): # retrun new_char new_state next_action // return false if no matching rule
    for rule in rules:
        if rule[0] == char and rule[1]==state:
            return rule
    return False

def check_input(symbs):
    
    for e in symbs[1:-1]:
        if e != "X":
            return False
    return True
def calculate(input, rules):
    """
    a robot is given a string as an input. The string consists of the symbols 0 and 1. 
    The robot processes the string according to a given set of rules, and either accepts it or rejects it.

    Before the robot starts processing the string, the symbol L is added to the beginning of the string 
    and the symbol R to the end of the string. 
    This way the robot knows the boundaries of the string. 
    For example, if the input is the string 0110, the robot receives it in the form L0110R.

    The robot starts the processing at the first position of the string containing the symbol L. 
    The initial state of the robot is 1.

    The robot processes the string according to a set of rules. 
    Each rule is activated when the robot is at a given symbol and in a given state. 
    ** As a result of the activation, the robot changes the symbol and its state, 
    and performs one of the following actions:

    LEFT: move one step to the left
    RIGHT: move one step to the right
    ACCEPT: accept the input
    REJECT: reject the input


    
    For example, the rule ("0", 2, "X", 4, "RIGHT") means that when the robot is at a symbol 0 and in the state 2, 
    it changes the symbol into X and the state into 4, and then moves one step to the right.

    -> Each symbol in the rules is 0, 1 or a letter in the range A–Z. 
    -> Each state of the robot is an integer in the range 1–100. 
    -> Each combination of a symbol and a state activates at most one rule. 
    
    # If at any point, the robot moves outside the input string,
    # or cannot find any matching rule, the robot rejects the input.
    
    It is possible that the robot gets stuck in an infinite loop, and never accepts or rejects the input. To avoid this, if the robot has not accepted or rejected the input after one thousand actions, the robot aborts the processing and rejects the input.
    
    The purpose of this set of rules is that the robot accepts the input string if it contains the same number of the symbols 0 and 1. 
    The robot scans the input multiple times, moving alternately left to right and right to left. In each pass from left to right, the robot replaces one 0 symbol with X and one 1 symbol with X. If all symbols get replaced with X, the robot accepts the input.
    """

    string = "L"+ input +"R"
    string = [i for i in string]
    state = 1
    index = 0
    count = 0
    while count < 1000:
        count+=1
        # if check_input(new_syb_state):
        #     return True
        
        count+=1
        symb = string[index]
        rule = find_rule(str(symb), int(state), rules)
        if (rule):
            new_symb = rule[2]
            new_state = rule[3]
            next_action = rule[4]
            string[index] = new_symb
            state = new_state
            if next_action == "RIGHT":
                if  index + 1 >= len(string):
                    return False
                index+= 1
            elif  next_action == "LEFT":
                if  index - 1 < 0:
                    return False
                index -=1
            elif next_action == "ACCEPT":
                return True
            elif next_action == "REJECT":
                return False
            
        else:
            return False
    return False


if __name__ == "__main__":
    rules = []
    


    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False


    # print(calculate("01", rules))