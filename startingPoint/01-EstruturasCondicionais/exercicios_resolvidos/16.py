"""
16 - Faça um programa que verifique a validade de uma senha fornecida pelo usuário. A senha é 4531. O programa deve mostrar uma mensagem de 
permissão de acesso ou não.
"""
password = int(input("Digite a senha de acesso: "))

print("Acesso permitido. Seja bem-vindo!" if password == 4531 else "Acesso negado. Por favor, verifique a senha e tente novamente.")
