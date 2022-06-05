/*
A função tocaSom faz a leitura da index.html através do comando "document.querySelector".
Em seguida seleciona o botão cujo "id == som_tecla_pom" dentro dos parenteses.
Em seguida disso, executa a função ".play()".
*/

function tocaSom (seletorElemento) {

    const elemento = document.querySelector(seletorElemento);

    if (elemento && elemento.localName === 'audio') {
        elemento.play();
    }

    else {
        //alert ('Elemento ou Seletor Inválido!);
        console.log ('Elemento ou Seletor Inválido!');
    }
}


/*
const == valor constante. Portanto não pode ser alterado,
também não pode receber outro valor.
Sendo assim listaDeTeclas é um valor fixo.
*/

const listaDeTeclas = document.querySelectorAll('.tecla');


/*
let == armazenar outros valores dentro de uma função.
Portanto só pode ser usado dentro de uma função.
*/

let contador = 0;


/*
A função while, traduzindo para o pt-br, significa enquanto.
O while espera receber uma condição que seja verdadeira ou falsa.
Ele é uma estrutura de repetição que, enquanto for verdadeira, a função (contador < listaDeTeclas)
se repetirá. Quando 'while' == false, a função (contador < lista.lenght) encerrará.


while (contador < listaDeTeclas.length) {
    const tecla = listaDeTeclas[contador];
    const instrumento = tecla.classList[1];
    // template string
    const idAudio = `#som_${instrumento}`;
    tecla.onclick = function () {
        tocaSom(idAudio);
    }
    contador = contador + 1;
    
}
*/

for (let contador = 0; contador < listaDeTeclas.length; contador++) {
    
    const tecla = listaDeTeclas[contador];    
    const instrumento = tecla.classList[1];        
    const idAudio = `#som_${instrumento}`; //template string
    
    tecla.onclick = function () {
        tocaSom(idAudio);
    }
    
    tecla.onkeydown = function (evento) {
        if (evento.code === 'Space' || evento.code === 'Enter') {
            tecla.classList.add('ativa');
        }
    }

    tecla.onkeyup = function () {
        tecla.classList.remove('ativa');
    }
}