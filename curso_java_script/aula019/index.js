/*
Primitivos (imutáveis) - string, number, boolean, undefined, 
null (bigint, symbol) - Valores copiados

Referência (mutável) - array, object, function - Passados por referência
*/
const a = {
  nome: "Arthur",
  sobrenome: "Nicolas",
};
const b = a;

b.nome = "sung";
a.sobrenome = " jin woo";
console.log(a);
console.log(b);
