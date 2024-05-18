const btnCriar = document.querySelector("#btnCriar");
const listaFilmes = document.querySelector("#listaFilmes");
const inputFilme = document.querySelector("#inputFilme");

btnCriar.addEventListener("click", function (infosDoEvento){
    infosDoEvento.preventDefault();
    let novoFilme = document.createElement("li");
    novoFilme.innerHTML = inputFilme.value;

    let btnEditar = document.createElement("button");
    btnEditar.innerText = "<i class = 'fa- solid fa-pen-to-square'></i> <span>Editar</span>";
    btnEditar.addEventListener("click", function (){
        novoFilme.style.color = "red";
        novoFilme.classList.toggle("item-lista");
    })
    novoFilme.append(btnEditar);

    listaFilmes.append(novoFilme);

    /*
    novoFilme.innerHTML = `
        <h1>${inputFilme}</h1>
        <p>Avaliação: xxx</p>
        <span>Lorem ispu</span>
    `;

    let img = document.createElement("img");
    img.src = "link da imagem";
    */

    inputFilme.value = "";

    /*
    infosDoEvento.target -> Pega o html do objeto que foi criado
    infosDoEvento.target.id -> Pega o id do elemento que foi criado
    infosDoEvento.target.perentNode -> Pega o elemento pai od objeto que foi clicado
    */
});
