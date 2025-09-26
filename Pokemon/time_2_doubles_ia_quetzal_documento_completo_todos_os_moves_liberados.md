# Time 2 — Doubles (IA Quetzal)

**Premissas do documento**
- Batalhas **sempre em dupla**.
- **Acesso a todos os moves** (tutors/TMs de todas as gerações) para os Pokémon do time e da sua Box.
- **Sem repetir** nenhum Pokémon do seu “time final” (Incineroar, Flutter Mane, Mega Metagross, Gholdengo, Dracovish, Clefable e swaps ligados).
- **Sem Focus Sash** por risco de perda. Preferência por itens **não consumíveis** ou de baixo impacto caso perdidos.
- Foco em **explorar heurísticas da IA**: flinches (Rock Slide), controle de Speed (Electroweb/Thunder Wave/Glare), debuffs em área (Snarl/Breaking Swipe), **Wide Guard** contra spam de dano em área, e **Taunt/Encore** para travar TR/Setup.

---

## Visão geral do time
| Slot | Pokémon | Função | Item | Habilidade |
|---|---|---|---|---|
| 1 | **Tyranitar** | Setter de areia, anti‑TR/anti‑especial com Snarl | **Smooth Rock** | Sand Stream |
| 2 | **Tinkaton** | Controle primário (Fake Out/Encore/TWave) | **Protective Pads** | Mold Breaker |
| 3 | **Rotom‑W** | Speed control + burn/redução de dano físico | **Leftovers** | Levitate |
| 4 | **Dragapult** | Mitigação de ataque rival + limpeza | **Expert Belt** | Infiltrator/ Clear Body |
| 5 | **Buzzwole** | Breaker físico/sustain + **Wide Guard** | **Punching Glove** | Beast Boost |
| 6 | **Serperior** | Offense utilitário (Glare + snowball) | **Wide Lens** *(ou Miracle Seed)* | Contrary |

> Observação: Itens escolhidos do seu inventário, priorizando **não‑consumíveis**.

---

## Sets detalhados + alternativas (todos os moves liberados)

### 1) Tyranitar — setter de Sand + anti‑TR/anti‑especial
- **Item:** **Smooth Rock**  | **Habilidade:** Sand Stream  | **Nature:** Careful *(ou Adamant se quiser mais KOs)*
- **EVs sugeridos:** **252 HP / 92 Atk / 164 SpD** (sobrevive especiais relevantes; ainda bate forte)
- **Moves (padrão):**
  - **Rock Slide** (spread + chance de flinch, muito bom vs IA)
  - **Snarl** (cai SpA dos 2 alvos; excelente x casters)
  - **Taunt** (nega Trick Room, Calm Mind, Recover, etc.)
  - **Protect**
- **Opções/techs:** **Crunch** (STAB single target), **Low Kick**/**Superpower** (Steels/Normals), **Ice Punch** (Dragões/Ground), **Rock Tomb** (speed control extra).
- **Por que assim?** IA tende a insistir em TR/setup; **Taunt + Snarl** punem esse padrão enquanto **Rock Slide** gera flinches decisivos.

### 2) Tinkaton — controle ativo
- **Item:** **Protective Pads** (evita recoil de Helmet/Rough Skin/Barbs ao usar Fake Out/Hammer)
- **Habilidade:** Mold Breaker  | **Nature:** Jolly  | **EVs:** **252 HP / 4 Atk / 252 Spe**
- **Moves (padrão):**
  - **Fake Out** (garante turno livre pro parceiro)
  - **Gigaton Hammer** (pressão de dano mesmo sem investimento pesado)
  - **Encore** (trava Protect/Setup/TR que escapou do Taunt)
  - **Thunder Wave** (speed control forte vs IA)
- **Opções/techs:** **Taunt** (dobrar negação de TR), **Feint** (quebra Protect), **Knock Off** (remove itens chave), **Play Rough** (coverage Fairy), **Foul Play** (abusa do Atk rival).
- **Por que assim?** **Fake Out + Encore** cria armadilha clássica contra IA, forçando travas e trocas desfavoráveis.

### 3) Rotom‑Wash — speed control + mitigação física
- **Item:** **Leftovers** (sustain constante)  | **Habilidade:** Levitate  | **Nature:** Bold
- **EVs:** **252 HP / 196 Def / 60 Spe** (sobrevive pancadas físicas comuns; passa alguns tiers após **Electroweb**)
- **Moves (padrão):**
  - **Electroweb** (reduz Spe dos 2 oponentes)
  - **Hydro Pump** (STAB forte)
  - **Will‑O‑Wisp** (corta dano físico em 2/3)
  - **Protect**
- **Opções/techs:** **Discharge** (spread elétrico com parceiro Ground/imm une/Protect), **Thunderbolt**, **Volt Switch** (pivô), **Light Screen/Reflect**, **Rain Dance**, **Pain Split** (tutor) para sustain situacional.
- **Por que assim?** IA valoriza força bruta; **Wisp + Electroweb** reduz drasticamente KOs sofridos e garante prioridade ofensiva do seu lado.

### 4) Dragapult — mitigação e cleanup
- **Item:** **Expert Belt** (boost em acertos supereficazes sem lock)
- **Habilidade:** **Infiltrator** *(ou Clear Body se Intimidate for frequente)*  | **Nature:** Jolly
- **EVs:** **252 Atk / 4 SpD / 252 Spe**
- **Moves (padrão):**
  - **Dragon Darts** (pressão consistente em dupla)
  - **Breaking Swipe** (reduz Atk dos 2 rivais; ótimo vs IA física)
  - **Phantom Force** (desalinha turnos/duelos de alvo; punição a Protect)
  - **Protect**
- **Opções/techs:** **U‑turn** (pivô), **Thunder Wave** (layer extra de speed control), **Flamethrower** (misto, Steels/Ferrothorns), **Substitute** (punir Trocas/Protects da IA).
- **Por que assim?** **Breaking Swipe** + **Snarl/Wisp** criam um “tapete” de mitigação que a IA tem dificuldade de contornar.

### 5) Buzzwole — breaker/sustain + **Wide Guard**
- **Item:** **Punching Glove** (buff em socos e evita contato para não ativar habilidades/Helmet)
- **Habilidade:** Beast Boost  | **Nature:** Adamant  | **EVs:** **252 HP / 252 Atk / 4 SpD**
- **Moves (padrão):**
  - **Drain Punch** (sustain e KOs em Steels/Normals)
  - **Ice Punch** (Dragões/Terra/Voador)
  - **Thunder Punch** (Águas/Voador)
  - **Wide Guard** (bloqueia **Rock Slide / Earthquake / Heat Wave / Surf / Muddy Water** em ambos)
- **Opções/techs:** **Protect** (se preferir padrão VGC), **Quick Guard** (bloquear Fake Out/Prio), **Lunge** (−1 Atk no alvo, cuidado com Defiant), **Poison Jab** (Fairies).
- **Por que assim?** A IA adora moves em área; **Wide Guard** vira duelo inteiro quando lido corretamente.

### 6) Serperior — utilitário ofensivo (sem Sash)
- **Item:** **Wide Lens** *(consistência do Leaf Storm)* **ou Miracle Seed** (dano estável)
- **Habilidade:** Contrary  | **Nature:** Timid  | **EVs:** **4 HP / 252 SpA / 252 Spe**
- **Moves (padrão):**
  - **Leaf Storm** (snowball com Contrary)
  - **Glare** (paralisa até elétricos/terras; essencial vs sweepers da IA)
  - **Dragon Pulse** (cobertura segura)
  - **Protect**
- **Opções/techs:** **Substitute** (punir Protect/Trocas), **Leech Seed** (chip + sustain), **Hidden Power [Fire/Ice]** (se disponível) para cobrir Steels/Dragões, **Taunt** (anti‑setup/TR adicional).
- **Por que assim?** **Glare** é um “curinga” universal vs IA; **Leaf Storm** escala rápido e força trocas.

---

## Leads e linhas de T1–T2 (scripts prontos)

### Lead 1 — **Tyranitar + Tinkaton** (segurança/controle)
- **T1:** Fake Out no suporte mais incômodo + **Taunt** no setter/booster. Areia ativa.
- **T2:** **Thunder Wave** no striker mais rápido + **Rock Slide** para chip/flinch; avalie troca para Rotom‑W se houver ameaça física pesada para **Wisp**.

### Lead 2 — **Rotom‑W + Tyranitar** (pressão em área)
- **T1:** **Electroweb** + **Rock Slide**.
- **T2:** **Will‑O‑Wisp** no atacante físico + **Rock Slide**/**Snarl** conforme composição rival.

### Lead 3 — **Dragapult + Tinkaton** (anti‑setup)
- **T1:** Fake Out no redirecionador/Trick Roomer + **Breaking Swipe** (mitiga ambos os alvos).
- **T2:** **Encore** no alvo que usou Protect/Setup + **Dragon Darts** para capitalizar.

### Lead 4 — **Buzzwole + Rotom‑W** (anti‑spread e físicos)
- **T1:** **Wide Guard** se o board indicar Rock Slide/EQ/Heat Wave/Muddy Water; caso contrário, **Wisp** no striker + **Drain Punch** no parceiro mais frágil.
- **T2:** **Electroweb** para manter prioridade + cobertura de socos do Buzzwole.

### Lead 5 — **Serperior + Tinkaton** (controle bruto de Speed)
- **T1:** **Glare** no sweeper + Fake Out no suporte.
- **T2:** **Leaf Storm** (começa o snowball) + **Encore/TWave** no segundo alvo.

---

## Match‑ups típicos da Elite 4 “melhorada” (padrões da IA)

- **Spam de área (Rock Slide / EQ / Heat Wave / Surf / Muddy Water)**
  - Chame **Buzzwole** para **Wide Guard**; mantenha **Protect** no parceiro para ler baits. Rotom‑W pode trocar para segurar dano especial.

- **Trick Room**
  - **Taunt** (Tyranitar/Tinkaton) na abertura. Se TR subir, invista em **Protect** + trocas defensivas e volte a pressionar após 2 turnos; **Encore** pode travar o setter em Trick Room novamente.

- **Chuva**
  - Abra **Rotom‑W + Serperior**: **Electroweb + Glare** t1; entre **Tyranitar** para quebrar clima em janela segura. **Thunder Punch** do Buzzwole pune Waters.

- **Sol**
  - Traga **Tyranitar** para trocar clima; **Dragapult** lida bem com Fire/Grass via **Phantom Force/Darts**; **Wisp** neutraliza sweepers físicos de Fire.

- **Defiant/Competitive (Annihilape/Kingambit/etc.)**
  - Evite Intimidate/Lunge; abuse de **Encore/Taunt/Glare** e **Phantom Force** para desalinhar turnos. **Breaking Swipe** reduz Atk sem ativar Defiant.

- **Redirecionamento (Follow Me/Rage Powder)**
  - **Encore** pune Protect/Follow Me; **Rock Slide/Breaking Swipe** contorna via dano/queda em área; **Phantom Force** ignora redirecionamento em turnos alternados.

---

## Itens — justificativa e alternativas não‑consumíveis
- **Smooth Rock (Tyranitar):** estende areia para chip/SpD boost do TTar.
- **Protective Pads (Tinkaton):** evita danos/habilidades passivas ao usar Fake Out e Hammer.
- **Leftovers (Rotom‑W):** sustain constante em lutas longas.
- **Expert Belt (Dragapult):** flexível, sem lock; valor extra vs alvos em range.
- **Punching Glove (Buzzwole):** aumenta dano e evita contato (segurança vs Helmet/Barbs).
- **Wide Lens / Miracle Seed (Serperior):** consistência do **Leaf Storm** ou dano estável.

> Outras opções viáveis do seu inventário: **Light Clay** (se optar por telas no Rotom‑W), **Rocky Helmet** (punir contato no TTar), **Grassium Z/Electrium Z** em composições específicas (cristais **não são consumidos**).

---

## Rotas de jogo padrão (resumo rápido)
- **Controle primeiro, dano depois:** priorize **TWave/Glare/Electroweb/Breaking Swipe/Snarl** nos 1–2 primeiros turnos; só depois entre com pressão de KOs.
- **Leia o padrão da IA:** se ela “aperta” spread, priorize **Wide Guard**; se ela tenta TR/Setup, **Taunt + Encore**.
- **Proteja e troque sem medo:** a IA raramente pune sequências **Protect → Troca → Protect** se você alternar alvos e manter pressão de status.

---

## Checklist pré‑luta
- Leads marcados para cada match‑up acima.
- Itens equipados conforme tabela.
- Ordem da party com **Rotas de emergência** fáceis: Buzzwole (Wide Guard) e Tyranitar (Taunt/Snarl) nunca muito longe do topo.

---

### Quer versões alternativas?
Posso gerar uma **planilha de speed tiers** (com breakpoints pós‑Electroweb/TWave/Glare) e versões do time com **Z‑Moves** específicos (ex.: Electrium Z no Rotom‑W; Grassium Z no Serperior) mantendo a filosofia **sem Sash**.

