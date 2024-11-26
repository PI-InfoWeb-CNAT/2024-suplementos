$(document).ready(function() {
    $(".button-add-carrinho").click(function() {
        var produtoId = $(this).data('produto-id');
        
        $.ajax({
            url: "{% url 'carrinho' %}",  
            data: {
                'produto_id': produtoId,
                'csrfmiddlewaretoken': '{{ csrf_token }}', 
            },
            success: function(response) {
                alert('Produto adicionado ao carrinho!');
            },
            error: function(xhr, errmsg, err) {
                alert('Erro ao adicionar o produto ao carrinho.');
            }
        });
    });
});