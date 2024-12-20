import string
import random
def generate_promo(length = 8):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    all_proms = []
    for i in range(10):
        generator = random.choices(characters, k = 8)
        promo = ''.join(generator)
        all_proms.append(promo)
        yield promo
start = generate_promo()
while True:
    try:
        print(next(start))
        input('Нажмите ENTER')
    except Exception as e:
        print('Промокоды кончились')
        break