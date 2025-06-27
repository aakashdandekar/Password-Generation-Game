#Module
import tkinter as tk
from rule import *
import string

#Rule Code
rule = [
        "Rule 1: Password must be at least 21 characters long.",
        "Rule 2: Password must contain at least one uppercase letter.",
        "Rule 3: Password must contain at least one lowercase letter.",
        "Rule 4: Password must contain at least one digit.",
        "Rule 5: Password must contain at least one special character (!@#$%^&*).",
        "Rule 6: Password must not contain any spaces.",
        "Rule 7: The password must not start or end with a digit.",
        "Rule 8: Password must contain no repeated characters.",
        "Rule 9: Password must be a palindrome (reads the same backward).",
        "Rule 10: The sum of all digits must be a prime number.",
        "Rule 11: Password must contain a vowel.",
        "Rule 12: The ASCII value of all characters must add up to a multiple of 100.",
        "Rule 13: Include a chemical element’s symbol (like 'Na', 'Fe', etc.).",
        "Rule 14: Include a Roman numeral representing the current hour.",
        "Rule 15: Include a two-letter country code (ISO 3166-1 alpha-2).",
        "Rule 16: The middle character must be a mathematical operator (+ - * /).",
        "Rule 17: Password must contain in atleast two numbers.",
        "Rule 18: The number of vowels must equal the number of digits.",
        "Rule 19: Initials of Core Avengers['TS', 'SR', 'NR', 'BB', 'TO', 'CB']"
    ]

click_count = 0
count = -1

def update_rules():
    update_btn.config(text='Enter')

    global click_count
    global count

    click_count+=1
    count+=1

    input_text = text_box.get("1.0", tk.END).strip()

    if click_count == 1:
        output_rule.config(text=f"{rule[count]}")
    
    elif click_count == 2:
        if rule1_twelve_char(input_text) == True:
            output_rule.config(text=f"{rule[count]}")
        
        else:
            output_rule.config(text='Error!' ,fg='red')

    elif click_count == 3:
        if rule2_upper_case(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!' ,fg='red')
    
    elif click_count == 4:
        if rule3_lower_case(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!' ,fg='red')

    elif click_count == 5:
        if rule4_one_digi(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!' ,fg='red')

    elif click_count == 6:
        if rule5_symbol(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!' ,fg='red')    

    elif click_count == 7:
        if rule6_nospace(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!' ,fg='red')

    elif click_count == 8:
        if rule7_fst_n_lst_digi(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 9:
        if rule8_no_repeat(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 10:
        if rule9_palindrome(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 11:
        if rule10_sum_digi(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 12:
        if rule11_spelled_back(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 13:
        if rule12_ASCII_val(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')
    
    elif click_count == 14:
        if rule13_chem_elem(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 15:
        if rule14_roman_num(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 16:
        if rule15_country_code(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 17:
        if rule16_math_op(input_text) == True:
            output_rule.config(text=f"{rule[count]}")

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 18:
        if rule17_atleast_two(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 19:
        if rule18_vowel_num(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')

    elif click_count == 20:
        if rule19_prime_sym(input_text) == True:
            output_rule.config(text=f'{rule[count]}')

        else:
            output_rule.config(text='Error!', fg='red')
        
        
#Main Body
root = tk.Tk()

root.title("Password Game")
root.geometry("1000x500")
root.resizable(True, True)

title_card = tk.Label(root, text='The Password Generation', font='Arial 25', fg='black')
title_card.pack(pady=(250, 0))

text_box = tk.Text(root, height=1, width=40, font='Arial 15')
text_box.pack(pady=(20,20))

update_btn = tk.Button(root, text="Play",height=2, width=20, command=update_rules)
update_btn.pack()

output_rule = tk.Label(root, height=1, width=75, font='Arial 10')
output_rule.pack(pady=10)

root.mainloop()