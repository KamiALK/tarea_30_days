# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
concatenacion = 'Thirty'+'Days'+ 'Of'+'Python'

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Coding_For_All = 'Coding' + 'For' + 'All'

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print()
print(company)

# Print the length of the company string using len() method and print()
print('longitud de la variable',len(company))

# Change all the characters to uppercase letters using upper() method
print('mayusculas:    ', company.upper()) # uppper()no tiene parametros

# Change all the characters to lowercase letters using lower() method
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
company = 'Coding For All'
print ('solo la primera en mayuscula', company.capitalize())
print('la primer letra de cada palabra en mayuscula', company.title())
print('la primer letra de cada palabra en minuscula', company.swapcase())

# Cut(slice) out the first word of Coding For All string
frase = 'Coding For All string'
cut = frase[6:]
print('se recorre el string cut = frase[6:] ' , cut)

# Check if Coding For All string contains a word Coding using the method index, find or other methods
completo = 'Coding For All'
trozo = 'oding'
print(completo.index(trozo))

# Replace the word coding in the string 'Coding For All' to Python

