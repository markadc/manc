import random


def make_ua():
    a = random.randint(55, 62)
    c = random.randint(0, 3200)
    d = random.randint(0, 150)
    os_type = [
        "(Windows NT 6.1; WOW64)", "(Windows NT 10.0; WOW64)",
        "(X11; Linux x86_64)",
        "(Macintosh; Intel Mac OS X 10_12_6)"
    ]
    chrome_version = f"Chrome/{a}.0.{c}.{d}"
    os_choice = random.choice(os_type)
    ua = f"Mozilla/5.0 {os_choice} AppleWebKit/537.36 (KHTML, like Gecko) {chrome_version} Safari/537.36"
    return ua


def make_headers():
    headers = {"User-Agent": make_ua()}
    return headers
