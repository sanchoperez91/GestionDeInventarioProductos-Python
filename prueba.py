#creamos la clase principal productos
class Producto:
    #creamos el constructor de la clase producto
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad  
    
    # creamos los getters
    def get_nombre(self):
        return self.__nombre
        
    def get_categoria(self):
        return self.__categoria
    
    def get_precio(self):
        return self.__precio
       
    def get_cantidad(self):
        return self.__cantidad

    # creamos los setters   
    def set_nombre(self, nombre):
        self.__nombre = nombre    
    
    def set_categoria(self, categoria):
        self.__categoria = categoria       
    
    def set_precio(self, precio):
        #hacemos la validacion del precio para que no sea un importe negativo
        if precio >= 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor o igual que 0.")   
    
    def set_cantidad(self, cantidad):
        #hacemos la validacion de la cantidad para que no sea un valor negativo
        if cantidad >=0 :
            self.__cantidad = cantidad
        else :
            raise ValueError("La cantidad debe ser mayor que 0")       

#ahora creamos la clase Inventario
class Inventario:   
    #creamos el constructor de inventario
    def __init__(self):
        #creamos una lista vacia de productos
        self.__productos = []
    
    #creamos el metodo para agregar los productos    
    def agregar_producto(self, producto):   
        for x in self.__productos:
            #comprobamos si el producto ya existe y de ser asi devolvemos un error
            if x.get_nombre() == producto.get_nombre():
                raise ValueError("El nombre del producto ya existe en el inventario.")
            # Si no existe, lo agregamos
        self.__productos.append(producto)
    
    #ahora creamos el metodo para actualizar el precio o cantidad de un producto:
    #ponemos nombre como parametro obligatorio sin inicializar, mientras que precio y cantidad los inicializamos en None por si uno de los dos no se modifican
    def actualizar_producto(self, nombre, precio_nuevo=None, cantidad_nueva=None):
        #creamos un bucle for que recorra toda la lista de productos:
        for x in self.__productos:
            #primero buscamos el objeto producto cuyo nombre coincida con el de la busqueda
            if x.get_nombre() == nombre:
                #cuando encuentra ese nombre, confirma si el valor precio_nuevo esta vacio, de lo contrario sobrescribe el antiguo valor de precio con el actual guardado en precio_nuevo
                if precio_nuevo is not None:
                    x.set_precio(precio_nuevo)
                #cuando encuentra ese nombre, confirma si el valor cantidad_nueva esta vacio, de lo contrario sobrescribe el antiguo valor de cantidad con el actual guardado en cantidad_nueva
                if cantidad_nueva is not None:
                    x.set_cantidad(cantidad_nueva)
                    
                #como encontró el valor nombre == nombre no sigue con el bucle y de ahi la salida con el return
                return 
        #en caso de no encontrar el producto devolvemos el error
        raise ValueError("Producto no encontrado en el inventario.")    
    #ahora creamos el metodo para eliminar producto, como el enunciado no lo deja claro, entiendo que el producto se busca por el nombre
    def eliminar_producto(self, nombre):
        #creamos un bucle for que recorra toda la lista de productos:
        for x in self.__productos:
            #primero buscamos el objeto producto cuyo nombre coincida con el de la busqueda
            if x.get_nombre() == nombre:
                #seleccionamos ese objeto y lo eliminamos
                self.__productos.remove(x)
                #como encontró el valor nombre == nombre no sigue con el bucle y de ahi la salida con el return
                return   
        #en caso de no encontrar el producto devolvemos el error
        raise ValueError("Producto no encontrado en el inventario.")
    #ahora creamos el metodo para mostrar el inventario, es decir, imprimir todos los productos
    def mostrar_inventario(self):
        # primero confirmamos que la lista no este vacia
        if not self.__productos:
            #si la lista esta vacia imprimimos lo siguiente:
            print("El inventario está vacío.")
            return
        # Mostramos todos los productos en el inventario
        for x in self.__productos:
            print(f"Nombre: {x.get_nombre()}, Categoría: {x.get_categoria()}, Precio: {x.get_precio()}, Cantidad: {x.get_cantidad()}")
        
    #ahora creamos el metodo para buscar producto por el nombre
    def buscar_producto(self, nombre):
        #creamos un bucle for que recorra toda la lista de productos:
        for x in self.__productos:
            #primero buscamos el objeto producto cuyo nombre coincida con el de la busqueda
            if x.get_nombre() == nombre:
                #seleccionamos ese objeto y lo "retornamos"
                return x
        #si no encuentra el valor nombre == nombre no sigue con el bucle y de ahi la salida con el return None
        return None    