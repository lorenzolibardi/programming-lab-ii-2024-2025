from classes.pila import Pila

pila1 = Pila(5)
pila1.push(7)
pila1.push(3)
pila1.push(5)
pila1.push(5)
pila1.push(9)
print(pila1)
print(pila1.pop())
print(pila1)

pila2 = Pila(3)
pila3 = Pila(4)

print(pila2 < pila3)

print(Pila.pile_totali())

print(pila2 == pila3)