const nome = prompt("Digite seu nome completo:");

let quantidade = nome.length;
let resposta1 = nome[1];
let resposta2 = nome[0];
let resposta3 = nome[nome.length - 1];
let resposta40 = nome[nome.length - 1];
let resposta41 = nome[nome.length - 2];
let resposta42 = nome[nome.length - 3];
let resposta4 = resposta42 + resposta41 + resposta40;
let resposta5 = nome;
let resposta6 = nome.toLocaleUpperCase();
let resposta7 = nome.toLocaleLowerCase();

document.body.innerHTML += `Seu nome é: ${nome}<br />`;
document.body.innerHTML += `Seu nome tem ${quantidade} letras <br />`;
document.body.innerHTML += `A segunda letra do seu nome é: ${resposta1} <br />`;
document.body.innerHTML += `Qual o primeiro índice da letra LETRA no seu nome? ${resposta2}<br />`;
document.body.innerHTML += `Qual o último índice da letra LETRA no seu nome? ${resposta3}<br />`;
document.body.innerHTML += `As últimas 3 letras do seu nome são: ${resposta4}<br />`;
document.body.innerHTML += `As palavras do seu nome são: ${resposta5}<br />`;
document.body.innerHTML += `Seu nome com letras maiúsculas: ${resposta6}<br />`;
document.body.innerHTML += `Seu nome com letras minúsculas: ${resposta7}<br />`;
document.body.innerHTML += `Quantas vogais tem seu nome? <br />`;
