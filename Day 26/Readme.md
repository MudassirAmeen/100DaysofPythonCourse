>>> name = "Mudassir"
>>> new_name = [letter for letter in name]
>>> new_name
['M', 'u', 'd', 'a', 's', 's', 'i', 'r']
>>> new_range = [n*2 for n in range(1,5)]
>>> new_range
[2, 4, 6, 8]
>>> names = ["Alex", "Beth", "Caroline", "Dave", Eleanor", "Fraddie"]
  File "<stdin>", line 1
    names = ["Alex", "Beth", "Caroline", "Dave", Eleanor", "Freddie"]
                                                                   ^ 
SyntaxError: unterminated string literal (detected at line 1)        
>>> names = ["Alex", "Beth", "Caroline", "Dave", Eleanor", "Freddie"]
  File "<stdin>", line 1
    names = ["Alex", "Beth", "Caroline", "Dave", Eleanor", "Freddie"]     
                                                                   ^      
SyntaxError: unterminated string literal (detected at line 1)
>>> names = ["Alex", "Beth", "Caroline", "Dave", Eleanor", "Freddie"] 
  File "<stdin>", line 1
    names = ["Alex", "Beth", "Caroline", "Dave", Eleanor", "Freddie"]     
                                                                   ^      
SyntaxError: unterminated string literal (detected at line 1)
>>> names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]    
>>> short_names = [name.upper() for name in names if len(name) > 4] 
>>> short_names
['CAROLINE', 'ELEANOR', 'FREDDIE']
>>>




Do all of this the terminal.