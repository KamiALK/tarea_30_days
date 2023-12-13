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

# Replace the word coding i0n the string 'Coding For All' to Python

frase = 'Coding For All'

    
    
# parte_cambiada = input('vamos a reemplazar la frase: Coding For All /n escribe la palabra que deseas remplazar')
# parte_nueva = input('dime la parte nueva')
# print(frase.replace(parte_cambiada,parte_nueva))
# Change Python for Everyone to Python for All using the replace method or other methods
base = 'Python for Everyone'
cambio = 'Python for All'
print ('frase original',base)
print(base.replace('Python for Everyone','Python for All'))

# Split the string 'Coding For All' using space as the separator (split())
y = 'Coding For All'
print(y.split(' '))
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
var = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(var.split(','))
# What is the character at index 0 in the string Coding For All
var ='Coding For All'
indexvar = var[0]
print(indexvar)

# What is the last index of the string Coding For All.
var ='Coding For AlL'
ultimoindex = var[-1]
print(ultimoindex)

# What character is at index 10 in "Coding For All" string
var ='Coding For AlL'
index10 = var[10]
print(index10)
if index10 == ' ':
    print('tomaste in espacio')
    
# Create an acronym or an abbreviation for the name 'Python For Everyone'
frase = 'Python For Everyone'
acronimo = frase[0:17:-7]
print(acronimo)

