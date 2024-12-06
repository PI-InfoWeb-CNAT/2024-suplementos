const ajudaPopUp = document.querySelector('.ajuda-popup')

function abrir() {
    ajudaPopUp.style.visibility = 'visible'
    ajudaPopUp.style.opacity = '1'
}

function fechar() {
    ajudaPopUp.style.visibility = 'hidden'
    ajudaPopUp.style.opacity = '0'
}
// FILTRO

document.addEventListener("DOMContentLoaded", () => {
    const hoverArea = document.getElementById("selecionarBtn");
    const checkboxBox = document.getElementById("checkboxBox");
    const setinha = document.getElementById("setinha");
    const selecioneText = document.getElementById("Selecione"); 

    checkboxBox.style.display = "none";

    document.addEventListener("click", (event) => {
        const isClickInsideBox = checkboxBox.contains(event.target);
        const isClickInsideButton = hoverArea.contains(event.target);

        if (!isClickInsideBox && !isClickInsideButton) {
            checkboxBox.classList.remove("show");
            checkboxBox.style.display = "none";
            setinha.style.transform = "rotate(0deg)";
        }
    });

    hoverArea.addEventListener("click", () => {
        if (checkboxBox.style.display === "none" || checkboxBox.style.display === "") {
            checkboxBox.style.display = "flex"; 
            checkboxBox.classList.add('show'); 
            setinha.style.transform = "rotate(180deg)";
        } else {
            checkboxBox.classList.remove('show'); 
            checkboxBox.style.display = "none";
            setinha.style.transform = "rotate(0deg)";
        }
    });

    function ordenarProdutos(tipo, texto) {
        const produtosContainer = document.querySelector('.produtos');
        const produtos = Array.from(produtosContainer.children); 

        produtos.sort((a, b) => {
            const nomeA = a.querySelector('.titulo-produto').textContent.trim();
            const nomeB = b.querySelector('.titulo-produto').textContent.trim();
            const precoA = parseFloat(a.querySelector('.preco-produto').textContent.replace('R$', '').trim());
            const precoB = parseFloat(b.querySelector('.preco-produto').textContent.replace('R$', '').trim());
            const descontoA = parseFloat(a.querySelector('.promocao').textContent.replace('R$', '').trim());
            const descontoB = parseFloat(b.querySelector('.promocao').textContent.replace('R$', '').trim());

            if (tipo === "A-Z") {
                return nomeA.localeCompare(nomeB); 
            } else if (tipo === "Z-A") {
                return nomeB.localeCompare(nomeA); 
            } else if (tipo === "menor-preco") {
                return precoA - precoB; 
            } else if (tipo === "maior-preco") {
                return precoB - precoA; 
            } else if (tipo === "menor-promocao") {
                return descontoA - descontoB; 
            } else if (tipo === "maior-promocao") {
                return descontoB -  descontoA; 
            }
        });

        selecioneText.textContent = texto;
        checkboxBox.style.display = "none";
        setinha.style.transform = "rotate(0deg)";

        produtosContainer.innerHTML = '';
        produtos.forEach(produto => produtosContainer.appendChild(produto));
    }

    const filtros = document.querySelectorAll('.checkbox-box .filtro');

    filtros.forEach(filtro => {
        filtro.addEventListener('click', (event) => {
            const filtroTexto = event.target.textContent.trim();

            if (filtroTexto.includes("A-Z")) {
                ordenarProdutos("A-Z", "Ordem alfabética A-Z");
            } else if (filtroTexto.includes("Z-A")) {
                ordenarProdutos("Z-A", "Ordem alfabética Z-A");
            } else if (filtroTexto.includes("Menor preço")) {
                ordenarProdutos("menor-preco", "Menor preço");
            } else if (filtroTexto.includes("Maior preço")) {
                ordenarProdutos("maior-preco", "Maior preço");
            }
             else if (filtroTexto.includes("Menor promoção")) {
                ordenarProdutos("menor-promocao", "Menor promoção");
            } else if (filtroTexto.includes("Maior promoção")) {
                ordenarProdutos("maior-promocao", "Maior promoção");
            }
        });
    });
});


