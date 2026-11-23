# Orça Obra

Sistema de orçamentos para construção de casas. Ele funciona inteiro no navegador, sem instalação e sem servidor.

## Como usar

- **No computador:** baixe o repositório e abra o `index.html` no Chrome, Edge ou Firefox. Os dados ficam salvos no próprio navegador. Use o botão **Backup** com frequência.
- **Online:** a mesma versão está publicada como página no claude.ai. Lá os dados ficam salvos na sua conta.
- **Site próprio (opcional):** ative o GitHub Pages neste repositório (Settings → Pages → branch principal, pasta raiz). O `index.html` vira o seu site.

## O que ele faz

| Seção | Função |
|---|---|
| **Orçamentos** | Planilha por etapas (preliminares, fundação, estrutura, alvenaria, cobertura, instalações, revestimentos, esquadrias, pintura e complementares) com código, unidade, quantidade e preço unitário. Calcula BDI, desconto, preço de venda e R$/m², e confere o total com o CUB. Tem situação do orçamento (rascunho, enviado, aprovado, recusado), opção de duplicar e exportação da planilha em CSV. |
| **Proposta** | Gera a proposta comercial com o cabeçalho da sua empresa, o objeto, os valores por etapa (resumidos ou detalhados), as condições de pagamento, a validade e o espaço para assinaturas. Baixe o arquivo e use Imprimir → Salvar como PDF. |
| **Levantamento** | Recebe as medidas dos cômodos e calcula piso, paredes, reboco, cerâmica, forro, telhado, portas e janelas, com um desenho isométrico esquemático. Envia as quantidades direto para um orçamento. |
| **Preços** | Catálogo editável de serviços. Importa CSV (`código; descrição; unidade; preço; grupo`), por exemplo uma planilha do SINAPI exportada do Excel. |
| **Minha empresa** | Dados da empresa, BDI padrão, validade, condições, exclusões e valores do CUB. |

> ⚠️ Os preços do catálogo e os valores do CUB que vêm de fábrica são **aproximados** e servem só como ponto de partida. Antes de enviar qualquer proposta, atualize os preços com o SINAPI (Caixa) do seu estado e o CUB do Sinduscon local, ou use os seus custos reais.

## Estrutura

- `app/orcamento.html`: código-fonte (HTML, CSS e JS num único arquivo).
- `app/build.sh`: gera o `index.html` completo a partir do código-fonte.
- `index.html`: versão pronta para abrir no navegador.

## Projetos de referência no GitHub

Estes projetos serviram de inspiração e são bons para se aprofundar:

- [LAMP-LUCAS/AutoSINAPI](https://github.com/LAMP-LUCAS/AutoSINAPI): baixa e organiza as tabelas do SINAPI.
- [rg3915/orcamentos](https://github.com/rg3915/orcamentos): controle de orçamentos em Django.
- [datadrivenconstruction/QuantityTakeoff-Python](https://github.com/datadrivenconstruction/QuantityTakeoff-Python): quantitativos a partir de modelos BIM/IFC.
- [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) (Bonsai/BlenderBIM) e [FreeCAD](https://github.com/FreeCAD/FreeCAD): modelagem 3D/BIM gratuita.
