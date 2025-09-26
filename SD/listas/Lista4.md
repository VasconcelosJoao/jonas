## 1- O que acontece no cliente, em um sistema com ligação dinâmica, se o servidor cai no meio da execução de um procedimento remoto? O que acontece se o cliente executar de novo a mesma função?

Se o servidor cai durante a execução, o cliente não recebe resposta e ficará aguardando até ocorrer timeout. Dependendo da semântica adotada, o cliente pode:

* Executar no mínimo uma vez: esperar o servidor voltar ou redirecionar para outro servidor equivalente e reenviar a solicitação.
* Executar no máximo uma vez: desistir ao expirar o tempo, retornando erro.
* (Essa ak a professora nao considerou como uma possiblidade) Executar de 0 a n vezes: sem garantia, podendo ocorrer múltiplas execuções.

Se o cliente tentar novamente, pode acontecer:

(correção) no minimo uma: pode ser que seja executada um ou duas vezes
* Reexecução do procedimento desde o início, caso o servidor reinicie.
* Inconsistência, se a operação não for idempotente (ex.: transação bancária repetida).




---

## 2- Para cada uma destas aplicações, você escolheria a semântica no mínimo uma ou no máximo uma:

* (a) Leitura e escrita em arquivos: *No mínimo uma vez*, pois a reexecução garante persistência dos dados.
* (b) Compilação de um programa: *No máximo uma vez*, já que recompilar várias vezes não altera o resultado final, mas pode causar sobrecarga.
* (c) Aplicação bancária remota: *No máximo uma vez*, pois repetir operações (ex.: débito) pode gerar inconsistências financeiras graves.

### Correção
* (a) No Máximo Uma
* (b) No Minimo Uma

---

## 3- Suponha que o custo de se fazer uma RPC nula é de 1ms. Cada 1k de dados introduz um custo adicional de 2ms. Quanto tempo levará a leitura de 32 k via uma única RPC? E quanto tempo levarão 32 RPCs de 1k?

* Fórmula: tempo = custo RPC nula + (dados em kB × 2ms)

a) 1 RPC com 32k:
$1ms + (32 × 2ms) = 65ms$

b) 32 RPCs de 1k:
Cada RPC → $1ms + (1 × 2ms) = 3ms$
$32 × 3ms = 96ms$

Resposta:

* 1 RPC → 65ms
* 32 RPCs → 96ms

### Correção

---

## 4- Cite uma situação onde a RPC não é transparente.

A RPC perde transparência quando há falhas de comunicação ou queda de processos. Por exemplo:

* O cliente não localiza o servidor.
* Perda de mensagens na rede.(errado)
* Servidor cai durante a execução e o cliente recebe erro *NOSERVER*, que não ocorreria em uma chamada local.

### Correção
quando a semantica é no maximo uma e o servidor cai, quando o cliente nao localiza o servidor, quando o programador implementa no rpc de baixo nivel


---

## 5- Na implementação da RPC, imagine que o cliente e o servidor estão frequentemente na mesma máquina. Para este caso foi proposta uma implementação de RPC chamada Lightweight RPC, que visa minimizar o número de cópias. Como funciona a Lightweight RPC?

A Lightweight RPC (LRPC) otimiza chamadas locais:

* Cliente e servidor comunicam-se por memória compartilhada em vez de troca de mensagens.
* Argumentos são copiados diretamente para uma pilha compartilhada, evitando múltiplas cópias desnecessárias.
* O kernel apenas realiza a transição de execução entre cliente e servidor, tornando a chamada mais rápida e eficiente.

### Correção
O cliente copia os parametros da rpc para memoria compartilhada, o rpc ativa o servidor e o mesmo acessa diretamente a memoria compartilhada
---