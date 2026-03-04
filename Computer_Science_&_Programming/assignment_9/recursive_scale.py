def recursive_function(list_of_balls):
    if len(list_of_balls) == 1:
        return list_of_balls[0]

    group_balls_1 = sum(ball[1] for ball in list_of_balls[:(len(list_of_balls)//3)])
    group_balls_2 = sum(ball[1] for ball in list_of_balls[(len(list_of_balls)//3):(2*len(list_of_balls)//3)])
    group_balls_3 = sum(ball[1] for ball in list_of_balls[(2*len(list_of_balls)//3):])

    if group_balls_1 < group_balls_2:
        return recursive_function(list_of_balls[(len(list_of_balls)//3):(2*len(list_of_balls)//3)])
    elif group_balls_1 > group_balls_2:
        return recursive_function(list_of_balls[:(len(list_of_balls)//3)])
    else:
        return recursive_function(list_of_balls[(2*len(list_of_balls)//3):])


if __name__ == '__main__':
    list_of_balls = [[0,1], [1,1], [2,1], [3,1], [4,1], [5,1], [6,1], [7,2], [8,1]]

    heavier_ball = recursive_function(list_of_balls)

    print(heavier_ball[0])