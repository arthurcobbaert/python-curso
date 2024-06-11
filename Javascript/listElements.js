export function listElements(div, products) {
    div.innerHTML = "";
    for (const element of products) {
        div.innerHTML += `
            <div class="div-grid-2-listaProdutos">
                <div>
                    <img src="${element.img_capa}" />
                </div>
                <div>
                    <h4>${element.marca}</h4>
                    <p>${element.nome}</p>
                    <p>${element.preco}</p>
                    <p>Número de avaliações: ${element.numeroAvaliacoes}</p>
                    <p>Avaliação: ${element.avaliacao} ⭐</p>
                    <button>Comprar</button>
                </div>
            </div>
        `
    };
};
