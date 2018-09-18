cifra = 3
alfabeto = "abcdefghijklmnopqrstuvwxyz"
letras = 26

new_texto = []
new_texto2 = []
texto = ""
resultado = ""

menu = True

while menu == True:
        opcao = input("\nDigite 1 para Cifrar\nDigite 2 para Decifrar\nDigite 3 para mudar a Cifra\nDigite 0 para Sair\n")

        # ============================= Cifrar =============================

        if opcao == '1':
            new_texto = []
            texto = input("Digite o texto a ser cifrado: ")

            for i in range(len(texto)):
                cifrar = ord(texto[i]) + cifra
                if cifrar > 122:
                    cifrar = cifrar - letras
                cifrar = chr(cifrar)

                new_texto.append(cifrar)

            resultado = ''.join(new_texto)
            print("\nTexto cifrado: ", resultado)

        # ============================= Decifrar =============================

        elif opcao == '2':
            new_texto = []
            texto = input("Digite o texto a ser decifrado: ")
            for k in range(len(alfabeto)):
                new_texto = []
                for i in range(len(texto)):
                    decifrar = ord(texto[i]) + k
                    if decifrar > 122:
                        decifrar = decifrar - letras
                    decifrar = chr(decifrar)

                    new_texto.append(decifrar)
                    new_texto2.insert(k, new_texto)

                new_texto2[k] = ''.join(new_texto)
                print("Texto decifrado ",k+1,": ", new_texto2[k])

        elif opcao == '3':
            print("Valor atual da cifra: ", cifra)
            cifra = int(input("Digite o novo valor para a cifra:"))
            print("Valor da cifra alterado para: ", cifra)

        # ================================ END =================================

        elif opcao == '0':
            menu = False

