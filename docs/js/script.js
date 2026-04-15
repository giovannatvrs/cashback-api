const form = document.getElementById("form-cashback");

const API_URL = window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost"
    ? "http://127.0.0.1:8000"
    : "https://cashback-api-production-43b9.up.railway.app";

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const valorInput = document.getElementById("valor-compra").value.replace(",", ".");
    const descontoInput = document.getElementById("percentual-desconto").value.replace(",", ".");

    const valor = parseFloat(valorInput);
    const tipo = document.getElementById("tipo-cliente").value;
    const desconto = parseFloat(descontoInput);

    if (isNaN(valor) || valor <= 0) {
        showNotification("Valor da compra inválido", "error");
        return;
    }

    if (isNaN(desconto) || desconto < 0 || desconto > 100) {
        showNotification("Desconto deve estar entre 0 e 100%", "error");
        return;
    }

    const descontoFinal = isNaN(desconto) ? 0 : desconto;

    const response = await fetch(`${API_URL}/cashback/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            tipo_cliente: tipo,
            valor_compra: valor,
            percentual_desconto: descontoFinal
        })
    });

    if (!response.ok) {
        const erro = await response.json();
        alert(erro.detail || "Erro ao calcular cashback");
        return;
    }
    await carregarHistoricoConsultas();

    showNotification("Cashback calculado", "success");


    const data = await response.json();

    document.getElementById("resultado").innerText =
        `Cashback: R$ ${Number(data.cashback).toFixed(2)}`;

    document.getElementById("valor-compra").value = "";
    document.getElementById("percentual-desconto").value = "";
    document.getElementById("tipo-cliente").value = "Comum";
});

async function carregarHistoricoConsultas() {
    const response = await fetch(`${API_URL}/cashback/consultas`);
    const data = await response.json();

    const tbody = document.querySelector("#tabela-consultas tbody");
    tbody.innerHTML = "";

    data.forEach(consulta => {
        const row = `<tr>
            <td class="texto" data-label="Tipo de Cliente">${consulta.tipo_cliente}</td>
            <td data-label="Valor da Compra">R$ ${Number(consulta.valor_compra).toFixed(2)}</td>
            <td data-label="Valor Final">R$ ${Number(consulta.valor_final).toFixed(2)}</td>
            <td data-label="Cashback">R$ ${Number(consulta.cashback).toFixed(2)}</td>
            <td class="data" data-label="Data">${formatarData(consulta.data_consulta)}</td>
        </tr>`;
        tbody.innerHTML += row;

    });
}

document.addEventListener("DOMContentLoaded", carregarHistoricoConsultas);

function formatarData(dataISO) {
    if (!dataISO) return "-";

    const iso = dataISO.includes("Z") || dataISO.includes("+")
        ? dataISO
        : dataISO + "Z";

    const data = new Date(iso);

    if (isNaN(data)) return "Data inválida";

    return data.toLocaleString("pt-BR", {
        timeZone: "America/Sao_Paulo",
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    });
}

function showNotification(message, type = "success") {
    const notif = document.getElementById("notif");

    notif.textContent = message;
    notif.className = type;
    notif.style.display = "block";

    setTimeout(() => {
        notif.style.display = "none";
    }, 3000);
}