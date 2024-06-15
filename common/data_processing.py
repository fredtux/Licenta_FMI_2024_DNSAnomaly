import re

def not_exfil(d):
    return not re.fullmatch(r'^[0-9]+\.[A-z\-\_0-9]+\.cicresearch\.ca\.*|init\.[A-z\-\_0-9]+\.base64\.cicresearc\.*|init\.[A-z\-\_0-9]+\.base64\.cicrese\.|init\.[A-z\-\_0-9]+\.base64\.cicre\.|init\.[A-z\-\_0-9]+\.base64\.+|init\.[A-z\-\_0-9]+\.|^\d+\.[A-z0-9\-\_]+\.b|init\.[A-z\-\_0-9]+\.b\.*|^\d+\.[A-z0-9\-\_]+\.', d)


def get_domain_name(text, slds):
    text = text.split('.')
    if len(text) > 2 and text[-2] in slds:
        return text[-3].lower()
    else:
        return text[-2].lower()
    
def same_domain(d1, set_domains):
    d1 = get_domain_name(d1)
    return d1 in set_domains