from string import ascii_lowercase, digits
from typing import Dict, List
from random import choices
import asyncio
import json
import re

from aiohttp import ClientSession, DummyCookieJar
from colorama import Fore


def randstr(__length: int, /) -> str:
    return "".join(choices(ascii_lowercase + digits, k=__length))


def load_tokens() -> List[str]:
    with open("./tokens.txt") as file:
        tokens = [line for line in file.readlines() if line]

    if not tokens:
        tokens = input("Enter tokens (comma seperated): ").split(",")

    return [token.strip() for token in tokens]


async def joiner(session: ClientSession, /, token: str, invite: str) -> None:
    headers = dict(session.headers)
    headers["authorization"] = token

    url = f"https://discord.com/api/v9/invites/{invite}"

    cookies = {
        "__cfuid"  : randstr(43),
        "__dcfduid": randstr(32),
        "locale"   : "en-US"
    }

    async with session.post(url, headers=headers, cookies=cookies) as response:
        if 200 <= response.status <= 204:
            return print(f"{Fore.GREEN}[+]{Fore.RESET} Joined")

        print(f"{Fore.RED}[-]{Fore.RESET} Failed")


async def main() -> None:
    with open("./data/logo.txt") as file:
        logo = file.read()

    print(f"{Fore.LIGHTMAGENTA_EX}{logo}{Fore.RESET}")

    tokens = load_tokens()
    invite = input("Enter your invite link: ")

    if invite.startswith(("http", "discord.gg")):
        invite = re.match(r".*?/(\w+$)", invite).group(1)

    with open("./data/headers.json") as file:
        headers: Dict[str, str] = json.load(file)

    async with ClientSession(cookie_jar=DummyCookieJar(), headers=headers) as session:
        await asyncio.gather(*[
            joiner(session, token, invite) for token in tokens
        ])


if __name__ == "__main__":
    asyncio.run(main())
