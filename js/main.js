function redirecionar(input) {
    // Verifica se um arquivo foi selecionado e se o tipo de arquivo é CSV
    if (input.files.length > 0 && input.files[0].name.endsWith(".csv")) {
        // Redireciona o usuário para a outra página
        setTimeout(() => {
            window.location.href = 'usuario.html'
        }, 3000)

    } else {
        alert("Por favor, selecione um arquivo CSV.");
    }
}


//--------------------------------------------------------
let $btnLogin = document.getElementById('login');
let $btnCadastro = document.getElementById('cadastro');
let $btnSair = document.getElementById('btn-sair');

$btnLogin.addEventListener('click', function () {
    window.location = 'signin.html';
});

$btnCadastro.addEventListener('click', function () {
    window.location = 'signup.html';
});

function sair() {
    window.location = 'signin.html';
}

//---------------------------------------------------------
//deve estar no input para o usuário carregar seu dataframe
function handleFileUpload() {
    const input = document.getElementById('input-file');
    const csvData = document.getElementById('csv-data');

    if (input.files.length > 0) {
        const file = input.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            // Aqui você pode processar os dados do arquivo CSV
            const csvContent = e.target.result;

            // Exiba as informações do arquivo CSV na div "csv-data"
            csvData.innerHTML = `<pre>${csvContent}</pre>`;
            csvData.classList.remove('hidden');
        };

        reader.readAsText(file, 'UTF-8');
    }
}

//----GRÁFICOS---------------------------------------------
// Cria o gráfico de área 1 e o exibe no elemento com ID "grafico1"
var fig1 = px.area(df, x = 'months_as_member', facet_col = 'category',
    labels = { 'months_as_member': 'Meses como Membro', 'category': 'Categoria' },
    title = 'Gráfico de Área: Distribuição de Categorias em Relação aos Meses como Membro');
Plotly.newPlot('grafico1', fig1.data, fig1.layout);

// Cria o gráfico de pizza 2 e o exibe no elemento com ID "grafico2"
var fig2 = px.pie(df, names = 'time', values = 'attended', title = 'Distribuição de Atendimentos por Hora do Dia');
Plotly.newPlot('grafico2', fig2.data, fig2.layout);

// Cria o gráfico de dispersão 3 e o exibe no elemento com ID "grafico3"
var fig3 = px.scatter(df_grouped, x = 'day_of_week', y = 'category', size = 'count', color = 'day_of_week',
    color_discrete_map = color_map,
    labels = { 'day_of_week': 'Dia da Semana', 'category': 'Categoria', 'count': 'Contagem' },
    title = 'Gráfico de Dispersão: Correlação entre Dias da Semana e Categorias');
Plotly.newPlot('grafico3', fig3.data, fig3.layout);

// Cria o gráfico de barras 4 e o exibe no elemento com ID "grafico4"
var fig4 = px.bar(df_grouped, x = 'day_of_week', y = 'count', color = 'time',
    labels = { 'day_of_week': 'Dia da Semana', 'count': 'Hora' },
    title = 'Gráfico de Barras: Contagem por Dia da Semana e Hora');
// Adicione o parágrafo de texto
fig4.add_annotation({
    text: maior_periodo,
    x: 0.5,  // Posição x no gráfico (0 a 1)
    y: 1.2,  // Posição y no gráfico (0 a 1)
    showarrow: false,
    font: { size: 14 },
    bgcolor: "lightgray",
    bordercolor: "gray",
    borderwidth: 1,
    borderpad: 4,
    opacity: 0.9
});
Plotly.newPlot('grafico4', fig4.data, fig4.layout);
