# ***Game of Eons***
## **Projeto Realizado por:**

### Daniel Fernandes (a22202501) e Vasco Caleiro (a22203051)

1. *Daniel Fernandes* (a22202501)
     - Final Main
    - Attack
    - Team
2. *Vasco Caleiro* (a22203051)
     - Primeira Iteração do Main
    - Characters
    - Spells   
    - Condition
------------------------------    
## **Desenvolvimento**


## O projeto é constituído por vários ficheiros:
- O ficheiro principal é o “main” onde se definem as funções complementares, as estruturas de dados principais e que também contém o código da execução do jogo propriamente dito que inclui:
    - Fluxo do Combate (Rounds) 
        -  Initiative Phase
        - Action Phase
            - Attack
             - Magic
     - Personagens
         - Valores iniciais das características das personagens
- O ficheiro “main” importa de outros ficheiros (classes): “character”, “spell”, “spellname”, ”condition”, “team”. 
- O ficheiro “character” é composto pela classe mais importante pois define as caracteristicas e condições das personagens utilizadas no jogo, além de conter funções úteis e relevantes;
- O ficheiro “spell” é uma classe que contém as funções das ações dos vários feitiços implementados no jogo;
- O ficheiro “spellname” serve para simplesmente definir os nomes dos feitiços para uma mais fácil utilização dos mesmos;
- O ficheiro “condition” tal como o “spellname”  define os nomes das condições possíveis nas variadas personagens;
- O ficheiro “team” define apenas as duas equipas existentes (do jogador e do computador) sendo os personagens distribuídos pelas duas equipas no “main”.


### **Referências**
https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html
-Usado para organizar elementos de acordo com o "turn_order"
https://www.w3schools.com/python/python_classes.asp
-Usado para determinar classes
https://www.geeksforgeeks.org/python-initialize-empty-array-of-given-length/
-Usado para uma melhor compreensão de "array's"
https://codereview.stackexchange.com/questions/264123/python-text-game-combat-system-with-enemies-in-the-same-position
-Usado para uma melhor compreensão de um sistema de combate 
https://www.geeksforgeeks.org/__init__-in-python/
-Usado para classes e funções
https://stackoverflow.com/questions/66361723/python-insertion-selection-sort-2d-arrays
-Usado para a junção de dois "arrays"