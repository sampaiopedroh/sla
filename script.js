const pessoas = ["Ana", "Bia", "Caio"];
// printa um elemento da array
console.log(pessoas[1]);

// adicionar um elemento no final da array
pessoas.push("Davi");
console.log(pessoas);

// tira o ultimo elemento da array
pessoas.pop();
console.log(pessoas);

// adiciona um elemento no começo da array
pessoas.unshift("Sla");
console.log(pessoas);

// remover o primeiro elemento da array
pessoas.shift();
console.log(pessoas);

// atualiza um elemento da array
pessoas[2] = "Cadu";
console.log(pessoas);

// for em uma array
pessoas.forEach(
    function passarCadaNome(pessoas){
        console.log(`Olá ${pessoas.toLowerCase()}`);
    }
);

// Arrow function - não precisa de palavra function, nome
pessoas.forEach(pessoas => console.log(`Olá ${pessoas.toLowerCase()}`));


// devolve uma array - poder manipular arrays 
// em variável
const pessoasSla = pessoas.map(elemento => elemento + " SLA");
console.log(pessoas);
// em function
function Sla(){
    return pessoas.map(elemento => elemento + " SLA");
}
console.log(Sla());

function dobrar(listaNums){
    return listaNums.map(elemento => elemento * 2);
}

const nums = [1, 2, 3, 4, 5]
console.log(dobrar(nums));