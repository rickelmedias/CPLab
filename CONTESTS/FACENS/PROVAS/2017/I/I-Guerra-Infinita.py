# Informações das joias de acordo com exercicio
gems = [("espaco", 200), ("mente", 160), ("alma", 160), ("realidade", 200), ("tempo", 170), ("poder", 170)]

# Variavel para guardar o caminho conforme for encontrando o melhor 
path = []

powerThanos=0 # Poder do Thanos
powerDefensors=[] # Poder dos Oponentes (Defensores Das Joias)

"""
    Classe de Defensor, ele possui:

    - Poder
    - Joia (Nome da Joia)
    - Poder Joia (Poder da Joia)
"""
class Defensor: 
    def __init__(self, power, gem, gemPower):
        self._power = power
        self._gem = gem
        self._gemPower = gemPower

    def getPower(self):
        return self._power
    
    def getGemName(self):
        return self._gem

    def getGemPower(self):
        return self._gemPower
    
"""
    Função recursiva que fica rodando com o poder atual do Thanos a cada vez que ele pega uma joia nova

    A regra utilizada para definir a proxima joia é:

    1. Verificar se Thanos pode derrotar algum Defensor.

    2. Se Thanos pode derrotar mais de um Defensor, então:
        
        Os dois defensores possuem o mesmo poder de joias?

        Sim, as joias tem mesmo poder
            - Será derrotado primeiro o oponente com a joia com menor ordem lexicográfica .

        Não, as joias tem poder diferente
            - Será derrotado primeiro oponente com a joia mais poderosa será derrotado primeiro
"""
def findThanosPath(currentPower):
    possiblePath = None
    i=0

    while i < len(powerDefensors):
        defensor = powerDefensors[i]

        thanosCanWin = currentPower - defensor.getPower() >=0 
        if thanosCanWin:
            if possiblePath is None:                
                possiblePath = (i, defensor)
            else:
                currentGemIsBetterThanOther = possiblePath[1].getGemPower() < defensor.getGemPower()
                currentGemIsEqualsThanOther = possiblePath[1].getGemPower() == defensor.getGemPower()
                currentGemIsLexicalMinor =  defensor.getGemName() <possiblePath[1].getGemName()
                if currentGemIsBetterThanOther or (currentGemIsEqualsThanOther and currentGemIsLexicalMinor):
                    possiblePath = (i, defensor)

        i+=1

    if possiblePath is not None:
        powerDefensors.pop(possiblePath[0])    
        if len(powerDefensors) >= 0:
            defensorPossible = possiblePath[1]
            path.append(defensorPossible.getGemName())
            findThanosPath(currentPower+defensorPossible.getGemPower())

"""
    Função para mostrar o resultado formatado de acordo com a saída

    Detalhe:
    - Caso o caminho do Thanos (path) tenha 5 ou menos joias, significa que Thanos 
    não conseguiu percorrer as 6 joias, ou seja, ele teve alguma derrota
"""
def printPath(path):
    if len(path) == 6:
        str=""
        for i in range(len(path)):
            str+=path[i]
            if i != len(path)-1:
                str+=" "
        print(str)
    else:
        print("Precisamos de mais poder antes dessa guerra!")

index = 0


"""
    Execução do Código
"""
while True:
    lineIntegers = list(map(int, input().split()))
    
    if (lineIntegers[0] == -1):
        break

    if index==0:
        powerThanos = sum(lineIntegers)
    else:
        powerDefensors.append(Defensor(sum(lineIntegers), gems[index-1][0], gems[index-1][1]))
    
    if index==6:
        # Funcao recursiva que executa ate achar o caminho possivel/impossivel do Thanos, começando pelo Thanos
        findThanosPath(powerThanos)
        # Printar o resultado do caminho para esse caso
        printPath(path)
        # Reseta para fazer o proximo caso
        path = []
        powerDefensors=[]
        index = 0
    else:
        index+=1
