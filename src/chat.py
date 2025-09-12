from search import search_prompt
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "🤖 Bem-vindo ao ChatBot Inteligente! (digite 'sair' para encerrar)\n")
    while True:
        user_input = input(Fore.GREEN + "👤 Você: " + Style.RESET_ALL)
        if user_input.lower() in ("exit", "sair", "quit"):
            print(Fore.YELLOW + "👋 Encerrando o chat. Até logo!")
            break
        response = search_prompt(user_input)
        print(Fore.MAGENTA + "🤖 Chatbot:" + Style.RESET_ALL, response)
        print("-" * 50)

if __name__ == "__main__":
    main()
