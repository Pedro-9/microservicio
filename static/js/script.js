
function get_productos() {
    fetch('/productos',{method: 'GET'})
        .then(response => response.json())
        .then(data => mostrarData(data))
        .catch(error => console.log(error))

    const mostrarData = (data) => {
        //console.log(data)
        data = data.productos
        let body = ""
        for (var i = 0; i < data.length; i++) {
            body += `<tr><td>${data[i].nombre}</td><td>${data[i].precio}</td><td>${data[i].cantidad}</td></tr>`
        }
        document.getElementById('data').innerHTML = body
        //console.log(body)
    }

}


function add_productos(){
    const _nombre = document.getElementById('nombre').value;
    const _precio = document.getElementById('precio').value;
    const _cantidad = document.getElementById('cantidad').value;

    // armar el body 
    const _body = { nombre: _nombre ,precio: _precio ,cantidad: _cantidad}

    // Header por default
    const _header = {"Content-Type": "application/json"}

    fetch('/productos',{
        method: "POST",
        body: JSON.stringify(_body),
        headers: _header
    })
    .then((res) => res.json())
    .catch((error) => console.error("Error:", error))
    .then((response) => console.log("Success:", response));

}
