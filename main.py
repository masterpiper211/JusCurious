import asyncio
import aiohttp
from bs4 import BeautifulSoup
from colorama import init, Fore, Style, Back
import pyfiglet
import time
import os
import sys

init(autoreset=True)  # Initialize colorama

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_animated_banner(text, version, duration=3, fps=10):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    banner = pyfiglet.figlet_format(text, font="slant")
    version_text = f"version {version}"

    lines = banner.split("\n")
    max_length = max(len(line) for line in lines)

    # Add version text below the banner
    lines.append("")  # Empty line for spacing
    lines.append(version_text.center(max_length))

    total_frames = duration * fps
    for frame in range(total_frames):
        clear_screen()
        colored_banner = ""
        for i, line in enumerate(lines):
            if i == len(lines) - 1:  # Version line
                color = Fore.WHITE + Back.BLACK
                animated_line = color + line[:frame % len(line)] + Style.RESET_ALL
            else:
                color = colors[(i + frame) % len(colors)]
                padding = " " * (max_length - len(line))
                animated_line = color + line[:frame % max_length] + Style.RESET_ALL + padding
            colored_banner += animated_line + "\n"

        sys.stdout.write(colored_banner)
        sys.stdout.flush()
        time.sleep(1/fps)

    # Final frame with full text
    clear_screen()
    colored_banner = ""
    for i, line in enumerate(lines):
        if i == len(lines) - 1:  # Version line
            color = Fore.WHITE + Back.BLACK
        else:
            color = colors[i % len(colors)]
        colored_banner += color + line + Style.RESET_ALL + "\n"
    sys.stdout.write(colored_banner)
    sys.stdout.flush()

# Social media websites list
social_media_websites = [
    "https://www.facebook.com/{}",
    "https://www.twitter.com/{}",
    "https://www.instagram.com/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.github.com/{}",
    "https://www.pinterest.com/{}",
    "https://www.reddit.com/user/{}",
    "https://www.youtube.com/user/{}",
    "https://www.twitch.tv/{}",
    "https://www.tiktok.com/@{}",
    "https://www.snapchat.com/add/{}",
    "https://www.quora.com/profile/{}",
    "https://www.soundcloud.com/{}",
    "https://www.spotify.com/user/{}",
    "https://www.medium.com/@{}",
    "https://www.behance.net/{}",
    "https://www.dribbble.com/{}",
    "https://www.deviantart.com/{}",
    "https://www.producthunt.com/@{}",
    "https://www.flickr.com/people/{}",
    "https://www.500px.com/{}",
    "https://www.vimeo.com/{}",
    "https://www.slideshare.net/{}",
    "https://www.scribd.com/{}",
    "https://www.codepen.io/{}",
    "https://www.stackoverflow.com/users/{}",
    "https://www.hackernews.com/user?id={}",
    "https://www.kaggle.com/{}",
    "https://www.goodreads.com/user/show/{}",
    "https://www.last.fm/user/{}",
    "https://www.bandcamp.com/{}",
    "https://www.soundclick.com/{}",
    "https://www.mixcloud.com/{}",
    "https://www.reverbnation.com/{}",
    "https://www.xing.com/profile/{}",
    "https://www.weibo.com/{}",
    "https://www.douban.com/people/{}",
    "https://www.zhihu.com/people/{}",
    "https://www.vk.com/{}",
    "https://www.ok.ru/profile/{}",
    "https://www.livejournal.com/profile?userid={}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.blogger.com/profile/{}",
    "https://www.wordpress.com/author/{}",
    "https://www.patreon.com/{}",
    "https://www.etsy.com/people/{}",
    "https://www.ebay.com/usr/{}",
    "https://www.amazon.com/gp/profile/{}",
    "https://www.xvideos.com/profiles/{}",
    "https://www.pornhub.com/model/{}",
    "https://www.xhamster.com/users/{}",
    "https://www.redtube.com/user/{}",
    "https://www.deviantart.com/{}",
    "https://www.newgrounds.com/{}",
    "https://www.furaffinity.net/user/{}",
    "https://www.gumroad.com/{}",
    "https://www.onlyfans.com/{}",
    "https://www.artstation.com/{}"
]

async def check_username(session, url, username):
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                text = await response.text()
                if username.lower() in text.lower():
                    return f"{Fore.GREEN}[+] Username found on {url}"
            return f"{Fore.RED}[-] Username not found on {url}"
    except asyncio.TimeoutError:
        return f"{Fore.YELLOW}[!] Timeout occurred for {url}"
    except Exception as e:
        return f"{Fore.YELLOW}[!] Error occurred for {url}: {str(e)}"

async def search_username(username):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for website in social_media_websites:
            url = website.format(username)
            tasks.append(asyncio.ensure_future(check_username(session, url, username)))

        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

if __name__ == "__main__":
    create_animated_banner("JusCurious", "1.0.0")
    username = input("Enter the username you want to search for: ")

    start_time = time.time()
    asyncio.run(search_username(username))
    end_time = time.time()
    print(f"\nSearch completed in {end_time - start_time:.2f} seconds")
