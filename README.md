"# AutomacaoConsultasCnpj" 

Como Usar Usando o Executável

**Preparação da Planilha:**

Abra o arquivo **ListaCnpj.xlsx** em sua planilha de escolha (por exemplo, Microsoft Excel, Google Sheets).
Na coluna **"Cnpj"**, insira a lista de CNPJs que você deseja consultar.
Certifique-se de que os CNPJs contenham apenas **números, sem pontos, barras ou traços.**

**Execução do Executável:**

Execute o executável **ConsultasCnpj.exe**.
Você pode fazer isso simplesmente dando um duplo clique no arquivo **ConsultasCnpj.exe** no seu sistema operacional.
OU
Se preferir executar a partir do terminal ou prompt de comando, navegue até a pasta onde o executável está localizado e execute o seguinte comando:

**ConsultasCnpj.exe**

O executável lerá automaticamente a lista de CNPJs do arquivo **ListaCnpj.xlsx** e consultará as informações de cada CNPJ através da API externa.

**Resultados:**

Os dados de CNPJ serão coletados e salvos em um arquivo chamado **dados_cnpjs.json**.
O arquivo **dados_cnpjs.json** conterá informações detalhadas de todos os CNPJs listados na planilha.

**Atualizações:**

Se você executar o executável novamente com uma lista de CNPJs atualizada na planilha, o arquivo dados_cnpjs.json será substituído pelos novos dados.
Isso significa que, se um CNPJ tiver sido atualizado desde a última consulta, o arquivo dados_cnpjs.json conterá as informações mais recentes.




**Usando o Arquivo Python**

**Preparação da Planilha:**

Abra o arquivo **ListaCnpj.xlsx** em sua planilha de escolha (por exemplo, Microsoft Excel, Google Sheets).
Na coluna "Cnpj", insira a lista de CNPJs que você deseja consultar. Certifique-se de que os CNPJs contenham apenas **números, sem pontos, barras ou traços**.
**Execução do Arquivo Python:**

Abra o terminal ou prompt de comando.

Navegue até a pasta onde o arquivo **ConsultasCnpj.py** está localizado.

Execute o seguinte comando:


**python ConsultasCnpj.py**

O script Python lerá a lista de CNPJs do arquivo **ListaCnpj.xlsx** e consultará as informações de cada CNPJ através da API externa.

**Resultados:**

Os dados de CNPJ serão coletados e salvos em um arquivo chamado **dados_cnpjs.json**.
O arquivo **dados_cnpjs.json** conterá informações detalhadas de todos os CNPJs listados na planilha.
Atualizações:

Se você executar o script Python novamente com uma lista de CNPJs atualizada na planilha, o arquivo dados_cnpjs.json será substituído pelos novos dados.
Isso significa que, se um CNPJ tiver sido atualizado desde a última consulta, o arquivo dados_cnpjs.json conterá as informações mais recentes.
