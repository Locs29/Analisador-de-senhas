#Importando o módulo regex (Expressão Regular);
import re

#Definindo a função que irá classificar a senha através de um sistema de pontuação;
def verificar_forca_senha(senha):

#Aqui se define o máximo de caracteres que podem ser entrados (15);
#Aqui tmb se define o mínimo de caracteres que podem ser entrados (1);
#Aqui se uma das 2 premissas se confirmar verdadeira, o programa vai dar erro e explicar o porque disso;
    max_caracteres = 15
    if len(senha) > max_caracteres:
        forca = "Erro :P"
        feedback = [f"Ops, aconteceu um erro! Tente uma senha com menos de {max_caracteres} caracteres!"]
        return (forca, feedback)

    if len(senha) == 0:
        forca = "Erro ;-;"
        feedback = ["Você deve começar digitando uma senha para poder verificar se ela é forte..."]
        return (forca, feedback)
    
    pontuacao = 0
    feedback = []
    
    #Aqui se cria uma lista que define palavras comuns de forma constante;
    PALAVRAS_COMUNS = [ "123", "234", "345", "456", "567","678", "789", "890", "abc", "professor",
                      "aluno", "qwerty", "aaa","bbb","ccc","ddd","eee","fff","ggg",
                       "hhh", "iii", "jjj", "kkk","lll", "mmm", "nnn", "ooo", "ppp",
                        "qqq", "rrr", "ttt", "uuu", "vvv", "www", "xxx", "yyy",
                        "zzz"]
    
    #Aqui verificamos se na senha há a presença de palavras comuns;
    #Partimos da premissa que não ha palavras comuns;
    #Mas caso se encontre palavras comuns, o código rapidamente bloqueia;
    #O uso do re.escape serve pro uso de caracteres especiais na senha;
    #Já o re.IGNORECASE, serve para ignorar a presença de minúsculas ou maiúsculas na palavra.
    palavra_encontrada = False
    for palavra_comum in PALAVRAS_COMUNS:
        if re.search(re.escape(palavra_comum), senha, re.IGNORECASE):
            palavra_encontrada = True
            break
    
    #Aqui se dá uma punição de 2 pontos (-2) e também dá uma orientação do porque disso ocorrer e o que deve alterar.
    if palavra_encontrada:
        pontuacao -= 2
        feedback.insert (0, f"Cuidado! Sua senha está vulnerável a ataques de dicionário,ela contém a palavra comum: {palavra_comum}")
        feedback.insert (1, "Busque não usá-la, ou pelo menos substitua as vogais por números ou símbolos ")
        feedback.insert (2, "Você sofreu a penalidade [- 2 pontos]")
        feedback.insert (3, "=" * 70)
        

#Aqui começa o sistema de pontuação, tudo vale 1 ponto, mas a quant. de caracteres pode valer até 2 pts;
    #Comprimento básico: mínimo 8 caracteres (2 pts se >= 12);
    if len(senha) >= 8:
        feedback.append("Atende ao comprimento básico de 8 ou mais caracteres.")
        
        #Comprimento avançado: mínimo 12 caracteres, o [-1] indica a substituição do .append (último item da lista) que defini anteriormente caso a premissa for verdadeira;
        #Se nada for confirmado verdadeira, o último item será substituido por uma mensagem de orientação do mínimo de caracteres necessários para se poder pontuar nesse requisito;
        if len(senha) >= 12:
            pontuacao += 2
            feedback[-1] = "Atende ao comprimento avançado de 12 ou mais caracteres). [+2 pontos]" # Atualiza o feedback
        else:
            pontuacao += 1
            feedback[-1] = "Atende ao comprimento básico de 8 a 11 caracteres. [+1 ponto]"

    else:
        feedback.append("A senha deve ter no mínimo 8 caracteres para começar a pontuar.")

    #Letras maiúsculas, aq se usa a raw string para o uso do padrão regex de verificar de A até Z;
    if re.search(r"[A-Z]", senha):
        pontuacao += 1
        feedback.append("Inclui letra maiúscula. [+1 ponto]")
    else:
        feedback.append("Falta letra maiúscula (A-Z).")

    #Letras minúsculas, mesma coisa, só que com letras minúsculas;
    if re.search(r"[a-z]", senha):
        pontuacao += 1
        feedback.append("Inclui letra minúscula. [+1 ponto]")
    else:
        feedback.append("Falta letra minúscula (a-z).")

    #Números, aqui se utiliza o padrão regex "\d" para indicar os números;
    if re.search(r"\d", senha):
        pontuacao += 1
        feedback.append("Inclui número (0-9). [+1 ponto]")
    else:
        feedback.append("Falta número (0-9).")

    #Caracteres especiais, aqui se cria uma variavel para os caracteres especiais;
    caracteres_especiais = r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/\\|]"
    #Aqui cria-se uma sequência para colocar a condição de ter obrigatóriamente 2 caracteres especiais na senha (no mínimo), que estejam presentes na variável que defini anteriormente;
    #Diferentemente do re.search, que busca dizer se há a presença de algo, o re.findall busca a presença de TODOS que estão presentes na senha;

    aparicoes_especiais = re.findall(caracteres_especiais, senha)
    numero_aparicao = len(aparicoes_especiais)
    minimo_aparicoes = 2
    if numero_aparicao >=minimo_aparicoes:
        pontuacao += 1
        feedback.append("Muito bem! Inclui mais de 1 caractere especial. [+ 1 ponto]")
    elif numero_aparicao == 1:
        feedback.append("Falta mais 1 caractere especial, você está quase lá! Altere sua senha!")
    else:
        feedback.append("Falta caractere especial (ex: !@#$%...).")

    #Após a somatória da pontuação, aqui se registra a pontuação total
    #Também se registra a mensagem referente a cada classificação de pontuação/força da senha;
    
    forca = ""
    if pontuacao == 6:
        forca = 'Forte'
        mensagem = "É isso ai! Sua senha atingiu a pontuação máxima e é considerada Forte!"
    elif pontuacao >= 4:
        forca = 'Média'
        mensagem = "Sua senha é considerada Média. Ela atende aos requisitos básicos, buque a melhorar (ex: use 12+ caracteres)."
    elif pontuacao < 0:
        forca = '???'
        mensagem = "Como... você fez isso? Transcendeu a matéria!"
    elif pontuacao == 0:
        forca = '???'
        mensagem = "Haha, engraçadinho! Tentando quebrar as regras..."
    elif pontuacao <= 3:
        forca = 'Fraca'
        mensagem = "ATENÇÃO: Sua senha é Fraca. Ela falha nos critérios de segurança essenciais, busque urgentemente altera-lá"
    
   #Depois do registro da pontuação, aqui mostra na tela a pontuação;
    feedback.insert(0, f"| Pontuação Total: {pontuacao}/6 | Classificação: {forca} |")
    feedback.insert(1, "=" * 47)
    feedback.insert(2, mensagem)
    feedback.insert(3, "=" * 100)
    
    return (forca, feedback)

#Aqui se registra o valor que o usuário vai entrar e também o resultado que a senha dele vai ter.

senha_de_entrada = input("Digite a senha que você deseja verificar: ")

resultado, feedback = verificar_forca_senha(senha_de_entrada)

print("\n" + "-" * 100)
print(f"Análise da força da senha: {resultado}")
print("-" * 100)

for linha in feedback:
    print(linha)
print("-" * 100)
