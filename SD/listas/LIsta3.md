## 1 Considere o NFS. Que operação deve ser feita antes que o arquivo seja montado pelo cliente?

O cliente deve solicitar ao servidor a montagem do diretório exportado, enviando o path. O servidor, então, verifica permissões e envia uma autorização de manipulação do arquivo.

### Correção
O arquivo tem que ser exportado no servidor. "exportfs"

---

## 2 Em que camada do sistema NFS o cliente decide se o arquivo é local ou remoto?

A decisão é feita na camada do sistema de arquivos virtual (VFS – Virtual File System), que identifica se o vnode aponta para um i-nodo local ou um r-nodo remoto.

### Correção
Sistema de arquivo virtual

---

## 3 Cite a principal razão pela qual o NFS é considerado um sistema em rede e não um sistema verdadeiramente distribuído.

Porque o NFS é stateless (não mantém estado sobre os arquivos abertos) e não garante a mesma semântica de consistência de um sistema totalmente distribuído. Ele apenas compartilha arquivos via rede, sem fornecer um espaço único de nomes e sem controle global de acesso.

### Correção
Porque ele não tem transparencia de localização

---

## 4 O NFS não mantém a mesma semântica do Unix para leitura e escrita de arquivos. Descreva um cenário em que isso ocorre.

No Unix local, dois processos podem abrir o mesmo arquivo e a consistência é garantida pelo kernel.
No NFS, se dois processos em máquinas diferentes acessarem o mesmo arquivo, pode haver inconsistências devido ao cache local. Exemplo: um processo grava no arquivo, mas outro ainda acessa a versão desatualizada de seu cache, gerando resultados incorretos.

### Correção
O problema ébasicamente o nde o m2 espera receber um send de p1 em outra maquina porem ela le o cache salve dentro da maquina2 antes de alterar o arquivo.


---