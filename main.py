import random


def get_cart():
    cart = random.choice(list(carts.keys()))
    while carts[cart] == 0:
        cart = random.choice(list(carts.keys()))
    carts[cart] -= 1
    return cart


def determining_score(carts: list) -> int:
    s = 0
    flag = False
    for cart in carts:
        if cart == 'A':
            flag = True
            s += 11
        else:
            s += int(cart)
    if s > 21 and flag:
        s -= 10
    return s


def dealer_check(carts: list):
    while determining_score(carts) <= 16:
        print('The dealer decided to take a card...')
        carts.append(get_cart())


def stand(d_carts: list, p_carts: list, game_bank: float, u_money: float) -> tuple:
    if determining_score(d_carts) < determining_score(p_carts):
        u_money += game_bank
        game_bank = 0
        print(f'you win , your money: {u_money} \n'
              f'your cart: {p_carts} \n'
              f'dealer cart: {d_carts}')
        if input('if you want leave game enter exit/continue \n').lower() == 'exit':
            return False, game_bank, u_money
        return True, game_bank, u_money
    else:
        game_bank = 0
        print(f'you lost, your money: {u_money} \n'
              f'your cart: {p_carts} \n'
              f'dealer cart: {d_carts}')
        if input('if you want leave game enter exit/continue \n').lower() == 'exit':
            return False, game_bank, u_money
        return True, game_bank, u_money


def hit(d_carts: list, p_carts: list, game_bank: float, u_money: float) -> tuple:
    player_carts.append(get_cart())
    if determining_score(p_carts) > 21:
        game_bank = 0
        print(f'you lost, your money: {u_money} \n'
              f'your cart: {p_carts} \n'
              f'dealer cart: {d_carts}')
        if input('if you want leave game enter exit/continue \n').lower() == 'exit':
            return True, False, game_bank, u_money
        return True, True, game_bank, u_money
    else:
        dealer_check(d_carts)
        if determining_score(d_carts) > 21:
            u_money += game_bank
            game_bank = 0
            print(f'you win , your money: {u_money} \n'
                  f'your cart: {p_carts} \n'
                  f'dealer cart: {d_carts}')
            if input('if you want leave game enter exit/continue \n').lower() == 'exit':
                return True, False, game_bank, u_money
            return True, True, game_bank, u_money
        else:
            return False, True, game_bank, u_money


user_money = 10000
stay = True
while stay and user_money >= 1000:
    carts = {'A': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, '10': 12}
    print("A thousand dollars were deducted from the user and"
          " a thousand dollars were added to the casino's game.")
    user_money -= 1000
    bank = 2000
    dealer_carts = [get_cart(), get_cart()]
    player_carts = [get_cart(), get_cart()]
    while True:
        print(f'Second dealer cart : {dealer_carts[1]} \n'
              f'Your carts {[x for x in player_carts]} \n'
              f'You can choose from the following options: \n'
              f'1 - Stand \n'
              f'2 - hit \n')
        user_answer = input('your choice: ')
        if user_answer == '1':
            dealer_check(dealer_carts)
            stay, bank, user_money = stand(dealer_carts, player_carts, bank, user_money)
            break

        if user_answer == '2':
            end, stay, bank, user_money = hit(dealer_carts, player_carts, bank, user_money)
            if end:
                break
            continue
