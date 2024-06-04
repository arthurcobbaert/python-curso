import { products } from "./data.js";

const div = document.getElementById('div-lista-produtos');

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
            </div>
        </div>
    `
};