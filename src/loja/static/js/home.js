document.getElementById('formPesquisa').addEventListener('submit', function(event) {
    event.preventDefault()

    const inputPesquisa = document.querySelector('.input-pesquisa').value

    if (inputPesquisa.trim() !== '') {
        document.getElementById('containerMid').style.display = 'none'

        history.pushState(null, '', `?produto=${inputPesquisa}`)
        
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(window.location.href, {
            headers: {
                'x-requested-with': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken,
            }
        })
        .then(response => response.text())
        .then(data => {
            document.querySelector('.pesquisa .produtos').innerHTML = data
        })
        .catch(error => {
            console.error('Erro na pesquisa:', error)
        })

        return false
    }
})