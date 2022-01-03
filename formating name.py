# formating name using function

def name_formating(first_name,last_name):
    if first_name =="" or last_name=="":
        return "you don't provide valid input"
    formated_first_name=first_name.title()
    formated_last_name=last_name.title()
    return (f"you name is {formated_first_name} {formated_last_name}")

print(name_formating(input("What is your first name? "),input("What is your last name? ")))
