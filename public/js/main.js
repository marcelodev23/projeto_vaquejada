async function carregarPedidos() {
    const response = await axios.get('http://127.0.0.1:8000/dados/pedidos')
    const dados_pedidos = response.data;
    const lista_table = document.getElementById('table_dados')
    lista_table.innerHTML = ''
    dados_pedidos.forEach(function (pedido) {
        const item = document.createElement('tr')
        lista_table.append(item)
        //-----------------------------------------
        const numero = document.createElement('td')
        numero.innerHTML = pedido[0]
        lista_table.append(numero)
        //------------------------------------------
        const puxador = document.createElement('td')
        puxador.innerHTML = pedido[1]
        lista_table.append(puxador)
        //------------------------------------------
         const Esteira = document.createElement('td')
         Esteira.innerHTML = pedido[2]
         lista_table.append(Esteira)
        //------------------------------------------
        const Representacao = document.createElement('td')
        Representacao.innerHTML = pedido[3]
        lista_table.append(Representacao)
        //------------------------------------------
        const Situação = document.createElement('td')
        if (pedido[4]== 0){
            Situação.innerHTML = 'Reservado'
        }
        if (pedido[4]== 1){
            Situação.innerHTML = 'Pago'
        }
        
        lista_table.append(Situação)
    });
}

async function dados_evento (){
    const response = await axios.get('http://127.0.0.1:8000/dados/evento')
    const dados_pedidos = response.data;
    const name_nn = document.getElementById('name_parque')
    name_nn.innerHTML= dados_pedidos[0][0] 
}



async function carregar() {
    const response = await axios.get('http://127.0.0.1:8000/dados/pedidos')
    const dados_pedidos = response.data;
    const lista_table = document.getElementById('k')
    lista_table.innerHTML = ''
    let s=0
    dados_pedidos.forEach(function (pedido) {
        s+=1

        const numero = document.createElement('button')
        numero.innerHTML = pedido[0]
        lista_table.append(numero)
        //------------------------------------------
    });
}

async function test() {
    const response = await axios.get('http://127.0.0.1:8000/dados/pedidos')
    const dados_pedidos = response.data;
    
    const response_ = await axios.get('http://127.0.0.1:8000/dados/evento')
    const dados_evento = response_.data;
    
    const lista_table = document.getElementById('k')
    lista_table.innerHTML = ''
    var lista_total = []
    var lista_numeros_reservados = []

    for (let index = 1; index <= parseInt(dados_evento[0][1]); index++) {
        lista_total.push(index);
    }

    dados_pedidos.forEach(function (dados) {
        lista_numeros_reservados.push(dados[0]);
    })

    console.log(lista_numeros_reservados[1]);
    console.log(lista_total);

    for (let index = 1; index <= lista_total.length; index++) {
       
           const numero = document.createElement('button')
            numero.innerHTML = index
            lista_table.append(numero)
        
        
    }

    //for (let index = 1; index <= 100; index++) {
    //    const numero = document.createElement('button')
    //    numero.innerHTML = index
    //    numero.style.color = "blue"
    //    lista_table.append(numero)
       
    //}
}


//document.getElementById("k").innerHTML = "Hello World! "
carregarPedidos()