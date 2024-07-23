import time


def traffic_signal():
    while True:
        # Red light
        print("Red light - Stop")
        time.sleep(5)  # 5 seconds for red light

        # Green light
        print("Green light - Go")
        time.sleep(7)  # 5 seconds for green light

        # # Yellow light
        # print("Yellow light - Prepare to stop")
        # time.sleep(2)  # 2 seconds for yellow light

        # # Green light left
        # print("Green light - Left")
        # time.sleep(5)  # 5 seconds for green light left

        # Yellow light
        print("Yellow light - Prepare to stop")
        time.sleep(2)  # 2 seconds for yellow light


# Run the traffic signal simulation
traffic_signal()
