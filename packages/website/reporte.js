// API Endpoint
const REPORTE_API_URL = "<yep>/get-reporte";

// Elementos del DOM
const tbodyReporte = document.getElementById("tbody-reporte");
const loadingDiv = document.getElementById("loading");
const errorMensaje = document.getElementById("error-mensaje");

// Cargar reporte al iniciar la página
document.addEventListener("DOMContentLoaded", async () => {
  await cargarReporte();
});

// Función para obtener el reporte desde el API
async function cargarReporte() {
  try {
    // Mostrar loading
    loadingDiv.style.display = "block";
    errorMensaje.textContent = "";
    errorMensaje.style.display = "none";

    const response = await fetch(REPORTE_API_URL, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`Error al cargar reporte: ${response.status}`);
    }

    const data = await response.json();

    // Asumiendo que el API retorna { votos: [{comida: "Peruana", cantidad: 10}, ...] }
    const votos = data.votos || [];

    // Ocultar loading
    loadingDiv.style.display = "none";

    // Renderizar tabla
    renderizarTabla(votos);
  } catch (error) {
    console.error("Error:", error);
    loadingDiv.style.display = "none";
    errorMensaje.textContent =
      "Error al cargar el reporte. Por favor intente nuevamente.";
    errorMensaje.style.display = "block";
  }
}

// Función para renderizar la tabla con los datos
function renderizarTabla(votos) {
  // Limpiar tabla existente
  tbodyReporte.innerHTML = "";

  if (votos.length === 0) {
    const tr = document.createElement("tr");
    tr.innerHTML =
      '<td colspan="2" class="no-datos">No hay votos registrados aún</td>';
    tbodyReporte.appendChild(tr);
    return;
  }

  // Agregar filas con los datos
  votos.forEach((voto) => {
    const tr = document.createElement("tr");

    const tdComida = document.createElement("td");
    tdComida.textContent = voto.comida || voto.tipo_comida || "N/A";

    const tdVotos = document.createElement("td");
    tdVotos.textContent = voto.cantidad || voto.votos || 0;
    tdVotos.className = "td-votos";

    tr.appendChild(tdComida);
    tr.appendChild(tdVotos);
    tbodyReporte.appendChild(tr);
  });
}

// Función para refrescar el reporte
async function refrescarReporte() {
  await cargarReporte();
}

// Agregar botón de refresh (opcional)
// Puedes descomentar esto si quieres un botón de actualización
/*
const btnRefresh = document.createElement('button');
btnRefresh.textContent = 'Actualizar';
btnRefresh.className = 'btn-refresh';
btnRefresh.onclick = refrescarReporte;
document.querySelector('.reporte-content').insertBefore(btnRefresh, document.querySelector('.tabla-votos'));
*/
