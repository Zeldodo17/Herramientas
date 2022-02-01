const form = document.getElementById('form')
const nombre = document.getElementById('nombre')
const usuario = document.getElementById('username')
const email = document.getElementById('email')
const password = document.getElementById('password')

form.addEventListener('submit', e =>{
    e.preventDefault();
    checkInputs();
})

function checkInputs() {
    const nombreValue = nombre.nodeValue.trim();
    const usuarioValue = usuario.nodeValue.trim();
    const emailValue = email.nodeValue.trim();
    const passwordValue = password.nodeValue.trim();

    if (nombreValue === ''){
        setErrorFor(usuario, 'No puede dejar el usuario en blanco')
    }else{
        setSuccessFor(usuario)
    }
}

function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small =  formControl.querySelector('small')
    formControl.className = 'form-contol error'
    small.innerText = message
}

function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-control success'
}

function isEmail(email){
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

















