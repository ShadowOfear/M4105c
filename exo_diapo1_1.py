def print_sentences():
    numbers = generate_numbers(3)

    for n in numbers:
        print(build_sentence(n))

def generate_numbers(n):
    m = []
    for x in range(1, n+1):
        m.append(x)
    return m
    
def build_sentence(n):
    n = str(n)
    for x in n:
        return ("Ceci est la phrase n°" + x)

# Ceci est la phrase n°1
# Ceci est la phrase n°2
# Ceci est la phrase n°3


def parse_tlds():
    urls = [
        "www.monsite.fr",
        "www.ooojah.com",
        "www.blablatop.org",
        "www.jeujeubla.ca"
    ]
    l = []
    for x in urls :
        l.append(x[-2].upper()+x[-1].upper())
    print(l)
    