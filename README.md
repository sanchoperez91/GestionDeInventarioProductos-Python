# GestionDeInventarioProductos-Python

# 📦 Inventario de Productos en Python

Este proyecto implementa una aplicación para la **gestión de un inventario de productos** usando **Python** y los principios de **Programación Orientada a Objetos (POO)**. La aplicación permite realizar las operaciones típicas de un inventario, como **agregar**, **actualizar**, **eliminar** y **mostrar** productos, cada uno de los cuales es representado como un objeto de la clase `Producto`.

## 🚀 Características

### Clases y Estructura
- **`Producto`**: Esta clase representa cada producto del inventario y tiene los siguientes atributos privados:
  - `nombre`: nombre del producto.
  - `categoria`: categoría a la que pertenece el producto.
  - `precio`: precio del producto (debe ser mayor que 0).
  - `cantidad`: cantidad de producto en stock (debe ser mayor o igual a 0).
- **`Inventario`**: Esta clase gestiona una lista de productos y permite realizar diversas operaciones sobre ellos.

### Funcionalidades Principales
La aplicación ofrece las siguientes operaciones sobre el inventario:

1. **Agregar Producto**: Añade un nuevo producto al inventario después de verificar que no exista ya. Si el producto ya está en el inventario, no se agrega.
2. **Actualizar Producto**: Permite modificar el `precio` y la `cantidad` de un producto existente. Antes de actualizar, verifica que los valores sean válidos.
3. **Eliminar Producto**: Elimina un producto del inventario por su nombre, si existe.
4. **Mostrar Inventario**: Lista todos los productos en el inventario, mostrando el nombre, categoría, precio y cantidad de cada producto.
5. **Buscar Producto**: Permite buscar un producto específico por su nombre.

### Validaciones
La aplicación incluye las siguientes validaciones y manejos de errores:

- El `precio` debe ser mayor que 0.
- La `cantidad` debe ser mayor o igual a 0.
- Las entradas de datos se validan para evitar valores no válidos.
- Excepciones manejadas para asegurar que el sistema sea robusto y fácil de usar.

### Encapsulamiento y Métodos
- Todos los atributos de la clase `Producto` son privados, lo que asegura el encapsulamiento. Se implementan **getters** y **setters** para acceder y modificar los valores de los atributos de manera controlada.
- La clase `Inventario` organiza cada funcionalidad en métodos dedicados, lo que facilita la legibilidad y la reutilización del código.

## 📄 Estructura del Código

El código está estructurado para ser legible y modular:

- Cada funcionalidad (agregar, actualizar, eliminar, etc.) está implementada en un método específico dentro de su clase correspondiente.
- Se evita el uso de variables globales, y toda la información sobre productos se gestiona exclusivamente dentro de la clase `Inventario`.

## 📝 Ejemplo de Uso

```python
# Crear un inventario
inventario = Inventario()

# Crear un producto
producto = Producto(nombre="Laptop", categoria="Electrónica", precio=1200.50, cantidad=10)

# Agregar el producto al inventario
inventario.agregar_producto(producto)

# Mostrar todos los productos en el inventario
inventario.mostrar_inventario()

# Buscar un producto
inventario.buscar_producto("Laptop")

# Actualizar la cantidad y precio de un producto
inventario.actualizar_producto("Laptop", precio=1300, cantidad=15)

# Eliminar un producto
inventario.eliminar_producto("Laptop")
