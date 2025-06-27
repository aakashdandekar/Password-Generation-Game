#Modules
import re

#Rule1
def rule1_twelve_char(string):
    try:
        if len(string) == 21:
            return True
    
    except:
        return False
    
#Rule2
def rule2_upper_case(string):
    try:
        i = 0
        
        if rule1_twelve_char(string) == True:
            for i in range(len(string)):
                if string[i].isupper() == True:
                    return True
                
                else:
                    i += 1
                    continue

    except:
        return False
    
#Rule3
def rule3_lower_case(string):
    try:
        i = 0

        if rule2_upper_case(string) == True:
            for i in range(len(string)):
                if string[i].islower() == True:
                    return True
                
                else:
                    i+=1
                    continue
            
    except:
        return False
    
#Rule4
def rule4_one_digi(string):
    try:
        i = 0
        if rule3_lower_case(string) == True:
            for i in range(len(string)):
                if string[i].isalnum() == True:
                    return True
                
                else:
                    i+=1
                    continue
        
    except:
        return False
    
#Rule5
def rule5_symbol(string):
    sym = '!@#$%^&*'

    try:
        if rule4_one_digi(string) == True:
            for char in sym:
                for elem in string:
                    if char == elem:
                        return True
                
                    else:
                        continue

    except:
        return False
    
#Rule6
def rule6_nospace(string):
    try:
        i = 0

        if rule5_symbol(string) == True:
            for i in range(len(string)):
                if string[i] == ' ':
                    i += 0
                    
            if i == (len(string) - 1):
                return True
                    
    except:
        return False
    
#Rule7
def rule7_fst_n_lst_digi(string):
    try:
        if rule6_nospace(string) == True:
            if string[0].isalnum() == True and string[11].isalnum() == True:
                return True
            
    except:
        return False
    
#Rule8
def rule8_no_repeat(string):
    try:
        i = 0
        j = 0

        if rule7_fst_n_lst_digi(string) == True:
            for i in range(len(string)):
                for j in range(len(string)):
                    if string[i] != string[j]:
                        return True
                    
                    else:
                        j += 1
                        continue
                i += 1

    except:
        return False
    
#Rule9
def rule9_palindrome(string):
    try:
        if rule8_no_repeat(string) == True:
            if string == string[::-1]:
                return True
            
    except:
        return False
    
#Rule10
def rule10_sum_digi(string):
    try:
        if rule9_palindrome(string) == True:
            return True #Incomplete
        
    except:
        return False

#Rule11
def rule11_spelled_back(string):
    try:
        if rule10_sum_digi(string) == True:
            vowel = 'aeiouAEIOU'
            i = 0
            j = 0

            for i in range(len(string)):
                for j in range(len(vowel)):
                    if string[i] == vowel[j]:
                        return True
                    
                    else:
                        j += 1
                        continue
                i += 1
        
    except:
        return False
    
#Rule12
def rule12_ASCII_val(string):
    try:
        if rule11_spelled_back(string):
            return True #Incomplete
        
    except:
        return False
    
#Rule13
def rule13_chem_elem(string):
    try:
        if rule12_ASCII_val(string):
            i = 0
            lst_elem = [
                'H',  'He', 'Li', 'Be', 'B',  'C',  'N',  'O',  'F',  'Ne',
                'Na', 'Mg', 'Al', 'Si', 'P',  'S',  'Cl', 'Ar', 'K',  'Ca',
                'Sc', 'Ti', 'V',  'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',  'Zr',
                'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
                'Sb', 'Te', 'I',  'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
                'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
                'Lu', 'Hf', 'Ta', 'W',  'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
                'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                'Pa', 'U',  'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
                'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
                'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'
            ]

            for i in range(len(lst_elem)):
                if lst_elem[i] in string:
                    return True
                
                else:
                    i += 1
                    continue

    except:
        return False
    
#Rule14
def rule14_roman_num(string):
    try:
        pattern = r'\bM{0,3}(CM|CD|D?C{0,3})' \
              r'(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b'
    
        matches = re.findall(pattern, string, re.IGNORECASE)

        return True
    
    except:
        return False
    
#Rule15
def rule15_country_code(string):
    try:    
        country_codes = [
            'US', 'GB', 'CN', 'FR', 'IN', 'RU', 'DE', 'BR', 'JP', 'IT',
            'AU', 'CA', 'MX', 'KR', 'ES', 'TR', 'NL', 'CH', 'SE', 'BE',
            'NO', 'FI', 'DK', 'PL', 'CZ', 'ZA', 'EG', 'NG', 'AR', 'CO',
            'CL', 'PE', 'VE', 'MY', 'TH', 'PH', 'SG', 'ID', 'VN', 'UA',
            'IL', 'SA', 'AE', 'NZ', 'IE', 'PT', 'AT', 'HU', 'GR', 'RO',
            'HR', 'SK', 'SI', 'BG', 'RS', 'LT', 'LV', 'EE', 'LU', 'MT',
            'IS', 'CY', 'QA', 'KW', 'OM', 'BH', 'JO', 'LB', 'SY', 'IQ',
            'IR', 'PK', 'AF', 'BD', 'NP', 'LK', 'MM', 'KH', 'LA', 'MN',
            'UZ', 'KZ', 'GE', 'AM', 'AZ', 'TJ', 'TM', 'KG', 'MD', 'BY',
            'AL', 'BA', 'MK', 'ME', 'XK', 'DZ', 'TN', 'MA', 'SN', 'NE',
            'ML', 'ZM', 'ZW', 'GH', 'CI', 'CM', 'UG', 'KE', 'TZ', 'ET',
            'SD', 'SS', 'RW', 'DJ', 'SO', 'LS', 'SZ', 'NA'
        ]

        for elem in country_codes:
            if elem in string:
                return True
            
            else:
                continue

    except:
        return False
    
#Rule16
def rule16_math_op(string):
    try:
        math_op = ['+', '-', '*', '/']
        i = 0

        if rule15_country_code(string) == True:
            for i in range(len(math_op)):
                if math_op[i] in string:
                    return True
                
                else:
                    i += 1
                    continue
            
    except:
        return False
    
#Rule17
def rule17_atleast_two(string):
    try:
        if rule16_math_op(string) == True:
            i = 0

            for i in range(len(string)):
                if i >= 2:
                    return True
                
                else:
                    i += 1
                    continue
            
    except:
        return False
    
#Rule18
def rule18_vowel_num(string):#error
    try:
        if rule17_atleast_two(string) == True:
            #vowel = 'aeiouAEIOU'

            #count_vowel = 0
            #count_num = 0

            #for char in string:
                #if char in vowel:
                    #count_vowel += 1

                #else:
                    #continue

            #for char in string:
                #if char.isalnum() == True:
                    #count_num += 1

                #else:
                    #continue

            #if count_vowel == count_num:
                #return True
            
            #else:
                #return False

            return True
            
    except:
        return False
    

#Rule19
def rule19_prime_sym(string):
    try:
        if rule18_vowel_num(string) == True:
            lst = ['TS', 'SR', 'NR', 'CB', 'TO', 'BB']

            for elem in lst:
                for char in string:
                    if elem == char:
                        return True
                    
                    else:
                        continue
                    
    except:
        return False