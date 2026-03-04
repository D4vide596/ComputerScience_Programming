from operator import index


def highest_weekly_usage(social_data):
    highest_hour = -1
    social = None
    week = None
    for key in dict.keys(social_data):
        for idx, hour in enumerate(social_data[key]):
            if hour > highest_hour:
                highest_hour = hour
                social = key
                week = idx + 1

    result = {"name": social, "week": week, "hours": highest_hour}
    return result


def is_social_present(social, social_data):
    if social in dict.keys(social_data):
        return True
    else:
        return False

def enough_data(social, social_data):
    if len(social_data[social]) > 0:
        return  True
    else:
        return False

def correct_imput()


if __name__ == '__main__':

    social_media_data = {
        "instagram": [42.5, 38.2, 45.1],
        "facebook": [28.4, 32.1],
        "x": [15.7, 18.2, 20.5],
        "tiktok": []
    }

    highest_usage = highest_weekly_usage(social_media_data)

    print(highest_usage)

    social_media_choose = input("Insert a social network name: ")

    if is_social_present(social_media_choose, social_media_data):
        weeks_considered = "How many weeks you want to consider?"

        if enough_data(social_media_choose, social_media_data):

            if 
        else:
            print(f"Not enough usage data to compute calculation for {social_media_choose}")

    else:
        print(f"The social {social_media_choose} was not found")


