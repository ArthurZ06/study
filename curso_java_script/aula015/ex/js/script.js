const numero = prompt("Digite um número");

let resposta0 = Math.sqrt(numero);
let resposta1 = Number.isInteger(numero)
let resposta2 = Number.isNaN(numero)

document.body.innerHTML += `Seu Número é ${numero} `;
document.body.innerHTML += `Raiz quadrada: ${resposta0} `;
document.body.innerHTML += `${numero} é inteiro:{} `;
document.body.innerHTML += `É NaN: {} `;
document.body.innerHTML += `Arredondando para baixo: {} `;
document.body.innerHTML += `Arredondando para cima: {} `;
document.body.innerHTML += `Com duas casas decimais: {} `;
