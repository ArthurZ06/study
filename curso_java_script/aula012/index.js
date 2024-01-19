let varA = 'A' // B
let varB = 'B' // C
let varC = 'C' // A

let copia = varA
varA = varB
varB = varC
varC = copia

//[varA, varB, varC] = [varB, varC, varA]

console.log(varA, varB, varC)


