## 1 Arquiteturas (a), (b) e (c) podem ser consideradas sistemas distribuídos?

*Um sistema distribuído é um conjunto de elementos que se comunicam através de uma rede de interconexão, utilizando software de sistema distribuído, em que cada elemento tem um ou mais processadores e memórias próprias.*

A. Não é considerado um sistema distribuído, pois trata-se de arquitetura paralela de memória compartilhada. Aqui, não há independência de memória entre os processadores.

Correção: É considerado sim um sistema distribuido, pois apesar de ter uma memória compartilhada no subsistema, não existe uma memória global, para o sistema.

B. Não é considerado sistema distribuído, pois ainda depende de uma única memória global acessível por todos. Configura-se mais como multiprocessadores paralelos.

C. Sim, essa é considerada sistema distribuído, pois cada processador possui sua memória local e a comunicação ocorre via rede de interconexão, atendendo à definição do curso.

---

## 2 Ausência de um clock global

A falta de um relógio global complica o projeto de sistemas distribuídos, pois dificulta o ordenamento de eventos entre processos distribuídos, impossibilita definir de forma absoluta quando algo ocorreu em diferentes nós e gera problemas em operações que dependem de sincronização de tempo (ex.: timestamps, consistência de dados, mensagens em ordem correta).

Exemplo: um processo pode registrar que enviou uma mensagem “às 12:10”, enquanto outro a recebeu “às 12:09:30” — sem clock global, a sequência lógica fica comprometida.

---

## 3 Diferenças entre as arquiteturas

* a) Cluster x Supercomputador

  * *Supercomputador*: arquitetura específica e proprietária, muito cara, de alto desempenho (ex.: Fugaku, El Capitan).
  * *Cluster*: conjunto de computadores completos interconectados, geralmente com hardware comum de mercado e software livre (TCP/IP, Linux, MPI).

* b) Cluster x Grid

  * *Cluster*: ambiente homogêneo, dedicado, com rede de baixa latência.
  * *Grid*: ambiente heterogêneo, dinâmico, não dedicado, formado por organizações virtuais que compartilham recursos quando ociosos.

* c) Grid x Supercomputador

  * *Supercomputador*: sistema único, integrado e proprietário, de altíssimo custo.
  * *Grid*: infraestrutura formada por vários recursos independentes, interligados via internet, mais flexível mas menos estável em desempenho.

* d) Grid x Cloud

  * *Grid*: foco em compartilhamento colaborativo de recursos de diferentes instituições.
  * *Cloud*: evolução do grid, mas baseada em modelo econômico (pay-per-use), data centers centralizados, virtualização e serviços sob demanda.

* e) Cluster x Cloud

  * *Cluster*: conjunto de computadores completos, interconectados por rede de baixa latência, geralmente homogêneos, dedicados e vistos como um único recurso computacional.
  * *Cloud*: evolução dos sistemas distribuídos, baseada em grandes data centers centralizados, uso intensivo de virtualização e modelo de negócio *pay-per-use*.

---

## 4 Quais arquiteturas de (3) podem ser consideradas sistemas distribuídos?

* Cluster: Sim, pois envolve múltiplos computadores autônomos interconectados e que podem ser vistos como um único sistema.
* Grid: Sim, é um paradigma de sistemas distribuídos em grande escala, com máquinas heterogêneas conectadas por rede.
* Cloud: Sim, é uma evolução dos sistemas distribuídos, baseada em virtualização e serviços sob demanda.
* Supercomputador: Em geral, não. Se for arquitetura MPP (Massively Parallel Processor), pode ser considerado apenas paralelo, não necessariamente distribuído, pois pode usar interconexão de memória sem independência de cada nó.

Containers rodando numa maquina só não é considerado um sistema distribuido perante a visao utilizada no curso
