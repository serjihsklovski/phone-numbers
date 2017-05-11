import re


def get_phone_numbers(text):
    template = r'((\+7|8)[-\s]?((\(\d{3}\))|\d{3})[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2})'
    return (match.group(1) for match in re.finditer(template, text))


if __name__ == '__main__':
    with open('test.html') as test:
        for line in test:
            for phone_number in get_phone_numbers(line):
                print(phone_number)
