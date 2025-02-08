class Pila: # Politica Last In First Out (LIFO)
    pile_create = 0

    def __init__(self, n):
        """
        Metodo che viene chiamato durante la costruzione di una istanza di
        Pila per impostarne lo stato iniziale.
        """
        self.size = n
        self.items = []
        Pila.pile_create += 1
    
    def push(self, item):
        assert item is not None
        if len(self.items) >= self.size:
            raise f"Error: stack reached max size (n={self.size})"
        self.items.append(item)
    
    def pop(self):
        if len(self.items) == 0:
            raise "Error: stack is empty"
        return self.items.pop()
    
    def destroy(self):
        del self
        Pila.pile_create -= 1

    @staticmethod # per definire metodi statici
    def pile_totali():
        return Pila.pile_create
    
    def __str__(self):
        """
        Metodo chiamato da str(oggetto) e da print(oggetto).
        Solitamente si implementa restituendo una stringa con una 
        rappresentazione informale/leggibile dell'oggetto.
        Se non è definito usa __repr__ (vedi sotto)
        """
        return str(self.items)
    
    def __repr__(self):
         """
         Metodo chiamato da repr(oggetto), e dalla console REPL quando si
         scrive oggetto e si preme invio.
         Se possibile, l'implementazione deve restituire una stringa che,
         quando passata a eval(), ricostruisce l'oggetto.
         Se non è definito usa il metodo di Object che stampa solo l'indirizzo
         """
         return f"Pila('{self.size}')"


    def __eq__(self, altro):
        """Metodo chiamato dall'espressione oggetto == altro.
          Se non è definito usa la definizione di Object basata sull'indirizzo in memoria"""
        assert type(altro) == Pila
        if len(self.items) != len(altro.items):
            return False
        if len(self.items) == 0: # quindi anche l'altra
            return self.size == altro.size
        for i in range(len(self.items)):
            if self.items[i] != altro.items[i]:
                return False
        return True

    def __lt__(self, altro):
        """
        Metodo chiamato dall'espressione oggetto < altro_oggetto. 
        """
        assert type(altro) == Pila, "Si possono confrontare solo 2 pile"
        if len(self.items) == 0 and len(altro.items) == 0:
            return self.size <= altro.size
        else:
            return len(self.items) <= len(altro.items)