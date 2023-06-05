
num1 = 42 #Declaración de Variables, número
num2 = 2.3 #Declaración de Variables, número
boolean = True #Declaración de Variables, booleano
string = 'Hello World' #Declaración de Variables, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Declaración de Variables, lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Declaración de Variables, diccionario
fruit = ('blueberry', 'strawberry', 'banana') #Declaración de Variables, tupla
print(type(fruit)) #type verifica tipo de dato 
print(pizza_toppings[1]) #muestra el elemento ubicado en esa posición
pizza_toppings.append('Mushrooms') #con append agrego un dato a la lista
print(person['name']) #muestra contenido 'name' del diccionario
person['name'] = 'George' #Variación dato
person['eye_color'] = 'blue'#Agrega dato que no estaba declarado
print(fruit[2]) #Declaración de Variables

if num1 > 45: #condicionales
    print("It's greater") #mostrar en la terminal si se cumple la condición
else: 
    print("It's lower") #mostrar en la terminal si se cumple la condición

if len(string) < 5: #condicionales
    print("It's a short word!") #mostrar en la terminal si se cumple la condición
elif len(string) > 15: 
    print("It's a long word!") #mostrar en la terminal si se cumple la condición
else: 
    print("Just right!") #mostrar en la terminal si se cumple la condición

for x in range(5): #ciclo desde 0 a 5
    print(x)
for x in range(2,5): #ciclo parte en 2 ahasta 5
    print(x)
for x in range(2,10,3): #ciclo parte en 2 hasta 10, de 3 en 3
    print(x)
x = 0
while(x < 5): #ciclo de 0 a 5, aumentando +1 en cada vuelta
    print(x)
    x += 1

pizza_toppings.pop() #elimina último elemento
pizza_toppings.pop(1) #elimina elemento en posición 1

print(person) #imprime person con dato agregado al diccionario
person.pop('eye_color') #elimina dato 'eye_color' de diccionario person
print(person) #imprime person con cambios

for topping in pizza_toppings: 
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives': #condicional
        break

def print_hello_ten_times(): #función
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #función
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #función
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section

comentario de varias lineas
"""

# print(num3)     #comentario en linea
# num3 = 72       #comentario en linea
# fruit[0] = 'cranberry'       #comentario en linea
# print(person['favorite_team'])    #comentario en linea
# print(pizza_toppings[7])   #comentario en linea
#   print(boolean)   #comentario en linea
# fruit.append('raspberry')   #comentario en linea
# fruit.pop(1)    #comentario en linea