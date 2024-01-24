const numero = Number(prompt("Digite um número"));
const numeroTitilo = document.getElementById("numero-titulo");
const texto = document.getElementById("texto");

numeroTitilo.innerHTML = numero;

texto.innerHTML = "";
texto.innerHTML += `<p>Raiz quadrada: ${Math.sqrt(numero)}<p>`;
texto.innerHTML += `<p>${numero} é inteiro: ${Number.isInteger(numero)}<p>`;
texto.innerHTML += `<p>Arredondando para baixo ${Math.floor(numero)}<p>`;
texto.innerHTML += `<p>Arredondando para cima ${Math.ceil(numero)}<p>`;
texto.innerHTML += `<p>Com duas casas decimais: ${numero.toFixed(2)}<p>`;
