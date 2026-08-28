const formulario =
    document.getElementById("formProduto");
const tabela =
    document.getElementById("tabelaProdutos");
const mensagem =
    document.getElementById("mensagem");
formulario.addEventListener(
    "submit",
    function (event) {
        event.preventDefault();
        const nome =
            document.getElementById("nome")
                .value
                .trim();
        const categoria =
            document.getElementById("categoria")
                .value;
        const quantidade =
            Number(
                document.getElementById("quantidade")
                    .value
            );
        const preco =
            Number(
                document.getElementById("preco")
                    .value
            );
        const fabricante =
            document.getElementById("fabricante")
                .value
                .trim();
        if (nome.length < 3) {
            mensagem.textContent =
                "Erro: o nome deve possuir pelo menos 3 caracteres.";
            return;
        }
        if (categoria === "") {
            mensagem.textContent =
                "Erro: selecione uma categoria.";
            return;
        }
        if (quantidade < 1) {
            mensagem.textContent =
                "Erro: a quantidade deve ser maior ou igual a 1.";
            return;
        }
        if (preco <= 0) {
            mensagem.textContent =
                "Erro: o preço deve ser maior que zero.";
            return;
        }
        if (fabricante.length < 2) {
            mensagem.textContent =
                "Erro: o fabricante deve possuir pelo menos 2 caracteres.";
            return;
        }
        const linha =
            document.createElement("tr");
        const colunaNome =
            document.createElement("td");
        const colunaCategoria =
            document.createElement("td");
        const colunaQuantidade =
            document.createElement("td");
        const colunaPreco =
            document.createElement("td");
        const colunaFabricante =
            document.createElement("td");
        const colunaAcoes =
            document.createElement("td");
        colunaNome.textContent =
            nome;
        colunaCategoria.textContent =
            categoria;
        colunaQuantidade.textContent =
            quantidade;
        colunaPreco.textContent =
            preco.toLocaleString(
                "pt-BR",
                {
                    style: "currency",
                    currency: "BRL"
                }
            );
        colunaFabricante.textContent =
            fabricante;
        const botaoExcluir =
            document.createElement("button");
        botaoExcluir.textContent =
            "Excluir";
        botaoExcluir.classList.add(
            "botao-excluir"
        );
        botaoExcluir.addEventListener(
            "click",
            function () {
                linha.remove();
                mensagem.textContent =
                    "Produto excluído.";
            }
        );
        colunaAcoes.appendChild(
            botaoExcluir
        );
        linha.appendChild(
            colunaNome
        );
        linha.appendChild(
            colunaCategoria
        );
        linha.appendChild(
            colunaQuantidade
        );
        linha.appendChild(
            colunaPreco
        );
        linha.appendChild(
            colunaFabricante
        );
        linha.appendChild(
            colunaAcoes
        );
        tabela.appendChild(
            linha
        );
        mensagem.textContent =
            "Produto cadastrado com sucesso.";
        formulario.reset();
    }
);