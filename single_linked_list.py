class SingleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    """ Por fuera de la clase nodo """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def show_list(self):
        # 1. Declarar una array vacío que contendraá los valores de los nodos de SLL
        array_with_nodes_value = list()
        current_node = self.head
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while (current_node != None):
            # Añado al final de la lista el valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            # Visito el próximo nodo antes de salir del while
            current_node = current_node.next
        # Imprimimos la lista
        print(array_with_nodes_value)

    def create_node_sll_ends(self, value):
        # Creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no
        if self.head == None:
            # Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            # Si ingresa en esta condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1
    def get_node(self, index):
        if index < 1 or index > self.length+1:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node
    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1
   
    def delete_node_sll_pop(self):
        # 1. validar si la lista esta vacia
        # 2. validar si la lista tiene un unico nodo
        # 3. Si tiene mas de un nodo eliminar el nodo que es la cola de la lista
        # 4. asignar el nodo anterior como la nueva cola de la lista
        if self.length==0:
            print('>>Lista vacia no hay nodos para eliminar<<')
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length -=1
        else:
            #1. Recorrer la lista para identificar la cola 
            current_node= self.head
            #2. validar mediante el enlace del nodo actual que haya un nodo
            new_tail= current_node
            while current_node.next != None:
                #3. Convertimos en la cola de la lista el nodo que actualmente estamos visitando 
                new_tail=current_node
                #4. Pasamos al siguiente nodo antes del salir del while por medio del enlace 
                current_node= current_node.next
            #5. Actualizamos la cola de la lista
            self.tail= new_tail
            self.tail.next=None
            #6. Restamos en 1 el tamaño de la lista
            self.length -=1

    '''Eliminar nodo al inicio de la lista'''

    def shift_node_sll(self):
        if self.length==0:
            print(">>Lista vacia no hay nodos por eliminar<<")
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length -=1
        else:
            #Actualizamos el nombre de la cabeza con la var auxiliar 
            remove_node=  self.head
            #Actualizamos la cabeza de la lista
            self.head= remove_node.next
            #Eliminamos el enlace de remove_node con la lista
            remove_node.next=None
            self.length -=1   


    def get_node_value(self, index):
        if index < 0 or index > self.length+1:
            return print('No se encontro')
        elif index == 1:
            return self.head.value
        elif index == self.length:
            return self.tail.value
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node.value

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            # Encontro el nodo y se puede actualizar
            
            search_node.value = new_value
        else:
            # No encuentra el nodo
            return print("No se encontro el nodo")

    def insert_on_index(self, index, value):
        new_node = self.Node(value)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self.head
            for i in range(index):
                previous_node = previous_node.next
                if previous_node is None:
                    raise IndexError("Index out of range")
                new_node.next = previous_node.next
                previous_node.next = new_node
    

    def remove_node_index(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll != None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
            else:
                return print(" >> No se encontro el nodo <<")

    def list_size(self):
        print(self.length)

    def get_node_index_with_value(self, value):
        if self.length == 0:
            return print("Lista vacia")
        elif self.length == 1:
            return 1
        else:
            current_node = self.head.next
            node_counter = 2
            while (value != current_node.value):
                current_node = current_node.next
                node_counter += 1
            return node_counter

    def list_is_empty(self):
        if self.length < 1:
            return print("La lista esta vacia")
        else:
            return print("La lista no esta vacia")

    def reverse(self):
        previous = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next
        self.head = previous
    
    def duplicados(self):
        if self.length == 0:
            return print("Lista vacia")
        elif self.length == 1:
            return 1
        else:
            current_node = self.head.next
            current_node2 = self.head.next
            node_counter = 2
        while current_node != None:
            while current_node2 != None:
                if(current_node2==current_node):
                   return current_node
        



    def eliminarDuplicados(self):
        for i in range(1,self.length+1):
            for j in range(1,self.length+1):
                if(self.get_node(i)==self.get_node(j)):
                    self.remove_node_index(self,j)

    def remove_node_list(self):
        while self.head != None:
            remove_node = self.head
            self.head = remove_node.next
            self.length -= 1