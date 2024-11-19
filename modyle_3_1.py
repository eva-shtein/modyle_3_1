calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(argument_string):
    count_calls()
    dlina = len(argument_string)
    verhniy = argument_string.upper()
    nizhniy = argument_string.lower()
    return (dlina, verhniy, nizhniy)

def is_constains(argument_string, argument_list):
    count_calls()
    for i in argument_list:
        if str(i).upper() == argument_string.upper():
            return True
    return False

print(string_info("sTroka"))
print(is_constains('Capybara', ["capybara", 123] ))
print(calls)