let $btnLogin = document.getElementById('login');
let $btnCadastro = document.getElementById('cadastro');

$btnLogin.addEventListener('click', function(){
    window.location = 'signin.html';
});

$btnCadastro.addEventListener('click', function(){
    window.location = 'signup.html';
});