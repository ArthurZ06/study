/* 
Arthur Nicolas tem 17 anos, pesa 100 kg
tem 1.83 de altura e seu IMC é de 25
*/

const nome = "Arthur";
const sobrenome = "Nicolas";
const idade = 17;
const peso = 100;
const altura = 1.83;
const calculo = altura * 2;
var imc = peso / calculo;
var imc = imc.toFixed(2);

/*
console.log(
  nome,
  sobrenome,
  "tem",
  idade,
  "anos, pesa",
  peso,
  "kg tem",
  altura,
  "de altura e seu IMC é de",
  imc
);
*/

console.log(
  `${nome} ${sobrenome} tem ${idade} anos pesa ${peso} kg tem ${altura} de altura e seu IMC é de ${imc}`
);

if (imc <= 18.5)
  console.log("Rapaz vai comer uma macarronada ai pra ganhar uns quilinhos");
if (imc <= 24.99) console.log("Parabéns você é uma pessoa saúdavel ");
if (imc <= 29.99)
  console.log("Já esta na hora de você querer perder uns quilos não acha?");
if (imc >= 30)
  console.log(
    "Rapaz tu tá obeso mermão vai pra academia faz caminhada sla so não fica parado comendo salgadinho "
  );

if (idade < 18)
  console.log(
    "Hum tu e novinho deve tá brincando de esconde esconde o epoca boa "
  );

if (idade === 18)
  console.log(
    "Parabéns você saiu do modo tutorial agora se tá lascado pode começar a procurar emprego kkkkkkkkkkkk"
  );
if (idade >= 50)
  console.log(
    "Tu e doido mano se tá velho já em você já consegui a lancha pra pegar as novinhas? kkkkkkkkk"
  );
