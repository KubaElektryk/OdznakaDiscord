import requests

from discord import app_commands, Intents, Client, Interaction

print("\n".join([
    "Hej witaj w aktywatorze DC developer badge.",
    "Podaj swoj Bot Token aby kontunowac.",
    "",
    "Nie zamykaj aplikacji po podaniu Tokena. "
    "Jeśli zamkniesz twój bot nie wykona polecenia."
]))


while True:
    token = input("> ")

    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"
    })

    data = r.json()
    if data.get("id", None):
        break  
    print("\nNiepoprawny Token bota.")


class odznaka(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


client = odznaka(intents=Intents.none())


@client.event
async def on_ready():
    """ Nazywa się to, gdy bot jest gotowy i ma połączenie z Discordem
        Drukuje również adres URL zaproszenia bota, który automatycznie używa twojego
        Identyfikator klienta, aby upewnić się, że zapraszasz właściwego bota z odpowiednimi zakresami.
    """
    print("\n".join([
        f"Zalogowano {client.user} (ID: {client.user.id})",
        "",
        f"uzyj tego linku zeby dolaczyc {client.user} do twojego serwera:",
        f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot"
    ]))


async def _init_command_response(komenda: Interaction) -> None:
    """ Jest to wywoływane, gdy polecenie jest uruchamiane
        Powód, dla którego polecenie znajduje się poza funkcją polecenia
        jest tak, ponieważ istnieją dwa sposoby uruchamiania poleceń i poleceń ukośnika
        nie wspieraj natywnie aliasów, więc musimy to sfałszować.
    """

    print(f"> {komenda.user} użył komendy.")

    await komenda.response.send_message("\n".join([
        f"Hi **{komenda.user}**, Dzieki za napisanie do mnie.",
        "",
        "__**Gdzie twoja odznaka?**__",
        "Kwalifikacja do odznaki jest sprawdzana przez Discord w określonych odstępach czasu, "
        "w tej chwili zalecany czas oczekiwania przed próbą to 24 godziny.",
        "",
        "__**Minęły 24 godziny, jak teraz zdobyć odznakę?**__",
        "Jeśli minęły już 24 godziny, możesz udać się do "
        "https://discord.com/developers/active-developer i wypełnij znajdujący się tam 'formularz'.",
        "",
        "__**Active Developer Badge Aktualności**__",
        "Aktualizacje dotyczące odznaki Aktywnego programisty można znaleźć w "
        "Discord Developers server -> discord.gg/discord-developers - w #active-dev-badge .",
    ]))


@client.tree.command()
async def siema(komenda: Interaction):
    """ Powiedz cokolwiek """
    await _init_command_response(komenda)


@client.tree.command()
async def dajodznake(komenda: Interaction):
    """ Powiedz cokolwiek """
    await _init_command_response(komenda)

@client.tree.command()
async def pomoc(komenda: Interaction):
    """ Powiedz cokolwiek """
    await _init_command_response(komenda)


client.run(token)
