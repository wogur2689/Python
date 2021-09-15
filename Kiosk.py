menu = ('주문종료', '홍차', '녹차', '커피', '보리차', '레몬에이드', '복숭아 아이스티', '우유')
price = (0, 4000, 2000, 3500, 2500, 3000, 1500, 1000)

# 주문에 필요한 메시지 만들기
msg = '어서오세요. 코딩카페입니다. 주문하시겠어요? 메뉴는 하나씩 이야기 해주세요~'
for i in range(len(menu)):
    msg += '\n\t %d %s' % (i, menu[i])
    if i != 0:
        msg += ' %6d 원' % (price[i])
msg += '\n >> '

more = True
total = 0
money = 0

while more:
    instr = input(msg)
    order = int(instr)
    if order == 0:
        print()
        print(' 주문종료 '.center(20, '*'))
        more = False
    elif 1 <= order <= 7:
        cnt = int(input('몇잔을 드시겠어요?'))
        print('%s, %d개 주문' % (menu[order], cnt))
        sub = price[order] * cnt
        total += sub
        print('%s 주문가격 %d, 총 가격 %d' % (menu[order], sub, total))
    else:
        print('모르겠어요. 다시 주문하세요!')
    cnt = 0

else:
    more = True
    print('주문을 마치겠습니다.')
    sel = int(input('매장에서 드시려면 1번, 아니면 포장하시려면 2번을 입력하세요~'))
    if sel == 1:
        mejang = '매장에서 식사를 선택하셨습니다.'
        print(mejang)
    else:
        pojang = '포장을 선택하셨습니다.'
        print(pojang)

while more:
    print('총 주문가격 %d 원' % total)
    print('내신 금액: %d 원' % money)
    money = int(input('지불하셔야 하는 금액을 입력하세요.'))
    if total > money:
        print('금액이 부족합니다. 처음부터 다시 지불해 주세요')
        continue
    elif money > total:
        print('내신 금액: %d 원' % money)
        print('거스름돈: %d 원' % (money - total))
        break
    else:
        print('총 주문 가격과 금액이 맞습니다.')
        break

print('이용해 주셔서 감사합니다!'.center(30, '='))