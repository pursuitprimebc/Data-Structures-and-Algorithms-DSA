table_card = input()
in_hand_card = input().split()

for card in in_hand_card:
    if card[0] == table_card[0] or card[1] == table_card[1]:
        print("YES")
        break  
else:
    print("NO")