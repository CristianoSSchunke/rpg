function mostrarErro(texto) {
    const toast = document.getElementById("toast");

    toast.textContent = texto;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
}

function abrirModal(nomeModal) {
    document.getElementById(nomeModal).classList.add('show');
}

function fecharModal(nomeModal) {
    document.getElementById(nomeModal).classList.remove('show');
}

function mostrarSucesso(texto){
    const toast = document.getElementById("toast-sucesso");
    toast.innerHTML = "✅ " + texto;
    toast.classList.add("show");
    setTimeout(()=>{
        toast.classList.remove("show");
    },3000);
}