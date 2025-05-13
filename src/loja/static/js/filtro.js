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
        if (!produtosContainer) return console.error("Erro: Não foi possível encontrar a classe .produtos");
    
        const produtos = Array.from(produtosContainer.children);
    
        const extrairTexto = (el, selector, replaceStr = '') => 
            el.querySelector(selector)?.textContent.replace(replaceStr, '').trim() || '';
    
        produtos.sort((a, b) => {
            const nomeA = extrairTexto(a, '.titulo-produto');
            const nomeB = extrairTexto(b, '.titulo-produto');
            const precoA = parseFloat(extrairTexto(a, '.precoCalculado-produto, .preco-produto', 'R$')) || 0;
            const precoB = parseFloat(extrairTexto(b, '.precoCalculado-produto, .preco-produto', 'R$')) || 0;
            const descontoA = parseFloat(extrairTexto(a, '.promocao', '% OFF')) || 0;
            const descontoB = parseFloat(extrairTexto(b, '.promocao', '% OFF')) || 0;
    
            return {
                "A-Z": () => nomeA.localeCompare(nomeB),
                "Z-A": () => nomeB.localeCompare(nomeA),
                "menor-preco": () => precoA - precoB,
                "maior-preco": () => precoB - precoA,
                "menor-promocao": () => descontoA - descontoB,
                "maior-promocao": () => descontoB - descontoA
            }[tipo]();
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