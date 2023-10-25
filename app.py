def get_hour():
    while True:
        try:
            hour = input("Enter time in HH:MM format: ")
            hourHand, minuteHand = map(int, hour.split(":"))
            if 0 <= hourHand <= 23 and 0 <= minuteHand <= 59:
                return hourHand, minuteHand
            else:
                print("Please enter a valid time.")
        except ValueError:
            print("Invalid input. Please use HH:MM format.")


def calculate_angle(hourHand, minuteHand):
    hourHand = hourHand % 12
    hourHandAngle = (hourHand * 30) + (minuteHand * 0.5)
    minuteHandAngle = minuteHand * 6
    angle = abs(hourHandAngle - minuteHandAngle)

    if angle > 180:
        angle = abs(360 - angle)

    return angle


hourHand, minuteHand = get_hour()
betweenAngle = calculate_angle(hourHand, minuteHand)
print("Between angle:", betweenAngle)
