possible_games_id = []

with open('input.txt', 'r') as file:
    for line in file:


        line = line.strip().split()


        game_cubes_dict = {"game_id" : int(line[1][:len(line[1])-1])}

        line.pop(0)
        line.pop(0)

        line = [value.replace(",", "") for value in line]    
        
        reveals_list = []

        temp_list = []
        for value in line:
            if ";" in value:
                temp_list.append(value[:len(value)-1])
                reveals_list.append(temp_list)
                temp_list = []
            else:
                temp_list.append(value)

        reveals_list.append(temp_list)
        
        for index, reveal in enumerate(reveals_list, 1):
            reveal.reverse()

            temp_dict = {}
            for i in range(len(reveal)//2):
                temp_dict[reveal[i*2]] = reveal[(i*2)+1]
            
            game_cubes_dict[index] = temp_dict

        not_possible = False
        for key, value in game_cubes_dict.items():
            if key == "game_id":
                continue
            
            
            for inner_key, inner_value in value.items():
                if inner_key == "red" and int(inner_value) > 12:
                    not_possible = True

                elif inner_key == "green" and int(inner_value) > 13:
                    not_possible = True

                elif inner_key == "blue" and int(inner_value) > 14:
                    not_possible = True

        if not not_possible:
            possible_games_id.append(game_cubes_dict["game_id"])

    print(sum(possible_games_id))