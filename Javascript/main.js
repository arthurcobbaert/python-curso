import { products } from "./data.js";
import { listElements } from "./listElements.js";

const divListaProdutos = document.getElementById('div-lista-produtos');
const btnRelevante = document.getElementById('btn-relevante');
const btnHigh = document.getElementById('btn-high');
const btnLow = document.getElementById('btn-low');

// Preciso criar um novo Array para quando clicar no botão, ele renderizar os novos Elementos
listElements(divListaProdutos, products);

btnRelevante.addEventListener('click', () => {
    // a - b -> menor numero até o maior número
    // b - a -> vai criar do maior numero até o menor número
    const bestProducts = products.sort((a, b) => b.avaliacao - a.avaliacao);
    listElements(divListaProdutos, bestProducts);
});

btnHigh.addEventListener('click', () => {
    const highPrices = products.sort((a, b) => b.preco - a.preco);
    listElements(divListaProdutos, highPrices);
});

btnLow.addEventListener('click', () => {
    const lowPrices = products.sort((a, b) => a.preco - b.preco);
    listElements(divListaProdutos, lowPrices);
});
