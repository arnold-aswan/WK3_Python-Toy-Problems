# Consonant value
 
def consonant_value(input_string):
    let_dict = {
        " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}
    vowels = {'a','e','i','o','u'}
    
    consonant_string = input_string
    
    for vowel in input_string:
        if vowel in vowels:
            consonant_string = consonant_string.replace(vowel, " ")
    #print(consonant_string) 
    
    consonant_list = list(consonant_string)
    #print(consonant_list)   
     
    replaced = []
    for char in consonant_list:
        if char in let_dict:
               replaced.append(let_dict[char])
    #print(replaced) 
    
    max_value = 0
    current_value = 0
    for num in replaced:
        if num != 0:current_value += num
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    max_value = max(max_value, current_value)    
    print(max_value)        
                           
consonant_value('teenage')
    