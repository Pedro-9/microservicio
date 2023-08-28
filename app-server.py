from flask import Flask, jsonify, request

productos = [
    {"nombre": "laptop", "precio": 500, "cantidad":4},
    {"nombre": "mouse", "precio": 50, "cantidad":4},
    {"nombre": "monitor", "precio": 200, "cantidad":7},
]

app = Flask(__name__)

@app.route('/saludo')
def saludo():
    return jsonify({"mensaje": "Holaa!"})


@app.route('/productos')
def getproductos():
    return jsonify({"productos": productos})


@app.route('/productos/<string:nombre_producto>')
def getProducto(nombre_producto):
    productosFound = [product for product in productos if product['nombre']==nombre_producto]
    if (len(productosFound)>0):
        return jsonify({"producto": productosFound[0]})
    return jsonify({"mensaje": "Producto No Encontrado."})


@app.route('/productos', methods=['POST'])
def addProducto():
    new_product = {
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad']
    }
    productos.append(new_product)
    return jsonify({"mensaje": "Producto Agregado Exitosamente", "productos": productos})


@app.route('/productos/<string:nombre_producto>', methods=['PUT'])
def editProducto(nombre_producto):
    productFound = [product for product in productos if product['nombre'] == nombre_producto]
    if (len(productFound)>0):
        productFound[0]['nombre'] = request.json['nombre']
        productFound[0]['precio'] = request.json['precio']
        productFound[0]['cantidad'] = request.json['cantidad']
        return jsonify(
            {
                "mensaje": "Producto actualizado",
                "producto": productFound[0]
            }
        )
    return jsonify({"mensaje":"Producto No Encontrado"})


@app.route('/productos/<string:nombre_producto>', methods=['DELETE'])
def deleteProducto(nombre_producto):
    productFound = [product for product in productos if product['nombre'] == nombre_producto]
    if (len(productFound)>0):
        productos.remove(productFound[0])
        return jsonify({
            "mensaje": "Producto Eliminado",
            "productos": productos
        })
    return jsonify({"mensaje": "Producto No Encontrado"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    