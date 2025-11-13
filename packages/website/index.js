// API Endpoints
const COMIDA_API_URL = "<yep>/v1/get-comidas";
const SELECCION_API_URL = "<yep>/v1/set-seleccion";

// Elementos del DOM
const comidasSelect = document.getElementById("comida-select");
const votarBtn = document.getElementById("votar-btn");
const mensajeDiv = document.getElementById("mensaje");

// Cargar comidas al iniciar la página
document.addEventListener("DOMContentLoaded", async () => {
  await cargarComidas();
});

// Función para obtener lista de comidas desde el API
async function cargarComidas() {
  try {
    const response = await fetch(COMIDA_API_URL, {
      method: "GET",
    });

    if (!response.ok) {
      throw new Error(`Error al cargar comidas: ${response.status}`);
    }

    const data = await response.json();

    const comidas = data || [];

    comidasSelect.innerHTML = '<option value="">Seleccionar</option>';

    comidas.forEach((comida) => {
      const option = document.createElement("option");
      option.value = comida.nombre;
      option.textContent = comida.nombre;
      comidasSelect.appendChild(option);
    });
  } catch (error) {
    console.error("Error:", error);
    mostrarMensaje("Error al cargar las opciones de comida", "error");
  }
}

// Función para enviar el voto
async function enviarVoto(comidaSeleccionada) {
  try {
    const response = await fetch(SELECCION_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        comida: comidaSeleccionada,
        timestamp: new Date().toISOString(),
      }),
    });

    if (!response.ok) {
      throw new Error(`Error al enviar voto: ${response.status}`);
    }

    const data = await response.json();

    mostrarMensaje("¡Voto registrado exitosamente!", "success");

    // Limpiar selección después de 2 segundos
    setTimeout(() => {
      comidasSelect.value = "";
      mensajeDiv.textContent = "";
      mensajeDiv.className = "mensaje";
    }, 2000);

    return data;
  } catch (error) {
    console.error("Error:", error);
    mostrarMensaje(
      "Error al registrar el voto. Por favor intente nuevamente.",
      "error"
    );
  }
}

// Función para mostrar mensajes al usuario
function mostrarMensaje(texto, tipo) {
  mensajeDiv.textContent = texto;
  mensajeDiv.className = `mensaje ${tipo}`;
}

// Event listener para el botón de votar
votarBtn.addEventListener("click", async () => {
  const comidaSeleccionada = comidasSelect.value;

  if (!comidaSeleccionada) {
    mostrarMensaje("Por favor seleccione una comida antes de votar", "error");
    return;
  }

  // Deshabilitar botón mientras se procesa
  votarBtn.disabled = true;
  votarBtn.textContent = "Enviando...";

  await enviarVoto(comidaSeleccionada);

  // Rehabilitar botón
  votarBtn.disabled = false;
  votarBtn.textContent = "Votar";
});
