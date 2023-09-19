import HigherLower_gameData
import random


# for x in range(len(HigherLower_gameData.data)):
#     print(f"{HigherLower_gameData.data[x]['name']} with {HigherLower_gameData.data[x]['follower_count']} followers "
#           f"- {HigherLower_gameData.data[x]['description']} from {HigherLower_gameData.data[x]['country']}")
#     print("---------------------------------------------------------------------------------------------")

# print(len(HigherLower_gameData.data))

while len(HigherLower_gameData.data) > 45:
    first_player = random.choice(HigherLower_gameData.data)
    second_player = random.choice(HigherLower_gameData.data)

    print(f"{first_player['name']} - {first_player['description']}from {first_player['country']}")
    print(f"{second_player['name']} - {second_player['description']}from {second_player['country']}")
    print("----------------------")

    choice = int(input("Who has more followers 1 or 2?\n"))

    if choice == 1:
        if first_player['follower_count'] > second_player['follower_count']:
            print("Correct")
            # print(f"{first_player['name']} - {first_player['description']}from {first_player['country']}"
            #       f" has {first_player['follower_count']} followers")
            HigherLower_gameData.data.remove(second_player)
            second_player = random.choice(HigherLower_gameData.data)
        else:
            print(f"Wrong\n{second_player['name']} has {second_player['follower_count']} followers "
                  f"but {first_player['name']} "
                  f"only {first_player['follower_count']}")
            break
    if choice == 2:
        if first_player['follower_count'] < second_player['follower_count']:
            print("Correct")
            # print(f"{second_player['name']} - {second_player['description']}from {second_player['country']}"
            #       f" has {second_player['follower_count']} followers")
            HigherLower_gameData.data.remove(first_player)
            first_player = random.choice(HigherLower_gameData.data)
        else:
            print(
                f"Wrong\n{first_player['name']} has {first_player['follower_count']} followers "
                f"but {second_player['name']} "
                f"only {second_player['follower_count']}")
            break
    # print(len(HigherLower_gameData.data))

# for element in HigherLower_gameData.data:
#     print(element)
#     print(len(HigherLower_gameData.data))
