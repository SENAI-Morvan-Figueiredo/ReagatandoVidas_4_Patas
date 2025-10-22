// Aguarda o documento HTML ser completamente carregado antes de tentar manipular os elementos
document.addEventListener('DOMContentLoaded', function() {
    
    // Pega os elementos do HTML pelo ID
    var profileIcon = document.getElementById('profileIcon');
    var dropdownMenu = document.getElementById('dropdownMenu');
    var container = document.querySelector('.profile-menu-container');

    // 1. Função para mostrar/esconder o menu ao clicar no ícone
    if (profileIcon && dropdownMenu) {
        profileIcon.addEventListener('click', function(event) {
            // ESSENCIAL: Impede que o clique suba e ative o listener de fechar menu imediatamente
            event.stopPropagation(); 
            
            // Alterna a classe 'show' (que está no CSS) para exibir ou ocultar
            dropdownMenu.classList.toggle('show');
        });
    }

    // 2. Função para esconder o menu ao clicar fora dele
    document.addEventListener('click', function(event) {
        // Verifica se o menu está visível e se o clique NÃO foi dentro do container do menu
        if (dropdownMenu && container && dropdownMenu.classList.contains('show') && !container.contains(event.target)) {
            dropdownMenu.classList.remove('show');
        }
    });

});