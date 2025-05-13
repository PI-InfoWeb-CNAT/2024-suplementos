document.getElementById('formPesquisa').addEventListener('submit', function(event) {
    event.preventDefault()

    const inputPesquisa = document.querySelector('.input-pesquisa').value

    if (inputPesquisa.trim() !== '') {
        document.getElementById('containerMid').style.display = 'none'
        document.getElementById('loading').style.display = 'flex';

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
        .finally(() => {
            document.getElementById('loading').style.display = 'none';
        });

        return false
    }
})

const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
if (successMessage) {
    setTimeout(function() {
        window.location.href = homeUrl
    }, 2000)
} else if (errorMessage) {
    setTimeout(function() {
        window.location.href = homeUrl
    }, 2000)
} 