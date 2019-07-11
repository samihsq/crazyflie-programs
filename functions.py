import time

f = "f"
b = "b"
r = "r"
l = "l"

value = 0
yratio = 0
xratio = 0


def liftoff(cf, stall_time):
    for y in range(15):
        cf.commander.send_hover_setpoint(0, 0, 0, y / 30)
        time.sleep(0.07)

    for y in range(1):
        cf.commander.send_hover_setpoint(0, 0, 0, 0.5)
        time.sleep(stall_time)


def landing(cf, stall_time):
    for y in range(1):
        cf.commander.send_hover_setpoint(0, 0, 0, 0.5)
        time.sleep(stall_time)

    # landing
    for y in range(19):
        cf.commander.send_hover_setpoint(0, 0, 0, (20 - y) / 40)
        time.sleep(0.1)
    time.sleep(0.5)

    cf.commander.send_stop_setpoint()


def flyrlfb(cf, distance, sec, height, direction):
    ratio = distance / sec
    print(direction)
    if direction == "r" or direction == "b":
        ratio = -ratio
    else:
        ratio = ratio

    '''if d <= 90:
        xratio = d/90
        yratio = -((90-d)/90)'''

    if direction == "r" or direction == "l":
        for _ in range(1):
            cf.commander.send_hover_setpoint(0, 0.43 * ratio, 0, height)
            time.sleep(sec)
    elif direction == "f" or direction == "b":
        for _ in range(1):
            cf.commander.send_hover_setpoint(0.43 * ratio, 0, 0, height)
            time.sleep(sec)
    for y in range(1):
        cf.commander.send_hover_setpoint(0, 0, 0, 0.4)
        time.sleep(0.5)


def fly(cf, distance, sec, height, direction):
    ratio = distance / sec
    print(direction)

    '''if d <= 90:
        xratio = d/90
        yratio = -((90-d)/90)'''

    for _ in range(1):
        cf.commander.send_hover_setpoint(0, 0, direction, height)
        print("turning")
        time.sleep(1)
    for _ in range(1):
        cf.commander.send_hover_setpoint(0.43 * ratio, 0, 0, height)
        print('2')
        time.sleep(sec)
    for y in range(1):
        cf.commander.send_hover_setpoint(0, 0, 0, height)
        print("3")
        time.sleep(0.5)