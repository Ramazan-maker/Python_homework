import re
import sys
exchange_rates = {
    'USD': 477.50, "$": 477.50,
    'EUR': 502.75, "€": 502.75
}

def convert_currency(match):
    amount = float(match.group(1))
    currency = match.group(2).upper()  # Преобразовать валюту в верхний регистр
    if currency in exchange_rates:
        converted_amount = amount * exchange_rates[currency]
        return f"{converted_amount:.2f} ₸"
    return match.group(0)


def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    pattern = r'(\d+\.\d+)\s*(USD|EUR|\$|€)'

    converted_text = re.sub(pattern, convert_currency, text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование python converter.py input.txt output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)