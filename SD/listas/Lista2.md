## 1 O que vem a ser imagem única do sistema?

Imagem única significa que, para o usuário e para o programador, o sistema distribuído deve aparentar ser um sistema único e coeso, mesmo sendo composto por múltiplos computadores conectados em rede. Essa transparência evita que o usuário precise conhecer a localização ou complexidade interna dos recursos .

### Correção
Ilusão de manipular um sistema único quando na realidade se manipula um sistema composto por varias maquinas.

---

## 2 Cite um argumento para a replicação de servidores (do mesmo tipo) em um sistema distribuído.

A replicação de servidores aumenta a tolerância a falhas e melhora a distribuição de carga. Se um servidor falha, outro pode assumir; além disso, múltiplos servidores atendem melhor a vários clientes simultâneos, reduzindo gargalos.

### Correção
Tolerancia a fahas e Distribuição de carga.

---

## 3 Cite dois motivos pelos quais a transparência é interessante em sistemas distribuídos. Cite uma situação na qual a transparência é uma desvantagem.

Motivos:

* Facilita o uso do sistema, já que o usuário não precisa se preocupar com localização dos recursos.
* Garante acesso uniforme, permitindo que recursos locais e remotos sejam acessados da mesma forma.

Desvantagem:
Em alguns casos, a transparência pode mascarar problemas de desempenho. Por exemplo, acessar um arquivo remoto via rede pode parecer idêntico ao acesso local, mas na prática pode ser muito mais lento, causando frustração.

### Correção
Facilidade no uso do sistema, Transparencia de tolerancia a falhas(não é para simplificar o uso, para permitir o uso quando ocorrer a falha) ou Disponibilidade.
Desvantagem: acaba omitindo informações, como falhas ou detalhes


---

## 4 Cite as vantagens de se ter um servidor de nomes centralizado e as vantagens de se ter um servidor de nomes distribuído.

* Servidor de nomes centralizado:

  * Simplicidade na administração.
  * Facilidade de implementação e manutenção.

* Servidor de nomes distribuído:

  * Maior tolerância a falhas, pois não depende de um único ponto central.
  * Melhor escalabilidade, já que múltiplos servidores podem atender consultas simultâneas .

### Correção
* Servidor de nomes centralizado:
    * Não tem problema de coerencia e consistencia, menos mensagens.
* Servidor de nomes distribuído:
    * Tolerencia a falhas
    * Distribuição de carga

---

## 5 Considere a afirmação abaixo. Diga se a mesma está correta ou incorreta e justifique a sua resposta:

“Os timestamps lógicos podem ser utilizados tanto para detectar a perda de mensagens como para garantir que mensagens enviadas por um mesmo nodo sejam recebidas na ordem de envio”.

Resposta: A afirmação está incorreta.

* Os timestamps lógicos servem para ordenar eventos e garantir a ordem relativa entre mensagens (ex.: evitar inversão na ordem de chegada).
* Entretanto, não detectam perda de mensagens, pois uma mensagem perdida simplesmente não gera timestamp no destino. Para perda de mensagens, utilizam-se outros mecanismos, como ACKs (acknowledgements) .

### Correção
Pode ser identificada a perda devido as mensagens posteriores que chegam sem chegar a faltante, nao vai identificar a ultima ou as ultimas mas uma intermediaria pode ser identificada devia as mensagens recebidas