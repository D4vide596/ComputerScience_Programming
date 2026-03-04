def convert_to_fahrenheit(list_c):
    list_f = []
    for c in list_c:
        f = round((c * 9/5) + 32, 1)
        list_f.append(f)
    return list_f


def calculate_average(list_c):
    sum_temp = 0
    for t in list_c:
        sum_temp += t
    return round(sum_temp/len(list_c), 2)

def count_hot_days(list_c, threshold):
    count = 0
    for t in list_c:
        if t > threshold:
            count+=1
    return count

if __name__ == "__main__":
    temps = [20, 22, 19, 25, 30, 18]

    # 1. Function to convert all to Fahrenheit
    temps_f = convert_to_fahrenheit(temps)
    print(f"Fahrenheit: {temps_f}")

    # 2. Function to find average
    avg = calculate_average(temps)
    print(f"Average Celsius: {avg}")

    # 3. Function to count how many days were hot (> 21 degrees)
    hot_days = count_hot_days(temps, threshold=21)
    print(f"Hot days: {hot_days}")