import re


def get_phone_numbers(text):
    template_map = {
        't1': r'\(\+\d{1,3}\s\d{2,3}(-\d{2})?\)',
        't2': r'\+\d{1,3}\s\d{2,3}(-\d{2})?',
        't3': r'\+\d{1,3}\s\(\d{2,3}(-\d{2})?\)',
        't4': r'\d{2,3}(-\d{2})+'
    }

    template = r'((({t1}|{t2}|{t3})\s)?{t4})'.format_map(template_map)

    return (match.group(1) for match in re.finditer(template, text))


if __name__ == '__main__':
    with open('test.html') as test:
        for line in test:
            for phone_number in get_phone_numbers(line):
                print(phone_number)
