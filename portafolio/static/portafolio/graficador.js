

const params = new URLSearchParams(window.location.search);
const fechaInicio = params.get("fecha_inicio");
const fechaFin = params.get("fecha_fin");
const portafolio = params.get("portafolio");

async function cargarGraficoPesos() {
    console.log("graficador.js cargado");
    // Endpoint que devuelve Response(listado_pesos)
    const response = await fetch(
        `/api/peso-activos/?fecha_inicio=${encodeURIComponent(fechaInicio)}&fecha_fin=${encodeURIComponent(fechaFin)}&portafolio=${encodeURIComponent(portafolio)}`
    );
    const datos = await response.json();

    // Fechas únicas y ordenadas
    const fechas = [...new Set(datos.map(item => item.fecha))].sort();

    // Activos únicos
    const activos = [...new Set(datos.map(item => item.activo))];

    const colores = [
        "#4E79A7", // Azul
        "#F28E2B", // Naranjo
        "#E15759", // Rojo
        "#76B7B2", // Turquesa
        "#59A14F", // Verde
        "#EDC948", // Amarillo
        "#B07AA1", // Morado
        "#FF9DA7", // Rosado
        "#9C755F", // Café
        "#BAB0AC", // Gris
        "#1F77B4", // Azul intenso
        "#FF7F0E", // Naranjo intenso
        "#2CA02C", // Verde intenso
        "#D62728", // Rojo intenso
        "#9467BD", // Violeta
        "#17BECF", // Cian
        "#8C564B"  // Marrón
    ];

    const datasets = activos.map((activo, index) => {

        const serie = fechas.map(fecha => {
            const registro = datos.find(item =>
                item.fecha === fecha &&
                item.activo === activo
            );

            return registro ? registro.peso : 0;
        });

        return {
            label: activo,
            data: serie,
            fill: true,
            stack: 'pesos',
            tension: 0.3,
            borderWidth: 2,
            borderColor: colores[index % colores.length],
            backgroundColor: colores[index % colores.length] + "66"
        };
    });

    new Chart(document.getElementById("graficoPesos"), {
        type: "line",
        data: {
            labels: fechas,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,

            interaction: {
                mode: "index",
                intersect: false
            },

            plugins: {
                title: {
                    display: true,
                    text: "Distribución de pesos por activo"
                },
                legend: {
                    position: "bottom"
                }
            },

            scales: {
                x: {
                    title: {
                        display: true,
                        text: "Fecha"
                    }
                },
                y: {
                    stacked: true,
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: "Peso"
                    }
                }
            }
        }
    });
}

async function cargarGraficoValores() {
    console.log("graficador.js cargado");
    const datosAPI = await fetch(
        `/api/valor-historico/?fecha_inicio=${encodeURIComponent(fechaInicio)}&fecha_fin=${encodeURIComponent(fechaFin)}&portafolio=${encodeURIComponent(portafolio)}`
    ).then(res => res.json());
    const etiquetasFechas = datosAPI.map(item => item.fecha);
    const valoresVt = datosAPI.map(item => item.valor);

    const ctx = document.getElementById('graficoPortafolio').getContext('2d');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: etiquetasFechas,
            datasets: [
                {
                    label: 'Portafolio',
                    data: valoresVt,
                    borderColor: '#1f77b4', // Color azul para toda la línea
                    borderWidth: 3,
                    fill: false,
                    tension: 0.1,
                    pointBackgroundColor: '#1f77b4',
                    pointBorderColor: '#1f77b4'
                },
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Evolución Histórica del Valor del Portafolio',
                    font: { size: 18, weight: 'bold' }
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Fechas' }
                },
                y: {
                    title: { display: true, text: 'Valor en el tiempo($)' }
                }
            }
        }
    });
}

cargarGraficoPesos();
cargarGraficoValores();
