/*
    A função "tocaSom", através do parâmetro "(seletorElemento)", faz a leitura da "index.html".
    Mas para isso, criamos uma variavel "const" , que recebe o nome de "elemento", cujo valor é "document.querySelector".
    O valor "document.querySelector", ler a "index.html" no nosso "main.js" para interagir com o HTML do nosso AluraMidi.
*/

function tocaSom (seletorElemento) {

    const elemento = document.querySelector(seletorElemento);


/*
    Essa condição é para informar que a nossa função "TocaSom" só executará o audio, se o parâmetro for "(seletorElemento)".
    Caso você entre no console do devTools e digite "TocaSom(qualquer_outra_coisa)", aparecerá a mensagem "Elemento ou Seletor Inválido".
*/     
    if (elemento && elemento.localName === 'audio') {
        elemento.play();
    }

    else {
        
        //alert ('Elemento ou Seletor Inválido!);
        // Esse comando acima gera um alerta na tela com a mensagem que está dentro dos parenteses.
        console.log ('Elemento ou Seletor Inválido!'); 
        // Esse comando vai gerar a mensagem no console do DevTools, cuja mensagem está dentro dos parenteses.
    }
}

/*
    const == valor constante. Portanto não pode ser alterado,
    também não pode receber outro valor.
    Sendo assim listaDeTeclas é um valor fixo.

    A função while, traduzindo para o pt-br, significa 'enquanto'.
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
    O for é também uma estrutura de repetição, porém menos limitada.
    Basta analisarmos que notaremos suas diferenças em respeito ao "while".
*/

const listaDeTeclas = document.querySelectorAll('.tecla');

for (let contador = 0; contador < listaDeTeclas.length; contador++) {
    
    const tecla = listaDeTeclas[contador];    
    const instrumento = tecla.classList[1];        
    const idAudio = `#som_${instrumento}`; 
    
    tecla.onclick = function () {
        tocaSom(idAudio);
    }
    
    // Evento para quandoa a tecla for pressionada.
    tecla.onkeydown = function (evento) {
        if (evento.code === 'Space' || evento.code === 'Enter') {
            tecla.classList.add('ativa');
        }
    }
    // Evento para quandoa a tecla for largada.
    tecla.onkeyup = function () {
        tecla.classList.remove('ativa');
    }
}