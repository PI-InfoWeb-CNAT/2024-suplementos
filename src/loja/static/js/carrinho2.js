$(document).ready(function() {
    $(".button-add-carrinho").click(function(e) {
        e.preventDefault();  // Previne o envio padrão do formulário

        var produtoId = $(this).data('produto-id');
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();  // Pega o token CSRF do formulário

        $.ajax({
            type: "POST",
            url: urlAdicionarCarrinho,  // Usa a variável com a URL injetada
            
            data: {
                'produto_id': produtoId,
                'csrfmiddlewaretoken': csrfToken,  // Envia o CSRF token
            },
            success: function(response) {
                alert(response.message);  // Exibe mensagem de sucesso
            },
            error: function(xhr, errmsg, err) {
                alert('Erro ao adicionar o produto ao carrinho.');
            }
        });
    });
});
