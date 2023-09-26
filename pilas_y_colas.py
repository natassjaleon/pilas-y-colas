import os # para manipular paths
import json # para cargar archivos JSON
from datetime import datetime # para operar con objetos de fecha
from uuid import uuid4 # para generar IDs
import sys # para exportar .txt file

# encuentra el path del archivo a cargar
def find_path(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, name)
# carga el archivo en un objeto diccionario
def load_archive(path):
   # Abriendo config.json
    f = open(path)
   # Retorna .json como un diccionario
    archive = json.load(f)
   # Cierra el archivo .json
    f.close()
    return archive

# Clase para crear y gestionar una cola para las reservaciones
class MyQueue():
    def __init__(self):
        self.q = []
        self.size = len(self.q)

    # encola elementos al final de la lista
    def enqueue(self, element):
        self.q.append(element)
        self.size+=1
        #print(element," fue agregado a la cola.")

    # remueve elemento al frente de la cola
    def dequeue(self):
        if self.is_empty():
            return print("La cola ya se encuentra vacía.")
        element = self.q.pop(0)
        self.size-=1
        print("\nReservación eliminada exitosamente.")

    # retorna si la cola está vacía
    def is_empty(self):
        if len(self.q)==0:
            return True
        return False

    # imprime una reservación de la cola
    def display(self, reservation):
        print("\nNombre del cliente:", getattr(reservation, 'client_name'))
        print("Fecha de reservación: ", getattr(reservation, 'reservation_date'))
        print("Fecha de check in: ", getattr(reservation, 'check_in'))
        print("Fecha de check out: ", getattr(reservation, 'check_out'))
        print("Hora de check in: ", getattr(reservation, 'check_in_hour'))
        print("Hora de check out: ", getattr(reservation, 'check_out_hour'))
        print("Duración de estadía: ", getattr(reservation, 'length_of_stay'))
        print("Número de huéspedes: ", getattr(reservation, 'number_of_guests'))
        print("Número de habitación: ", getattr(reservation, 'room_number'))
        print("Tipo de habitación: ", getattr(reservation, 'room_type'))
        print("Preferencias alimentarias: ", getattr(reservation, 'diet'))
        print("Correo electrónico: ", getattr(reservation, 'email'))
        print("Número de teléfono: ", getattr(reservation, 'phone'))
        print("Precio total: ", getattr(reservation, 'total_price'))
        print("Método de pago: ", getattr(reservation, 'payment_method'))
        print("Notas adicionales: ", getattr(reservation, 'notes'))
        print("Estado de la reservación: ", getattr(reservation, 'status'))
        print("ID de la reservación: ", getattr(reservation, 'reservation_id'))
        print('')
        
    # imprime reservación de la cola si cumple con el criterio
    def find(self, criteria, element):
        if self.is_empty():
            return print("No se encontraron reservaciones.")
        if criteria == '1':
            criteria = 'client_name'
        elif criteria == '2':
            criteria = 'reservation_date'
        elif criteria == '3':
            criteria = 'check_in'
        elif criteria == '4':
            criteria = 'check_out'
        elif criteria == '5':
            criteria = 'check_in_hour'
        elif criteria == '6':
            criteria = 'check_out_hour'
        elif criteria == '7':
            criteria = 'length_of_stay'
        elif criteria == '8':
            criteria = 'number_of_guests'
        elif criteria == '9':
            crtieria = 'room_number'
        elif criteria == '10':
            criteria = 'room_type'
        elif criteria == '11':
            criteria = 'diet'
        elif criteria == '12':
            criteria = 'email'
        elif criteria == '13':
            criteria = 'phone'
        elif criteria == '14':
            criteria = 'total_price'
        elif criteria == '15':
            criteria = 'payment_method'
        elif criteria == '16':
            criteria == 'notes'
        elif criteria == '17':
            criteria = 'status'
        elif criteria == '18':
            criteria = 'reservation_id'
        for reservation in self.q:
            if getattr(reservation, criteria).lower()==element:
                self.display(reservation)
                
    # retorna si la reservación existe dentro de la cola
    def is_reservation(self, criteria, element):
        if criteria == '1':
            criteria = 'client_name'
        elif criteria == '2':
            criteria = 'reservation_date'
        elif criteria == '3':
            criteria = 'check_in'
        elif criteria == '4':
            criteria = 'check_out'
        elif criteria == '5':
            criteria = 'check_in_hour'
        elif criteria == '6':
            criteria = 'check_out_hour'
        elif criteria == '7':
            criteria = 'length_of_stay'
        elif criteria == '8':
            criteria = 'number_of_guests'
        elif criteria == '9':
            crtieria = 'room_number'
        elif criteria == '10':
            criteria = 'room_type'
        elif criteria == '11':
            criteria = 'diet'
        elif criteria == '12':
            criteria = 'email'
        elif criteria == '13':
            criteria = 'phone'
        elif criteria == '14':
            criteria = 'total_price'
        elif criteria == '15':
            criteria = 'payment_method'
        elif criteria == '16':
            criteria == 'notes'
        elif criteria == '17':
            criteria = 'status'
        elif criteria == '18':
            criteria = 'reservation_id'
        for reservation in self.q:
            if getattr(reservation, criteria).lower()==element:
                return True
        return False
    
    # si el id que se busca existe en una reservación dentro de la cola
    # lo reubica al frente de la misma
    def find_id(self, reservation_id):
        for i in self.q:
            if getattr(self.q[0], 'reservation_id') == reservation_id:
                return
            element = self.q.pop(0)
            self.q.append(element)

    # imprime todas las reservaciones de la cola
    def iterate(self):
        if self.is_empty():
            return print("No se encontraron reservaciones.")
        for reservation in self.q:
            self.display(reservation)

# Clase para crear un objeto para cada reservación realizada
class Reservation:
    def __init__(self, reservation_object):
        if 'client_name' in reservation_object:
            if type(reservation_object['client_name']) is not str or reservation_object['client_name']==None or reservation_object['client_name']=='':
                print("Nombre del cliente inválido; el campo no puede estar vacío y debe ser una cadena.")
                raise Exception
        else:
            print("El campo del nombre del cliente no puede estar vacío.")
            raise Exception
        self.client_name = reservation_object['client_name']
      # fecha de reservación debe estar en formato str %Y/%m/%d %H:%M:%S
        if 'reservation_date' not in reservation_object:
            print("El campo de la fecha y hora de la reservación no puede estar vacío.")
            raise Exception 
        try: self.reservation_datetime = datetime.strptime(reservation_object['reservation_date'], '%Y/%m/%d %H:%M:%S')
        except:
            print("El campo de la fecha y hora de la reservación debe estar escrito en el formato aaaa/mm/dd hh:mm:ss.")
            raise Exception
      # guarda la fecha separada de la hora
        self.reservation_date=self.reservation_datetime.date()
         
      # fecha de check in debe estar en formato str %Y/%m/%d %H:%M:%S
        if 'check_in' not in reservation_object:
            print("El campo de la fecha y hora del check-in no puede estar vacío.")
            raise Exception
        try:
            self.check_in = datetime.strptime(reservation_object['check_in'], '%Y/%m/%d %H:%M:%S')
         # guarda la hora de check in separada de la fecha
            self.check_in_hour = self.check_in.time()
        except:
            print("El campo de la fecha y hora del check-in debe estar escrito en el formato aaaa/mm/dd hh:mm:ss.")
            raise Exception
      # fecha de check out debe estar en formato %Y/%m/%d %H:%M:%S
        if 'check_out' not in reservation_object:
            print("El campo de la fecha y hora del check-out no puede estar vacío.")
            raise Exception
        try:
            self.check_out = datetime.strptime(reservation_object['check_out'], '%Y/%m/%d %H:%M:%S')
         # guarda la hora de check in separada de la fecha
            self.check_out_hour = self.check_out.time()
        except:
            print("El campo de la fecha y hora del check-out debe estar escrito en el formato aaaa/mm/dd hh:mm:ss.")
            raise Exception
      # genera duración de la estadía basado en check in y check out
        if (self.check_out.date()-self.check_in.date()).days>1:
            self.length_of_stay = str((self.check_out.date()-self.check_in.date()).days)+' días'
        else:
            self.length_of_stay = str((self.check_out.date()-self.check_in.date()).days)+' día'

      # número de huéspedes debe ser un entero
        if "number_of_guests" in reservation_object:
            if type(reservation_object['number_of_guests']) is not int or reservation_object['number_of_guests']==None or reservation_object['number_of_guests']=='':
                print("Número de huéspedes inválido; el campo no puede estar vacío y debe ser un número entero.")
                raise Exception
        else:
            print("El campo del número de huéspedes no puede estar vacío.")
            raise Exception
        self.number_of_guests = reservation_object['number_of_guests']

        if 'room_number' in reservation_object:
            if type(reservation_object['room_number']) is not str or reservation_object['room_number']==None or reservation_object['room_number']=='':
                print("Número de habitación inválido; el campo no puede estar vacío.")
                raise Exception
        else:
            print("El campo del número de habitación.")
            raise Exception
        self.room_number = reservation_object['room_number']
      # tipo de habitación debe ser una cadena
        if 'room_type' in reservation_object:
            if type(reservation_object['room_type']) is not str or reservation_object['room_type']==None or reservation_object['room_type']=='':
                print("Tipo de habitación inválido; el campo no puede estar vacío.")
                raise Exception
        else:
            print("El campo del tipo de habitación no puede estar vacío.")
            raise Exception         
        self.room_type = reservation_object['room_type']
      # las preferencias alimentarias deben ser una cadena
        if 'diet' in reservation_object:
            if type(reservation_object['diet']) is not str or reservation_object['diet']==None or reservation_object['diet']=='':
                self.diet = 'Sin preferencias'
            else: self.diet = reservation_object['diet']
        else: self.diet = 'Sin preferencias'
      # debe haber al menos 1 campo de contacto lleno, correo o teléfono (ambos str)
        if 'email' not in reservation_object and 'phone' not in reservation_object:
            print("El campo del contacto del cliente (correo o telf) no puede estar vacío.")
            raise Exception
        if 'email' in reservation_object:
            if reservation_object['email']!='' and reservation_object['email']!=None and type(reservation_object['email']) is str:
                self.email = reservation_object['email']
            else: self.email = 'n/a'
        else: self.email = 'n/a'
        if 'phone' in reservation_object:
            if reservation_object['phone']!='' and reservation_object['phone']!=None and type(reservation_object['phone']) is str:
                self.phone = reservation_object['phone']
            else: self.phone = 'n/a'
        else: self.phone = 'n/a'
        if self.email == self.phone:
            print("El campo del contacto del cliente (correo o telf) no puede estar vacío y debe ser una cadena.")
            raise Exception
      # el precio total debe ser un decimal
        if 'total_price' in reservation_object:
            if type(reservation_object['total_price']) is str or reservation_object['total_price']==None or reservation_object['total_price']=='':
                print("Precio total inválido; el campo no puede estar vacío y debe ser un número.")
                raise Exception
        else:
            print("El campo del precio total no puede estar vacio.")
            raise Exception
        self.total_price = float(reservation_object['total_price'])
      # el método de pago debe ser una cadena
        if 'payment_method' in reservation_object:
            if type(reservation_object['payment_method']) is not str or reservation_object['payment_method']==None or reservation_object['payment_method']=='':
                print("Método de pago inválido; el campo no puede estar vacío y debe ser una cadena")
                raise Exception
        else:
            print("El campo del método de pago no puede estar vacio.")
            raise Exception
        self.payment_method = reservation_object['payment_method']
      # las notas adicionales deben ser una cadena
        if 'notes' in reservation_object:
            if type(reservation_object['notes']) is not str or reservation_object['notes']==None or reservation_object['notes']=='':
                self.notes = 'No hay notas adicionales.'
            else:
                self.notes = reservation_object['notes']
        else:
            self.notes = 'No hay notas adicionales.'
      # el estado de la reservación debe ser una cadena: Pendiente o Confirmado
        if 'reservation_status' in reservation_object:
            if (reservation_object['reservation_status']).lower()!='pendiente' and (reservation_object['reservation_status']).lower()!='confirmado':
                print("Estado de reservación inválido; el campo debe estar lleno con Pendiente o Confirmado.")
                raise Exception
        else:
            print("El campo del estado de la reservación no puede estar vacio.")
            raise Exception
        self.status= reservation_object['reservation_status']
        if 'hotel' in reservation_object:
            if type(reservation_object['hotel']) is not str or reservation_object['hotel']==None or reservation_object['hotel']=='':
                print("Hotel inválido; el campo no puede estar vacío y debe ser una cadena.")
                raise Exception
        else:
            print("El campo del hotel no puede estar vacío.")
            raise Exception
        self.hotel = reservation_object['hotel']
      # genera y guarda ID
        self.reservation_id = str(uuid4())

# Clase para crear y gestionar un objeto para cada hotel
class Hotel:
    def __init__(self, hotel_object):
        if 'name' in hotel_object:
            if type(hotel_object['name']) is not str or hotel_object['name']==None or hotel_object['name']=='':
                print("Nombre del hotel inválido; el campo no puede estar vacío y debe ser una cadena.")
                raise Exception
        else:
            print("El campo del nombre del hotel no puede estar vacío.")
            raise Exception
        self.name = hotel_object['name']

        if 'address' in hotel_object:
            if type(hotel_object['address']) is not str or hotel_object['address']==None or hotel_object['address']=='':
                self.address = input("Dirección del hotel vacía. Ingrese una dirección: ")
            else:
                self.address = hotel_object['address']
        else:
            self.address = input("Dirección del hotel vacía. Ingrese una dirección: ")

        if 'phone' in hotel_object:
            if type(hotel_object['phone']) is not str or hotel_object['phone']==None or hotel_object['phone']=='':
                self.phone = input("Número de teléfono del hotel vacío. Ingrese telf.: ")
            else:
                self.phone = hotel_object['phone']
        else:
            self.phone = input("Número de teléfono del hotel vacío. Ingrese telf.: ")

        # diccionario para guardar habitaciones del hotel (#hab: tipo hab)
        if 'available_rooms' in hotel_object:
            if type(hotel_object['available_rooms']) is not dict or hotel_object['available_rooms']==None or hotel_object['available_rooms']=='':
                self.available_rooms = {}
            else:
                self.available_rooms = hotel_object['available_rooms']
        else:
            self.available_rooms = {}

        # crea cola y va encolando cada reservación del hotel
        if 'reservations' in hotel_object:
            self.reservation_queue = MyQueue()  # Queue to store reservations
            for reservation in hotel_object['reservations']:
                self.reservation_queue.enqueue(Reservation(reservation))
        else:
            self.reservation_queue = MyQueue()

    # Agrega reservación a la cola
    def add_reservation(self, reservation):
        try:
            r = Reservation(reservation)
            self.reservation_queue.enqueue(r)
            print("\nSe creó la reservación exitosamente.")
            return True
        except:
            print("\nNo se pudo crear la reservación.")
            return False

    # retorna si la cola de reservaciones está vacía
    def are_reservations(self):
        return self.reservation_queue.is_empty()

    # retorna si la reservación que se busca existe en la cola
    # si existe, la imprime
    def search_reservations(self, search_criteria, element):
        if self.reservation_queue.is_reservation(search_criteria, element):
            return self.reservation_queue.find(search_criteria, element)
        return print("\nNo se encontró ninguna reservación que coincida.")

    # lista reservaciones del hotel
    def list_reservations(self):
        self.reservation_queue.iterate()
    
    # elimina reservación de la cola por ID
    def delete_reservation(self, reservation_id):
        # retorna si la reservación ID existe en la cola
        if self.reservation_queue.is_reservation('reservation_id', reservation_id):
            # si existe, posiciona reservación al frente de la cola
            self.reservation_queue.find_id(reservation_id)
            # remueve primer elemento de la cola
            self.reservation_queue.dequeue()
            return True
        print("\nNo se encontró la reservación.")
        return False
            
    # agrega habitación a la lista de habitaciones del hotel
    def add_room(self, room_number, room_details):
        self.available_rooms[room_number] = room_details
        print("\nHabitación %s: %s agregada exitosamente." %(room_number, self.available_rooms[room_number]))

    # retorna información sobre habitación del hotel que se busca
    def search_room(self, room_number):
        # si existe reservación con esa habitación en la cola:
        if self.reservation_queue.is_reservation('room_number', room_number):
            print("""\nHabitación %s: %s
No se encuentra disponible. Reservación:""" %(room_number,self.available_rooms[room_number]))
            # imprime información de la habitación incluyendo reservación que la ocupa 
            self.reservation_queue.find('room_number', room_number)
            return False
        if room_number in self.available_rooms:
            print("""\nHabitación %s: %s
Se encuentra disponible.""" %(room_number, self.available_rooms[room_number]))
            return True
        print("\nNo se encontró dentro de las habitaciones del hotel.")
        return False

    # lista las habitaciones del hotel y su estado
    def list_rooms(self):
        if self.available_rooms == {}:
            return print("\nNo se encontraron habitaciones en el registro.")
        for key in self.available_rooms:
            print("Habitación %s: %s" %(key, self.available_rooms[key]),end='')
            if self.reservation_queue.is_reservation('room_number', key):
                print(" - Reservada")
            else:
                print(" - Disponible")

    # modifica la habitación seleccionada si existe en el registro y si no está ocupada
    def modify_room(self, room_number, new_details):
        if self.available_rooms == {}:
            print("\nNo se encontraron habitaciones en el registro.")
            return False
        if room_number in self.available_rooms:
            self.available_rooms[room_number] = new_details
            print("\nSe ha modificado la habitación %s: %s exitosamente." %(room_number,self.available_rooms[room_number]))
            return True 
        print("\nNo se encontró la habitación %s dentro de las habitaciones disponibles." %room_number)
        return False

    # elimina la habitación seleccionada si existe en el registro y si no está ocupada
    def delete_room(self, room_number):
        if room_number in self.available_rooms:
            del self.available_rooms[room_number]
            print("\nHabitación %s eliminada exitosamente." %room_number)
            return True
        print("\nNo se encontró la habitación %s dentro de las habitaciones disponibles." %room_number)
        return False

class HotelNode:
    def __init__(self, hotel):
        self.hotel = hotel
        self.next = None
        
# clase para crear y gestionar una lista enlazada de la cadena de hoteles
class HotelChain:
    def __init__(self):
        self.head = None

    # agrega hotel al inicio de la lista enlazada y desplaza el resto
    def add_hotel(self, hotel):
        new_node = HotelNode(hotel)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # busca y retorna hotel dentro de la lista enlazada de hoteles
    def find_hotel(self, hotel_name):
        current = self.head
        while current:
            if current.hotel.name == hotel_name.title():
                return current.hotel
            current = current.next
        return False

    # lista los hoteles de la cadena creando una lista llamada hotels
    # iterando a través de la lista enlazada de la cadena
    # y agregando cada nombre de hotel a la lista hotels
    def list_hotels(self):
        hotels = []
        current = self.head
        while current:
            hotels.append(current.hotel.name)
            current = current.next
        return hotels

    # itera a través de la lista enlazada hasta encontrar el hotel a eliminar
    def delete_hotel(self, hotel_name):
        current = self.head
        prev = None
        while current:
            if current.hotel.name.lower() == hotel_name.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    
    # llama función para agregar habitación a la lista de habitaciones del hotel
    def add_room(self, hotel_name, room_number, room_details):
        # selecciona el hotel y agrega la habitación
        # retorna True si se agregó exitosamente
        return self.find_hotel(hotel_name).add_room(room_number, room_details)

    # verifica que la habitación existe o no dentro del hotel
    def is_room(self, hotel_name, room_number):
        if room_number in getattr(self.find_hotel(hotel_name),'available_rooms'):
            return True
        return False
    
    # verifica que la habitación existe o no dentro del hotel
    # si existe: imprime sus detalles
    def search_room(self, hotel_name, room_number):
        x = self.find_hotel(hotel_name).search_room(room_number)
        if x:
            return True
        return False
    
    # lista las habitaciones dentro del hotel
    def list_rooms(self, hotel_name):
        # selecciona el hotel y lista las habitaciones
        return self.find_hotel(hotel_name).list_rooms()
    
    # modifica la habitación seleccionada y retorna True si se modificó exitosamente
    def modify_room(self, hotel_name, room_number, new_details):
        return self.find_hotel(hotel_name).modify_room(room_number, new_details)
    
    # elimina la habitación seleccionada y retorna True si se eliminó exitosamente
    def delete_room(self, hotel_name, room_number):
        return self.find_hotel(hotel_name).delete_room(room_number)
    
    # llama función para agregar reservación al hotel seleccionado
    def add_reservation(self, hotel_name, reservation):
        # selecciona hotel y llama función para agregar reserva
        return self.find_hotel(hotel_name).add_reservation(reservation)

    # verifica si existen reservaciones creadas dentro del hotel seleccionado
    def are_reservations(self, hotel_name):
        return self.find_hotel(hotel_name).are_reservations()

    # retorna si existe o no una reservación dentro del hotel
    # si existe, la imprime
    def search_reservation(self, hotel_name, criteria, element):
        x = self.find_hotel(hotel_name).search_reservations(criteria, element)
        return x
    
    # lista las reservaciones por hotel
    def list_reservations_by_hotel(self):
        hotels = self.list_hotels()
        current = self.head
        h=0
        print("%s's Hotel" %hotels[h])
        current.hotel.list_reservations()
        while current.next:
            h+=1
            current = current.next
            print("______________________________________")
            print("%s's Hotel" %hotels[h])
            current.hotel.list_reservations()

    # lista todas las reservaciones de un hotel en particular
    def list_reservations(self, hotel_name):
        return self.find_hotel(hotel_name).list_reservations()
    
    # busca reservación del hotel por ID y la elimina si existe
    def delete_reservation(self, hotel_name, reservation_id):
        return self.find_hotel(hotel_name).delete_reservation(reservation_id)

# clase para crear objeto de acción hecha en el sistema
class Action:
    def __init__(self, action, date):
        self.action = action
        self.date = date
        
class HistorialNode:
    def __init__(self, action):
        self.action = action
        self.next = None
        
# clase para crear y gestionar pila del historial de acciones en el sistema
class Historial:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def add(self, action):
        new_node = HistorialNode(action)
        new_node.next = self.head
        self.head = new_node
    def delete(self):
        if self.is_empty():
            return None
        else:
            deleted_action = self.head.action
            self.head = self.head.snext
            return deleted+action
    def see_head(self):
        if self.is_empty():
            return None
        else:
            return self.head.action
    def iterate(self):
        if self.is_empty():
            print("La pila está vacía")
        else:
            self._iterate_aux(self.head)
            
    def _iterate_aux(self, node):
        if node is not None:
            print(node.action.date, end=" ")
            print(node.action.action)
            self._iterate_aux(node.next)
    # función para exportar elementos de la pila
    def export(self, file):
        if not self.is_empty():
            self._export_aux(self.head, file)

    def _export_aux(self, node, file):
        if node is not None:
            file.write(node.action.date+" ")
            file.write(node.action.action)
            self._export_aux(node.next, file)
            

# función para crear reservación
def create_reservation():
    flag=True
    reservation = {}
    print("""\nAgregar reservación. Llene la siguiente información:
*Campos obligatorios
**Fechas en formato AAAA/MM/DD hh:mm:ss""")
    while flag:
        client_name = input("\nNombre del cliente*: ")
        if client_name == '':
            print("\nEl campo del nombre del cliente es obligatorio.")
        else:
            reservation['client_name']=client_name.title()
            flag=False 
    flag = True
    while flag:
        reservation_date=input("Fecha** de la reservación*: ")
        try:
            datetime.strptime(reservation_date, '%Y/%m/%d %H:%M:%S')
            reservation['reservation_date']=reservation_date
            flag = False
        except:
            print("\nEl campo de la fecha y hora de la reservación debe estar escrito en el formato aaaa/mm/dd hh:mm:ss.")
    flag = True
    while flag:
        check_in=input("Fecha** del check-in*: ")
        try:
            datetime.strptime(check_in, '%Y/%m/%d %H:%M:%S')
            reservation['check_in']=check_in
            flag = False
        except:
            print("\nEl campo de la fecha y hora del check-in debe estar escrito en el formato aaaa/mm/dd hh:mm:ss.")
    flag = True
    while flag:
        check_out=input("Fecha** del check-out*: ")
        try:
            datetime.strptime(check_out, '%Y/%m/%d %H:%M:%S')
            reservation['check_out']=check_out
            flag = False
        except:
            print("\nEl campo de la fecha y hora del check-out debe estar escrito en el formato aaaa/mm/dd hh:mm:ss.")
    flag = True
    while flag:
        number_of_guests = input("Número de huéspedes*: ")
        try:
            reservation['number_of_guests']=int(number_of_guests)
            flag=False
        except:
            print("\nEl campo del número de huéspedes debe ser un número entero.")
    flag=True
    while flag:
        room_number = input("Número de la habitación*: ")
        try:
            int(room_number)
            reservation['room_number']=room_number
            flag=False 
        except:
            print("\nEl campo del número de la habitación debe ser un número entero.")

    flag = True
    while flag:
        room_type =input("Tipo de la habitación*: ")
        if  room_type == '':
            print("\nEl campo del tipo de la habitación es obligatorio.")
        else:
            reservation['room_type']=room_type.title()
            flag=False 

    reservation['diet']=input("Preferencias alimentarias: ").title()
    flag=True
    while flag:
        email = input("Correo electrónico*: ")
        phone = input("Número de teléfono: ")
        if  email == '' and phone=='':
            print("\nEs obligatorio llenar al menos uno de los campos de contacto.")
        else:
            reservation['email']=email.lower()
            reservation['phone']=phone
            flag=False
    flag=True    
    while flag:
        total_price =input("Precio total*: ")
        try:
            reservation['total_price']=float(total_price)
            flag=False
        except:
            print("\nEl campo del precio total debe ser un número.")
    flag=True
    while flag:
        payment_method=input("Método de pago*: ")
        if  payment_method == '':
            print("\nEl campo del método de pago es obligatorio.")
        else:
            reservation['payment_method']=payment_method.title()
            flag=False 
            
    reservation['notes']=input("Notas adicionales: ").title()
    flag=True
    while flag:
        reservation_status=input("Estado de la reserva (Pendiente/Confirmado)*: ")
        if  reservation_status.lower() not in ['pendiente', 'confirmado']:
            print("\nEl campo del estado de la reserva es obligatorio y debe llenarlo solo con pendiente o confirmado.")
        else:
            reservation['reservation_status']=reservation_status.title()
            flag=False 
    flag=True
    while flag:
        hotel=input("Hotel en el que se reservó*: ")
        if  hotel =='':
            print("\nEl campo del hotel es obligatorio.")
        else:
            reservation['hotel']=hotel.title()
            flag=False
    return reservation

# función para crear hotel
def create_hotel(hotels):
    flag=True
    hotel = {}
    available_rooms = {}
    hotel['reservations']=[]  
    print("\nCrear hotel. Llene la siguiente información:")
    while flag:
        name = input("\nNombre del hotel: ")
        if name == '':
            print("El campo del nombre del hotel es obligatorio.")
        elif name.title() in hotels:
            print("%s ya existe dentro de la cadena de hoteles." %name.title())
        else:
            hotel['name']=name.title()
            flag=False
    flag=True
    while flag:
        address = input("Dirección: ")
        if address == '':
            print("El campo de la dirección del hotel es obligatorio.")
        else:
            hotel['address']=address.title()
            flag=False
    flag=True
    while flag:
        phone=input("Número de teléfono: ")
        if phone =='':
            print("El campo del número de teléfonod el hotel es obligatorio.")
        else:
            hotel['phone']=phone
            flag=False
    flag=True
    print("Habitaciones disponibles en el hotel: ")
    i=1
    while flag:
        room_number=input('  Número de la habitación %i: ' %i)
        try:
            int(room_number)
            room_type = input('  Tipo de la habitación %i: '  %i).title()
            if room_type=='':
                print("El campo del tipo de la habitación es obligatorio.")
            else:
                available_rooms[room_number] = room_type
                flag2=True
                while flag2:
                    ans = input("Ingrese 1 si desea agregar otra habitación y 0 si no: ")
                    if ans=='0':
                        flag=False
                        flag2=False
                    elif ans == '1':
                        flag2=False
                    else:
                        print("Selección inválida. Intente nuevamente.")
                i+=1
        except: 
            print("El campo del número de la habitación debe ser un número entero.")
    
    hotel['available_rooms']=available_rooms

    flag=True
    while flag:
        try:
            reservation = create_reservation()
            hotel['reservations'].append(reservation)
            print("\nReservación creada exitosamente.")
            flag2=True
            while flag2:
                ans = input("Ingrese 1 si desea agregar otra reservación y 0 si no: ")
                if ans=='0':
                    flag=False
                    flag2=False
                elif ans == '1':
                    flag2=False
                else:
                    print("Selección inválida. Intente nuevamente.")
        except:
            print("No se pudo agregar la reservación al hotel.")
    return Hotel(hotel)

# función para seleccionar el criterio de búsqueda
def get_criteria():
    flag = True
    print("""\nCriterios de búsqueda:
1. Nombre del cliente
2. Fecha de reservación
3. Fecha de check in
4. Fecha de check out
5. Hora de check in
6. Hora de check out
7. Duración de la estadía
8. Número de huéspedes
9. Número de la habitación
10. Tipo de habitación
11. Preferencias alimentarias
12. Correo electrónico
13. Número de teléfono
14. Precio total
15. Método de pago
16. Notas adicionales
17. Estado de la reservación
18. ID de la reservación
0. Volver al menú anterior.""")
    while flag:
        option = input('\nSeleccione un criterio de búsqueda: ')
        if option in ['0','1','2','3','4','5','6','7','8','9', '10',
                          '11','12','13','14','15','16','17','18']:
            return option
        else:
            print("Selección inválida. Inténtelo nuevamente.")

# función para gestionar las habitaciones de cada hotel individualmente
def menu_rooms(hotel_chain_name, hotel_chain, hotel_name, historial):
    flag = True
    while flag:
        print("\nHabitaciones disponibles de %s's Hotels %s" %(hotel_chain_name, hotel_name.title()))
        print("""        1. Listar habitaciones
        2. Consultar habitación (eliminar/modificar)
        3. Crear habitación
        0. Volver al menú anterior""")
        option = input("\nSeleccione una opción: ")
        if option == '1':
            print(" ")
            # lista las habitaciones del hotel
            hotel_chain.list_rooms(hotel_name)
        elif option == '2':
            flag2=True
            room_number = input("\nIngrese el número de la habitación a consultar: ")
            # devuelve True si la habitación a consultar existe dentro del hotel
            # e imprime el número, el tipo y el estado de la misma si esta existe
            room = hotel_chain.search_room(hotel_name, room_number)
            if room: # si la habitación existe
                while flag2:
                    print("""\n            1. Modificar habitación
            2. Eliminar habitación
            0. Volver al menú anterior""")
                    selection = input("\nSeleccione una opción: ")
                    if selection == '1':
                        details = input("Ingrese el nuevo tipo de habitación: ")
                        # modifica el tipo de habitación
                        x = hotel_chain.modify_room(hotel_name, room_number, details.title())
                        if x:
                            action = "Se modificó el tipo de la habitación "+room_number+" a: "+details.title()+", del hotel "+hotel_name.title()+"."
                            flag2=False
                        else:
                            action = "Error al intentar modificar el tipo de la habitación "+room_number+" a: "+details.title()+", del hotel "+hotel_name.title()+"."
                        historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        
                    elif selection == '2':
                        # elimina la habitación
                        x = hotel_chain.delete_room(hotel_name, room_number)
                        if x:
                            action = "Se eliminó la habitación "+room_number+" del hotel "+hotel_name.title()+"."
                            flag2=False
                        else:
                            action = "Error al intentar eliminar habitación "+room_number+" del hotel "+hotel.name.title()+'.'
                        historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    
                    elif selection == '0':
                        flag2=False
                    else:
                        print("\nOpción inválida. Ingrese un número entero del 0 al 2.")
        elif option == '3':
            room_number = input("\nIngrese el número de la habitación a crear: ")
            try:
                int(room_number) #verifica que se ingrese un # entero de la habitación a crear
                # llama función para verificar que la habitación que se intenta crear no existe ya
                if not hotel_chain.is_room(hotel_name, room_number):
                    details = input("\nIngrese el tipo de habitación a crear: ")
                    # agrega habitación a la lista de habitaciones del hotel
                    x = hotel_chain.add_room(hotel_name, room_number, details.title())
                    action = "Se creó y agregó la habitación "+room_number+": "+details.title()+" al hotel "+hotel_name.title()+"."
                    historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                else:
                    action = "Error al intentar crear habitación en hotel "+hotel_name.title()+" con número de habitación ya existente: "+room_number+"."
                    historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                    print("\nHabitación %s ya en sistema." %room_number)
            except:
                action = "Error al intentar crear habitación en hotel "+hotel_name.title()+" con número de habitación inválido: "+room_number+"."
                historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("\nNúmero de habitación inválido. Intente nuevamente.")
        elif option == '0':
            return
        else:
            print("Opción inválida. Ingrese un número entero del 0 al 3.")            
        
# menú para gestionar reservaciones por hotel
def menu_reservations(hotel_chain_name, hotel_chain, hotel_name, historial):
    flag = True
    while flag:
        print("\nReservaciones de %s's Hotels %s" %(hotel_chain_name,hotel_name.title()))
        print("""        1. Listar reservaciones
        2. Buscar reservación
        3. Eliminar reservación
        4. Crear reservación
        0. Volver al menú anterior""")
        option = input("\nSeleccione una opción: ")
        if option == '1':
            print(" ")
            
            # lista las reservaciones del hotel
            hotel_chain.list_reservations(hotel_name)
            
        elif option == '2':
            print(hotel_chain.are_reservations(hotel_name))
            # llama función para verificar si existen reservaciones dentro del hotel
            if hotel_chain.are_reservations(hotel_name):
                print("No se encontraron reservaciones.")
            else:
                # llama función para obtener criterio de búsqueda
                criteria = get_criteria()
                if criteria!='0':
                    # reservación a buscar
                    element = input("Reservación a buscar: ")
                    # busca la reservación
                    hotel_chain.search_reservation(hotel_name, criteria, element.lower())
        elif option == '3':
            # llama función para verificar si existen reservaciones dentro del hotel
            if hotel_chain.are_reservations(hotel_name):
                print("No se encontraron reservaciones.")
            else:
                print("\nReservaciones disponibles:\n")
                # lista las reservaciones disponibles para eliminar
                hotel_chain.list_reservations(hotel_name)
                # id de reservación a eliminar
                reservation_id = input("Ingrese el ID de la reservación que desea eliminar: ")
                # elimina reservación
                x = hotel_chain.delete_reservation(hotel_name, reservation_id)
                if x:
                    action = "Se eliminó la reservación "+reservation_id+" del hotel "+hotel_name.title()+"."
                else:
                    action = "ID inválido. Error al intentar eliminar reservación "+reservation_id+" del hotel "+hotel_name.title()+"."
                historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        elif option == '4':
            # llama función para crear reservación y la agrega al hotel seleccionado
            reservation = create_reservation()
            x = hotel_chain.add_reservation(hotel_name, reservation)
            if x:
                action = "Se creó y agregó nueva reservación al hotel "+hotel_name.title()+"."
            else:
                action = "Error al intentar agregar reservación al hotel "+hotel_name.title()+"."
                historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        elif option == '0':
            return False
        else: print("Opción inválida. Ingrese un entero del 0 al 4.")

# menú para gestionar hotel individualmente
def menu_hotel(hotel_chain_name, hotel_chain, hotel_name, historial):
    flag = True
    while flag:
        print("\n%s's Hotels %s" %(hotel_chain_name, hotel_name.title()))
        print("""\n    1. Habitaciones
    2. Reservaciones
    3. Eliminar hotel
    0. Volver al menú principal""")
        selection = input("\nSeleccione una opción: ")
        if selection == '1':
            
            # llama a la función del menú para gestionar habitaciones
            menu_rooms(hotel_chain_name, hotel_chain, hotel_name, historial)
            
        elif selection == '2':

            # llama a la función del menú para gestionar reservaciones
            menu_reservations(hotel_chain_name, hotel_chain, hotel_name, historial)
            
        elif selection == '3':
            
            # elimina el hotel
            hotel_chain.delete_hotel(hotel_name)
            action = "Se eliminó el hotel "+hotel_name.title()+" de la cadena."
            historial.add(Action(action, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            return print("\n%s's Hotels %s eliminado exitosamente." %(hotel_chain_name, hotel_name.title()))

        elif selection == '0':
            return

        else:
            print('\nOpción inválida. Ingrese un entero del 1 al 4.')
            
# menú principal 
def menu(hotel_chain_name, hotel_chain, historial):
    print("\nCadena de hoteles %s's Hotels" %hotel_chain_name)
    flag=True
    while flag:
        print("""\nMenú principal:
1. Listar hoteles de la cadena
2. Listar reservaciones por hotel 
3. Seleccionar hotel (modificar/eliminar)
4. Crear hotel
5. Ver historial de acciones del sistema
0. Salir""")
        option = input("\nSeleccione una opción: ")
        
        # guarda los nombre de los hoteles de la cadena en una lista
        hotels = hotel_chain.list_hotels()
        
        if option == '1':
            print(" ")
            if len(hotels)==0:
                print("No hay hoteles agregados.")
            else:
                
                # imprime el nombre de cada hotel dentro de la cadena
                for h in hotels:
                    print("%s's Hotels %s" %(hotel_chain_name, h))
                    
        elif option == '2':
            if len(hotels)==0:
                print("\nNo hay hoteles agregados.")
            else:
                print('\nLista de reservaciones por hotel:\n')
                
                # imprime todas las reservaciones de la cadena por hotel
                hotel_chain.list_reservations_by_hotel()
            
        elif option == '3':
            if len(hotels)==0:
                print("\nNo hay hoteles agregados.")
            else:
                flag2=True
                print(" ")
                for h in hotels:
                    print(h)
                hotel_name = input("\nIngrese el nombre del hotel que desea seleccionar: ")
                if hotel_name.title() in hotels:
                    
                    # llama función del menú para gestionar cada hotel individualmente
                    menu_hotel(hotel_chain_name, hotel_chain, hotel_name, historial)
                else:
                    print("\nNo se encontró hotel %s" %hotel_name)
                    
        elif option == '4':
            try:
                # llama función para crear hotel y retorna objeto del tipo Hotel
                hotel = create_hotel(hotels)

                # agrega hotel a la cadena de hoteles
                hotel_chain.add_hotel(hotel)
                print("\n%s agregado exitosamente a la cadena de hoteles." %getattr(hotel,'name'))
            except:
                print("\n%s no pudo ser creado." %getattr(hotel,'name'))

        elif option == '5':
            # imprime el historial de acciones realizadas hasta ahora
            print("\nHistorial de acciones realizadas en el sistema: ")
            historial.iterate()
        
        elif option == '0':
            # exporta el historial de acciones a un archivo .txt y cierra el programa
            file = open('historial.text','w')
            historial.export(file)
            file.close()
            return print("\nFin.")
        else:
            print("\nOpción inválida. Ingrese un entero del 0 al 5.")


def main():
    # inicializa objeto lista enlazada de la cadena de hoteles del tipo HotelChain
    hotel_chain = HotelChain()
    # inicializa objeto pila de las acciones realizadas en el sistema
    historial = Historial()
    try:
        # intenta cargar archivo de datos y configuración
        config = load_archive(find_path('config.json'))
        # guarda nombre de la cadena de hoteles
        hotel_chain_name = config['hotel_chain_name']
        # lista para cargar el archivo JSON de cada hotel convertido en  objeto del tipo Hotel
        hotels=[]
        for path in config['file_route_name']:
            hotels.append(Hotel(load_archive(path)))
    except:
        raise Exception("Hubo un error en la carga del archivo. Revisar el path en config.json.")
    # agrega cada hotel a la lista enlazada de la cadena de hoteles
    for hotel in hotels:
        hotel_chain.add_hotel(hotel)
    # llama función menú
    menu(hotel_chain_name, hotel_chain, historial)
    
main()
