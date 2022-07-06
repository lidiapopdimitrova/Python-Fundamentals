team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards_input = input().split()
is_terminated = False
for card in cards_input:
    card_info = card.split("-")

    team_name = card_info[0]
    player_num = int(card_info[1])
    if team_name == 'A' and player_num in team_a:
        team_a.remove(player_num)

    elif team_name == 'B' and player_num in team_b:
        team_b.remove(player_num)
    if len(team_a) < 7:
        is_terminated = True
        break

    if len(team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_terminated:
    print("Game was terminated")