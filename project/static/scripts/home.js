function mostrarErro(texto) {
    const toast = document.getElementById("toast");

    toast.textContent = texto;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
}

function abrirModal() {
    document.getElementById('modal-campanha').classList.add('show');
}

function fecharModal() {
    document.getElementById('modal-campanha').classList.remove('show');
}

async function salvarCampanha() {
    if (!document.getElementById('nome').value.trim() || !document.getElementById('mestre').value.trim()) {
        mostrarErro('A campanha deve ter um nome e um mestre.');
        return;
    }

    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;
    const mestre = document.getElementById('mestre').value;
    const dataInicio = document.getElementById('data-inicio').value || null;
    const dataFim = document.getElementById('data-fim').value || null;

    const resposta = await fetch('/campanha/criar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            nome,
            descricao,
            mestre,
            dataInicio,
            dataFim
        })
    });

    if (resposta.ok) {
        location.reload();
    }
}

let campanhaSelecionada = null;
function abrirModalExcluir(id) {
    campanhaSelecionada = id;
    document.getElementById('modal-confirmar').classList.add('show');
}

function mostrarSucesso(texto){
    const toast = document.getElementById("toast-sucesso");
    toast.innerHTML = "✅ " + texto;
    toast.classList.add("show");
    setTimeout(()=>{
        toast.classList.remove("show");
    },3000);
}

async function confirmarExclusao() {
    const resposta = await fetch('/campanha/excluir', {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            id: campanhaSelecionada
        })
    });

    if (resposta.ok) {

    document.getElementById('modal-confirmar').classList.remove('show');

    mostrarSucesso("Campanha excluída com sucesso!");
    setTimeout(() => {
        location.reload();
    }, 1000);
    } else {
        document.getElementById('modal-confirmar').classList.remove('show');
        mostrarErro("Erro ao excluir a campanha.");
    }
}