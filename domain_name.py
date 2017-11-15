from tld import get_tld


# Getting the top level domain of the target


def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name


print('2___getting domain_name . . .')
print('domain_name of  https://www.thenewboston.com/ = ' + get_domain_name('https://www.thenewboston.com/'))
