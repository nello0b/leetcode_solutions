import random
from typing import List, Dict

PROG_LANG : List[str] = ["Python3", "Java", "JavaScript", "C", "C++"]

# Returns a random programming language from the list
def get_random_prog_lang():
    return random.choice(PROG_LANG)

# Returns a dictionary with counts of programming languages sampled
def sample_prog_lang(n: int) -> Dict[str, int]:
    langs: Dict[str, int] = {}
    empty = 6
    i = 0
    while i < n and empty > 0:
        lang = get_random_prog_lang()
        if lang in langs:
            langs[lang] += 1
        else:
            langs[lang] = 1
            empty -= 1
        i += 1
    for j in range(i, n):
        lang = get_random_prog_lang()
        langs[lang] += 1
    return langs

def print_sampled_languages(n: int):
    langs = sample_prog_lang(n)
    print(f"Sampled {n} programming languages:")
    for lang, count in langs.items():
        print(f"{lang}: {count}")


print("Random Language to do the exercise in:", f"\033[92m{get_random_prog_lang()}\033[0m")