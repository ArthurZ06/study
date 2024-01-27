/*
Entre 0 - 11 - Bom dia
Entre 12 - 17 - Bom tarde
Entre 18 - 23 - Bom noite
*/

// If pode ser usado sozinho
// Sempre que utilizo a palavra else, preciso de um if antes
// Eu posso ter vários else ifs na checagem
// So posso ter um else na checagem
// Podemos usar condições sem else if, utilizando apenas if e else

const hora = 19;

// Fiz desta maneira e funcionou

if (hora <= 11) {
  console.log("Bom dia");
} else if (hora <= 17) {
  console.log("Bom tarde");
} else if (hora <= 23) {
  console.log("Boa noite");
} else {
  console.log("Sua hora está errada");
}

// Maneira do curso 

// if (hora >= 0 && hora <= 11) {
//   console.log("Bom dia");
// } else if (hora >= 12 && hora <= 17) {
//   console.log("Bom tarde");
// } else if (hora >= 18 && hora <= 23) {
//   console.log("Boa noite");
// } else {
//     console.log("Sua hora está errada");
//   }
