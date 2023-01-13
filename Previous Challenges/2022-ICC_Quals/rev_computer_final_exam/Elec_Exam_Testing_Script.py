import numpy as np
import random as rand
import sys

pick_a_card = rand.randint(0,9)
voltage = rand.randint(25, 100)
current = rand.randint(25, 100)
R1 = rand.randint(100, 200)
R2 = rand.randint(200, 250)
R3 = rand.randint(300, 400)
R4 = rand.randint(400, 500)
R5 = rand.randint(500, 550)
R6 = rand.randint(550, 600)
R7 = rand.randint(600, 750)
R8 = rand.randint(750, 800)
R9 = rand.randint(800, 900)
R10 = rand.randint(900, 950)
f = rand.randint(1000, 20000)
infinity = float("inf")
a = rand.randint(R3, R4)
c = rand.randint(R4, R5)
e = rand.randint(R5, R6)
b = e - a
d = e - c
f = b * d
trace = {
    'Manganin': 290,
    'Constantan': 272.97,
    'Platinum': 64.16,
    'Nickel': 41.69,
    'Zinc': 35.49,
    'Tungsten': 31.76,
    'Aluminum': 15.94,
    'Gold': 13.32,
    'Copper': 10.09,
    'Silver': 9.546
}


def main():
    pick_a_card = rand.randint(0,9)

    match pick_a_card:
        case 0:
            print("Which of Kirchhoff's laws is utilised in Nodal Analysis?")
            quiz = "KCL"
        case 1:
            print("What does FPGA stand for?")
            quiz = "Field Programmable Gate Array"
        case 2:
            print("What does UEFI stand for?")
            quiz = "Universal Extensible Firmware Interface"
        case 3:
            print("What logical law is used in the following example. 'not (A and B) = not A or not B'")
            quiz = "De Morgan's Law"
        case 4:
            print("What CPU architecture is used by the Raspberry Pi Pico?")
            quiz = "ARM"
        case 5:
            print("What is the hexidecimal constant utilised in Quake's Fast Inverse Squareroot Algorithm?")
            quiz = "0x5f3759df"
        case 6:
            print("Frequency is measure in what?")
            quiz = "Hertz"
        case 7:
            print("What acronym is used to describe the act of connecting a toaster to the internet?")
            quiz = "IoT"
        case 8:
            print("What Nintendo DS game allowed hackers to bypass 3DS security?")
            quiz = "Cubic Ninja"
        case 9:
            print("What is the floating point standard?")
            quiz = "IEEE 754"

    quiz_response = quiz

    if quiz_response == quiz:
        print("Correct!")
    else:
        sys.exit("Incorrect!")

    match pick_a_card:
        case 0: 
            VTH = voltage * (((R3 * R6)/(R3 + R6)) / (((R3 * R6)/(R3 + R6)) + R1 + R4))
            RTH = R7 + ((R3 * R6)/(R3 + R6)) + R1 + R4
        case 1:
            VTH = voltage * (((R3 * R6)/(R3 + R6)) / (((R3 * R6)/(R3 + R6)) + R1 + R4))
            RTH = R7 + R8 + ((R3 * R6)/(R3 + R6)) + R1 + R4
        case 2:
            VTH = voltage * (R3 / (R3 + R1 + R4))
            RTH = R7 + R8 + R3 + R1 + R4
        case 3:
            VTH = voltage * (R3 / (R3 + R1 + R4))
            RTH = R7 + R3 + R1 + R4
        case 4:
            VTH = voltage * (R3 / (R3 + R1 + R2 + R4))
            RTH = R7 + R3 + R1 + R2 + R4
        case 5:
            VTH = current * ((R3 * R6)/(R3 + R6))
            RTH = R7 + ((R3 * R6)/(R3 + R6)) + R9
        case 6:
            VTH = current * ((R3 * R6)/(R3 + R6))
            RTH = R7 + ((R3 * R6)/(R3 + R6)) + R9 + R10
        case 7:
            VTH = current * (R3 / (R3 + R1 + R4))
            RTH = R7 + R3 + R9
        case 8:
            VTH = current * (R3 / (R3 + R1 + R4))
            RTH = R7 + R3 + R9 + R10
        case 9:
            VTH = current * (R3 / (R3 + R1 + R4))
            RTH = R7 + R3 + R9 + R10

    IN = VTH/RTH
    ID = 1/(RTH) * voltage - IN
    voltage_real = np.linspace(0, VTH, 50)
    diode = np.linspace(0, 100, 50) ** 2.5
    Vd = np.argwhere(np.diff(np.sign(voltage_real - diode))).flatten()

    operating_point = "0, 0"

    try:
        operating_point = str(int(Vd[1])) + ", " + str(int(voltage_real[Vd[1]]))
    except:
        operating_point = "NULL"

    print("Provide the Vd, Id coordinates for the diode operating point. ")
    print("ID: ", ID)
    print("Vth: " , VTH)
    print("Vd: ", Vd)
    print("Rth: ", RTH)
    print("Current: ", current)

    operating_point_response = input(": ")

    if operating_point_response == str(operating_point):
        print("Correct!")
    else:
        sys.exit("Incorrect!")

    print("Filters, much like this exam, cut off what is unwanted.")

    C = abs(ID*10**-6)
    L = abs(ID*10**-3)

    match pick_a_card:
        case 0:
            print("What is the cut off frequency of the RC low-pass filter?")
            print("C: %s" %C)
            filter_ans = 1 / (2 * np.pi * RTH * C)
        case 1:
            print("What is the cut off frequency of the RC high-pass filter?")
            print("C: %s" %C)
            filter_ans = 1 / (2 * np.pi * RTH * C)
        case 2:
            print("What is the phase shift of the RC low-pass filter?")
            print("C: %s, f: %s" % (C, f))
            filter_ans = -(np.arctan((2 * np.pi * f) * RTH * C))
        case 3:
            print("What is the phase shift of the RC high-pass filter?")
            print("C: %s, f: %s" % (C, f))
            filter_ans = np.arctan((1)/(2 * np.pi * f * RTH * C))
        case 4:
            print("What is the cut off frequency of the RL low-pass filter?")
            print("L: %s" %L)
            filter_ans = RTH / (2 * np.pi * L)
        case 5:
            print("What is the cut off frequency of the RL high-pass filter?")
            print("L: %s" %L)
            filter_ans = RTH / (2 * np.pi * L)
        case 6:
            print("What is the phase shift of the RL low-pass filter?")
            print("L: %s, f: %s" % (L, f))
            filter_ans = np.arctan(((2 * np.pi * f) * (L /RTH)))
        case 7:
            print("What is the phase shift of the RL high-pass filter?")
            print("L: %s, f: %s" % (L, f))
            filter_ans = np.arctan((RTH)/(2 * np.pi * f * L))
        case 8:
            print("What is the cut off frequency of the LC low-pass filter?")
            print("C: %s, L: %s" % (C, L))
            filter_ans = 1 / (2 * np.pi * np.sqrt(L * C))
        case 9:
            print("What is the phase shift of the LC low-pass filter?")
            print("C: %s, L: %s, f: %s" % (C, L, f))
            filter_ans = np.arctan((1)/(2 * np.pi * f * L * C))

    filter_response = input()

    if filter_response == filter_ans:
        print("Correct!")
    else:
        sys.exit("Incorrect!")

    match pick_a_card:
        case 0: circuit = {
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'R2': {'C2': c, 'C3': a}, 
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f}, 
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e}, 'C4': {'Vout': f}, 
                'C5': {'R6': d}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d},
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'Vout': None}
        case 1: circuit = {
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'R2': {'C2': c, 'C3': a},
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e}, 'C4': {'Vout': f},  
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f}, 
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'Vout': None,
                'C5': {'R6': d}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d}}
        case 2: circuit = {
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e},   
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f}, 
                'C5': {'R6': d}, 'Vout': None, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d},
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'C4': {'Vout': f},
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'R2': {'C2': c, 'C3': a}}
        case 3: circuit = {
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'R2': {'C2': c, 'C3': a}, 
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f}, 
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e}, 'C4': {'Vout': f}, 
                'C5': {'R6': d}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d},
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'Vout': None}
        case 4: circuit = {
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'Vout': None,  
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'R2': {'C2': c, 'C3': a},
                'R3': {'C3': b}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d},
                'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f}, 'C5': {'R6': d},
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e}, 'C4': {'Vout': f}, 
                'L3': {'Vout': f}, 'L4': {'Vout': f}}
        case 5: circuit = {
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'Vout': None, 'R1': {'C1': e, 'C2': c}, 
                'R2': {'C2': c, 'C3': a}, 'C3': {'L2': e}, 'C4': {'Vout': f}, 
                'C5': {'R6': d}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d},
                'Vin': {'R1': d, 'R2': b}, 'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e},
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f},
                }
        case 6: circuit = {
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'R2': {'C2': c, 'C3': a}, 
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f},
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'Vout': None, 
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e}, 'C4': {'Vout': f}, 
                'C5': {'R6': d}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d}}
        case 7: circuit = {
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e}, 'C4': {'Vout': f}, 
                 'R2': {'C2': c, 'C3': a}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d},
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f},
                'Vout': None, 'L3': {'Vout': f}, 'L4': {'Vout': f}, 'C5': {'R6': d},
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}}
        case 8: circuit = {
                'Vout': None, 'L3': {'Vout': f}, 'L4': {'Vout': f}, 
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'R2': {'C2': c, 'C3': a}, 
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}, 'R6': {'Vout': f}, 
                'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e}, 'C3': {'L2': e}, 'C4': {'Vout': f}, 
                'C5': {'R6': d}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d}}
        case 9: circuit = {
                'C5': {'R6': d}, 'C1': {'L1': a}, 'C2': {'L1': a, 'L2': e},
                'Vin': {'R1': d, 'R2': b}, 'R1': {'C1': e, 'C2': c}, 'R2': {'C2': c, 'C3': a},        
                 'C3': {'L2': e}, 'C4': {'Vout': f}, 'L1': {'R3': c, 'C4': b}, 'L2': {'R4': d},
                'L3': {'Vout': f}, 'L4': {'Vout': f}, 'Vout': None, 'R6': {'Vout': f},
                'R3': {'C3': b}, 'R4': {'C4': a}, 'R5': {'Vout': f}}

    print("Calculate the shortest path from Vin to Vout. Given the circuit provided here.")
    print(f"Hint {f}, {b}, {a}")

    shortest_path = input()

    trace_value = list(trace.values())[pick_a_card]

    Vdrop = int(current * (trace_value * (shortest_path/4107)))


main()