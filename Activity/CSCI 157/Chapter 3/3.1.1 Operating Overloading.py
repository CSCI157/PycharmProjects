__author__ = 'Fosssum'


class CPU:
    def __init__(self, manufacturer, processor_type, processor_speed, processor_cache, cores, rating):
        self.manufacturer = manufacturer
        self.processor_type = processor_type
        self.processor_speed = processor_speed
        self.processor_cache = processor_cache
        self.cores = cores
        self.rating = rating

    def __str__(self):
        header = "The " + self.manufacturer + self.processor_type + " has " + str(self.cores) + " cores, a " +\
                 str(self.processor_cache) + "MB cache, runs at " + str(self.processor_speed) +\
                 "Ghz and has a rating of " + str(self.rating) + "."
        return header

    def __lt__(self, other):
        if self.cores < other.cores:
            return True
        elif self.cores == other.cores:
            if self.processor_speed < other.processor_speed:
                return True
            elif self.processor_speed == other.processor_speed:
                if self.processor_cache < other.processor_cache:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.cores > other.cores:
            return True
        elif self.cores == other.cores:
            if self.processor_speed > other.processor_speed:
                return True
            elif self.processor_speed == other.processor_speed:
                if self.processor_cache > other.processor_cache:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.manufacturer == other.manufacturer:
            if self.cores == other.cores:
                if self.processor_speed == other.processor_speed:
                    if self.processor_cache == other.processor_cache:
                        if self.rating == other.rating:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __int__(self):
        return self.rating

    def __contains__(self, item):
        if item in self.manufacturer or self.processor_type:
            return str(self)
        else:
            return False


class HardDrive:
    def __init__(self, manufacturer, drive_size, transfer_rate, cache, rating):
        self.manufacturer = manufacturer
        self.drive_size = drive_size
        self.transfer_rate = transfer_rate
        self.drive_cache = cache
        self.rating = rating

    def __str__(self):
        header = "The " + self.manufacturer + " hard drive has " + str(self.drive_size) +\
                 "TB of storage, a data transfer rate of " + str(self.transfer_rate) + "Gbps, a cache of " +\
                 str(self.drive_cache) + "MB, and a rating of " + str(self.rating) + "."
        return header

    def __lt__(self, other):
        if self.drive_size < other.drive_size:
            return True
        elif self.drive_size == other.drive_size:
            if self.transfer_rate < other.transfer_rate:
                return True
            elif self.transfer_rate == other.transfer_rate:
                if self.drive_cache < other.drive_cache:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.drive_size > other.drive_size:
            return True
        elif self.drive_size == other.drive_size:
            if self.transfer_rate > other.transfer_rate:
                return True
            elif self.transfer_rate == other.transfer_rate:
                if self.drive_cache > other.drive_cache:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.manufacturer == other.manufacturer:
            if self.drive_size == other.drive_size:
                if self.transfer_rate == other.transfer_rate:
                    if self.drive_cache == other.drive_cache:
                        if self.rating == other.rating:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __int__(self):
        return self.rating

    def __contains__(self, item):
        if item in self.manufacturer:
            return str(self)
        else:
            return False


class RAM:
    def __init__(self, manufacturer, ram_type, size, rating):
        self.manufacturer = manufacturer
        self.type = ram_type
        self.size = size
        self.rating = rating

    def __str__(self):
        header = "The ram was made by " + self.manufacturer + " is of type " + self.type + ", has a size of " +\
                 str(self.size) + "Gb, and a rating of " + str(self.rating) + "."
        return header

    def __lt__(self, other):
        if "SDRAM" in self.type:
            if "SDRAM" not in other.type:
                return True
            elif "SDRAM" in other.type:
                if self.type < other.type:
                    return True
                else:
                    return False
            else:
                pass
        elif "DDR" in self.type:
            if "SDRAM" in other.type:
                return False
            elif "DDR" not in other.type:
                return True
            elif "DDR" in other.type:
                if self.type < other.type:
                    return True
                else:
                    return False
            else:
                pass
        elif "Rambus" in self.type:
            if "SDRAM" in other.type:
                return False
            elif "DDR" in other.type:
                return False
            elif "Rambus" not in other.type:
                return True
            elif "Rambus" in other.type:
                if self.type < other.type:
                    return True
                else:
                    return False
            else:
                pass
        elif "GDDR" in self.type:
            if "GDDR" in other.type:
                if self.type < other.type:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return "No data on RAM found."

    def __gt__(self, other):
        if "GDDR" in self.type:
            if "GDDR" not in other.type:
                return True
            elif "GDDR" in other.type:
                if self.type > other.type:
                    return True
                else:
                    return False
            else:
                pass
        elif "Rambus" in self.type:
            if "GDDR" in other.type:
                return False
            elif "Rambus" not in other.type:
                return True
            elif "Rambus" in other.type:
                if self.type > other.type:
                    return True
                else:
                    return False
            else:
                pass
        elif "DDR" in self.type:
            if "GDDR" in other.type:
                return False
            elif "Rambus" in other.type:
                return False
            elif "Rambus" not in other.type:
                return True
            elif "DDR" in other.type:
                if self.type > other.type:
                    return True
                else:
                    return False
            else:
                pass
        elif "SDRAM" in self.type:
            if "SDRAM" in other.type:
                if self.type > other.type:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return "No data on RAM found."

    def __eq__(self, other):
        if self.manufacturer == other.manufacturer:
            if self.type == other.type:
                if self.size == other.size:
                    if self.rating == other.rating:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __int__(self):
        return self.rating

    def __contains__(self, item):
        if item in self.manufacturer or self.type or self.size:
            return str(self)
        else:
            return False


class GraphicsCard:
    def __init__(self, manufacturer, g_coprocessor, g_ram, rating):
        self.manufacturer = manufacturer
        self.g_coprocessor = CPU(g_coprocessor[0], g_coprocessor[1], g_coprocessor[2], g_coprocessor[3],
                                 g_coprocessor[4], g_coprocessor[5])
        self.g_ram = RAM(g_ram[0], g_ram[1], g_ram[2], g_ram[3])
        self.rating = rating

    def __str__(self):
        header = "This graphics card was made by " + self.manufacturer + " as a coprocessor and coRAM it has:\n " +\
                 str(self.g_coprocessor) + "\n " + str(self.g_ram) + "\n With an graphics card rating of " +\
                 str(self.rating) + "."
        return header

    def __lt__(self, other):
        if self.g_ram < other.g_ram:
            return True
        elif self.g_ram == other.g_ram:
            if self.g_coprocessor < self.g_coprocessor:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.g_ram > other.g_ram:
            return True
        elif self.g_ram == other.g_ram:
            if self.g_coprocessor > self.g_coprocessor:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.manufacturer == other.manufacturer:
            if self.g_coprocessor == other.g_coprocessor:
                if self.g_ram == other.g_ram:
                    if self.rating == other.rating:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __int__(self):
        return self.rating

    def __contains__(self, item):
        if item in self.manufacturer or self.g_coprocessor or self.g_ram:
            return str(self)
        else:
            return False


class Computer:
    def __init__(self, cpu, hard_drive, graphics_card, computer_ram, rating):
        self.cpu = CPU(cpu[0], cpu[1], cpu[2], cpu[3], cpu[4], cpu[5])
        self.ram = RAM(computer_ram[0], computer_ram[1], computer_ram[2], computer_ram[3])
        self.hard_drive = HardDrive(hard_drive[0], hard_drive[1], hard_drive[2], hard_drive[3], hard_drive[4])
        self.graphics_card = GraphicsCard(graphics_card[0], graphics_card[1], graphics_card[2], graphics_card[3])
        self.rating = str(rating)

    def __str__(self):
        header = "\nThis computer was build with the following components:\n" + str(self.cpu) + "\n" +\
                 str(self.hard_drive) + "\n" + str(self.graphics_card) + "\n" + str(self.ram) +\
                 "\nThis computer has an over all rating of " + self.rating + ".\n"
        return header

    def __lt__(self, other):
        return int(self) < int(other)


    def __gt__(self, other):
        if int(self) > int(other):
            return True
        else:
            return False

    def __eq__(self, other):
        if int(self) == int(other):
            return True
        else:
            return False

    def __int__(self):
        number = int(0.4*int(self.cpu) + 0.2*int(self.ram) + 0.2*int(self.hard_drive) + 0.2*int(self.graphics_card))
        return number

    def __contains__(self, item):
        if item in self.cpu or self.ram or self.hard_drive or self.graphics_card:
            return True
        else:
            return False

processors = [["Intel ", "Core i5-6600K", 3.5, 6, 4, 8], ["Intel ", "Core i3-6100", 3.7, 3, 2, 7],
              ["AMD", "-FX_8320", 4.0, 8, 8, 9], ["Intel ", "Core 2 3.6 Ghz", 3.6, 6, 2, 7],
              ["Intel ", "Core 2 4.0 Ghz", 4.0, 8, 2, 9]]
harddrives = [["Western Digital Jim Bob", 4, 6, 32, 4], ["Seagate Jane Bob", 4, 4, 64, 5]]
graphicscards = [["EVGA GeForce GTX 1050 Ti SC GAMING", ["Intel ", "Core 2 3.6 Ghz", 3.6, 6, 2, 7],
                  ["EVGA", "GDDR5", 4, 8], 8],
                 ["Gigabyte Radeon Rx 460 Windforce",["Intel ", "Core 2 4.0 Ghz", 4.0, 8, 2, 9],
                  ["Gigabyte Radeon", "GDDR4", 4, 7], 8]]
ram = [["Intel", "Rambus", 32, 7], ["Intel", "DDR", 64, 8]]


def main_menu():
    print("What would you like to do?\n1. Print values of a component\n2. Compare the valuse of two components\n"
          "3. Build a computer\n4. Print a computer\n5. Check computers for 'GeForce'\n6. Compare computers\n7. Quit")
    choice = input("Please type in your choice: ")
    try:
        choice = int(choice)
        if not (1 <= choice <= 7):
            choice = main_menu()
    except ValueError:
        choice = main_menu()
    return choice


def menu1():
    print("\n  Please pick the type of component you would like to print the values of:\n  1. Processor\n"
          "  2. Hard drive\n  3. Graphics card\n  4. RAM\n  5. Go back to main menu")
    choice1 = input("  Please type in your choice: ")
    try:
        choice1 = int(choice1)
        if not (1 <= choice1 <= 5):
            choice1 = menu1()
    except ValueError:
        choice1 = menu1()
    return choice1


def menu1_1():
    print("\n    Please pick the processor you would like to print the values of:\n    1. Intel Core i5-6600K\n"
          "    2. Intel Core i3-6100\n    3. AMD-FX_8320\n    4. Intel Core 2 3.6 GHz\n    5. Intel Core 2 4.0 GHz\n"
          "    6. Return to main menu")
    choice1_1 = input("    Please type in your choice: ")
    try:
        choice1_1 = int(choice1_1)
        if not (1 <= choice1_1 <= 6):
            choice1_1 = menu1_1()
    except ValueError:
        choice1_1 = menu1_1()
    return choice1_1


def menu1_2():
    print("\n    Please pick the hard drive you like to print the value of:\n    1. Western Digital Jim Bob\n"
          "    2. Seagate Jane Bob\n    3. Return to main menu")
    choice1_2 = input("    Please type in your choice: ")
    try:
        choice1_2 = int(choice1_2)
        if not (1 <= choice1_2 <= 3):
            choice1_2 = menu1_2()
    except ValueError:
        choice1_2 = menu1_2()
    return choice1_2


def menu1_3():
    print("\n    Please pick the graphics card you would like to print the value of:\n"
          "    1. EVGA GeForce GTX 1050 Ti SC GAMING\n    2. Gigabyte Radeon Rx 460 Windforce\n"
          "    3. Return to main menu")
    choice1_3 = input("    Please type in your choice: ")
    try:
        choice1_3 = int(choice1_3)
        if not (1 <= choice1_3 <= 3):
            choice1_3 = menu1_3()
    except ValueError:
        choice1_3 = menu1_3()
    return choice1_3


def menu1_4():
    print("\n    Please pick the RAM you would like to print the value of:\n    1. Intel Rambus\n    2. Intel DDR\n"
          "    3. Return to main menu")
    choice1_4 = input("    Please type in your choice: ")
    try:
        choice1_4 = int(choice1_4)
        if not (1 <= choice1_4 <= 3):
            choice1_4 = menu1_4()
    except ValueError:
        choice1_4 = menu1_4()
    return choice1_4


def menu2():
    print("\n  Please pick the type of component you would like to compare:\n  1. Processor\n  2. Hard drive\n"
          "  3. Graphics card\n  4. Go back to main menu")
    choice2 = input("  Please type in your choice: ")
    try:
        choice2 = int(choice2)
        if not (1 <= choice2 <= 4):
            choice2 = menu2()
    except ValueError:
        choice2 = menu2()
    return choice2


def menu2_1():
    print("\n    Please pick the first processor you would like to compare:\n    1. Intel Core i5-6600K\n"
          "    2. Intel Core i3-6100\n    3. AMD-FX_8320\n    4. Intel Core 2 3.6 GHz\n    5. Intel Core 2 4.0 GHz\n"
          "    6. Return to main menu")
    choice2_1 = input("    Please type in your choice: ")
    try:
        choice2_1 = int(choice2_1)
        if not (1 <= choice2_1 <= 6):
            choice2_1 = menu2_1()
    except ValueError:
        choice2_1 = menu2_1()
    return choice2_1


def menu2_1_2():
    print("\n      Please pick the second processor you would like to compare:\n      1. Intel Core i5-6600K\n"
          "      2. Intel Core i3-6100\n      3. AMD-FX_8320\n      4. Intel Core 2 3.6 GHz\n"
          "      5. Intel Core 2 4.0 GHz")
    choice2_1_2 = input("      Please type in your choice: ")
    try:
        choice2_1_2 = int(choice2_1_2)
        if not (1 <= choice2_1_2 <= 5):
            choice2_1_2 = menu2_1_2()
    except ValueError:
        choice2_1_2 = menu2_1_2()
    return choice2_1_2


def menu3():
    print("\n  You may only have two built computers.\n"
          "  Would you like to delete the current list and rebuild? 1 for YES, 2 for NO.")
    choice3 = input("  Please type in your choice: ")
    try:
        choice3 = int(choice3)
        if not (1 <= choice3 <= 2):
            choice3 = menu3()
    except ValueError:
        choice3 = menu3()
    return choice3


def menu3_1():
    print("\n    Please pick the processor you would like to put in the computer:\n    1. Intel Core i5-6600K\n"
          "    2. Intel Core i3-6100\n    3. AMD-FX_8320\n    4. Intel Core 2 3.6 GHz\n    5. Intel Core 2 4.0 GHz")
    choice3_1 = input("    Please type in your choice: ")
    try:
        choice3_1 = int(choice3_1)
        if not (1 <= choice3_1 <= 5):
            choice3_1 = menu3_1()
    except ValueError:
        choice3_1 = menu3_1()
    return choice3_1


def menu3_2():
    print("\n    Please pick the hard drive you like to put in the computer:\n    1. Western Digital Jim Bob\n"
          "    2. Seagate Jane Bob")
    choice3_2 = input("    Please type in your choice: ")
    try:
        choice3_2 = int(choice3_2)
        if not (1 <= choice3_2 <= 2):
            choice3_2 = menu3_2()
    except ValueError:
        choice3_2 = menu3_2()
    return choice3_2


def menu3_3():
    print("\n    Please pick the graphics card you would like to put in the computer:\n"
          "    1. EVGA GeForce GTX 1050 Ti SC GAMING\n    2. Gigabyte Radeon Rx 460 Windforce")
    choice3_3 = input("    Please type in your choice: ")
    try:
        choice3_3 = int(choice3_3)
        if not (1 <= choice3_3 <= 2):
            choice3_3 = menu3_3()
    except ValueError:
        choice3_3 = menu3_3()
    return choice3_3


def menu3_4():
    print("\n    Please pick the RAM you would like to put in the computer:\n    1. Intel Rambus\n    2. Intel DDR")
    choice3_4 = input("    Please type in your choice: ")
    try:
        choice3_4 = int(choice3_4)
        if not (1 <= choice3_4 <= 2):
            choice3_4 = menu3_4()
    except ValueError:
        choice3_4 = menu3_4()
    return choice3_4


def menu4():
    print("\n  Please pick the computer you would like to print:\n  1. Computer 1\n  2. Computer 2")
    choice4 = input("  Please type in your choice: ")
    try:
        choice4 = int(choice4)
        if not (1 <= choice4 <= 2):
            choice4 = menu4()
    except ValueError:
        choice4 = menu4()
    return choice4

choice = 0
choice1 = 0
choice1_1 = 0
choice1_2 = 0
choice1_3 = ""
choice1_4 = 0
choice2 = 0
choice2_1 = 0
choice2_1_2 = 0
choice3 = 0
choice3_1 = 0
choice3_2 = 0
choice3_3 = 0
choice3_4 = 0
choice4 = 0

computers = []

while choice != 7:
    choice = main_menu()
    if choice == 1:
        choice1 = menu1()
        if choice1 == 1:
            choice1_1 = menu1_1()
            if choice1_1 == 1:
                print(str(CPU(processors[0][0], processors[0][1], processors[0][2], processors[0][3], processors[0][4],
                              processors[0][5])))
            elif choice1_1 == 2:
                print(str(CPU(processors[1][0], processors[1][1], processors[1][2], processors[1][3], processors[1][4],
                              processors[1][5])))
            elif choice1_1 == 3:
                print(str(CPU(processors[2][0], processors[2][1], processors[2][2], processors[2][3], processors[2][4],
                              processors[2][5])))
            elif choice1_1 == 4:
                print(str(CPU(processors[3][0], processors[3][1], processors[3][2], processors[3][3], processors[3][4],
                              processors[3][5])))
            elif choice1_1 == 5:
                print(str(CPU(processors[4][0], processors[4][1], processors[4][2], processors[4][3], processors[4][4],
                              processors[4][5])))
            elif choice1_1 == 6:
                pass
        elif choice1 == 2:
            choice1_2 = menu1_2()
            if choice1_2 == 1:
                print(str(HardDrive(harddrives[0][0], harddrives[0][1], harddrives[0][2], harddrives[0][3],
                                    harddrives[0][4])))
            elif choice1_2 == 2:
                print(str(HardDrive(harddrives[1][0], harddrives[1][1], harddrives[1][2], harddrives[1][3],
                                    harddrives[1][4])))
            elif choice1_2 == 3:
                pass
        elif choice1 == 3:
            choice1_3 = menu1_3()
            if choice1_3 == 1:
                print(str(GraphicsCard(graphicscards[0][0], graphicscards[0][1], graphicscards[0][2],
                                       graphicscards[0][3])))
            elif choice1_3 == 2:
                print(str(GraphicsCard(graphicscards[1][0], graphicscards[1][1], graphicscards[1][2],
                                       graphicscards[1][3])))
            elif choice1_3 == 3:
                pass
        elif choice1 == 4:
            choice1_4 = menu1_4()
            if choice1_4 == 1:
                print(str(RAM(ram[0][0], ram[0][1], ram[0][2], ram[0][3])))
            elif choice1_4 == 2:
                print(str(RAM(ram[1][0], ram[1][1], ram[1][2], ram[1][3])))
            elif choice1_4 == 3:
                pass
        elif choice1 == 5:
            pass
    elif choice == 2:
        choice2 = menu2()
        if choice2 == 1:
            choice2_1 = menu2_1()
            processor_comp_list = []
            if choice2_1 == 1:
                processor_comp_list += [processors[0]]
                choice2_1_2 = menu2_1_2()
                if choice2_1_2 == 1:
                    processor_comp_list += [processors[0]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 2:
                    processor_comp_list += [processors[1]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 3:
                    processor_comp_list += [processors[2]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 4:
                    processor_comp_list += [processors[3]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 5:
                    processor_comp_list += [processors[4]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
            elif choice2_1 == 2:
                processor_comp_list += [processors[1]]
                choice2_1_2 = menu2_1_2()
                if choice2_1_2 == 1:
                    processor_comp_list += [processors[0]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 2:
                    processor_comp_list += [processors[1]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 3:
                    processor_comp_list += [processors[2]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 4:
                    processor_comp_list += [processors[3]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 5:
                    processor_comp_list += [processors[4]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
            elif choice2_1 == 3:
                processor_comp_list += [processors[2]]
                choice2_1_2 = menu2_1_2()
                if choice2_1_2 == 1:
                    processor_comp_list += [processors[0]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 2:
                    processor_comp_list += [processors[1]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 3:
                    processor_comp_list += [processors[2]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 4:
                    processor_comp_list += [processors[3]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 5:
                    processor_comp_list += [processors[4]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
            elif choice2_1 == 4:
                processor_comp_list += [processors[3]]
                choice2_1_2 = menu2_1_2()
                if choice2_1_2 == 1:
                    processor_comp_list += [processors[0]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 2:
                    processor_comp_list += [processors[1]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 3:
                    processor_comp_list += [processors[2]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 4:
                    processor_comp_list += [processors[3]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 5:
                    processor_comp_list += [processors[4]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
            elif choice2_1 == 5:
                processor_comp_list += [processors[4]]
                choice2_1_2 = menu2_1_2()
                if choice2_1_2 == 1:
                    processor_comp_list += [processors[0]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 2:
                    processor_comp_list += [processors[1]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 3:
                    processor_comp_list += [processors[2]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 4:
                    processor_comp_list += [processors[3]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
                elif choice2_1_2 == 5:
                    processor_comp_list += [processors[4]]
                    print("Processor 1 is less than processor 2:")
                    print(CPU(processor_comp_list[0][0], processor_comp_list[0][1], processor_comp_list[0][2],
                              processor_comp_list[0][3], processor_comp_list[0][4], processor_comp_list[0][5]) <
                          CPU(processor_comp_list[1][0], processor_comp_list[1][1], processor_comp_list[1][2],
                              processor_comp_list[1][3], processor_comp_list[1][4], processor_comp_list[1][5]))
            elif choice2_1 == 6:
                pass
        elif choice2 == 2:
            print("There are only two hard drives on file:\n1. Western Digital Jim Bob\n2. Seagate Jane Bob\n")
            print("Hard drive 1 is less than hard drive 2:")
            print(HardDrive(harddrives[0][0], harddrives[0][1], harddrives[0][2], harddrives[0][3], harddrives[0][4]) <
                  HardDrive(harddrives[1][0], harddrives[1][1], harddrives[1][2], harddrives[1][3], harddrives[1][4]))
        elif choice2 == 3:
            print("There are only two graphics cards on file:\n1. EVGA GeForce GTX 1050 Ti SC GAMING\n"
                  "2. Gigabyte Radeon Rx 460 Windforce\n")
            print("Graphics card 1 is less than graphics card 2:")
            print(GraphicsCard(graphicscards[0][0], graphicscards[0][1], graphicscards[0][2], graphicscards[0][3]) <
                  GraphicsCard(graphicscards[1][0], graphicscards[1][1], graphicscards[1][2], graphicscards[1][3]))
        elif choice2 == 4:
            pass
    elif choice == 3:
        if len(computers) == 0:
            choice3_1 = menu3_1()
            if choice3_1 == 1:
                computers = [[[], [], [], [], []]]
                computers[0][0] = processors[0]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[0] += []
                    computers[0][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[0] += []
                    computers[0][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 2:
                computers = [[[], [], [], [], []]]
                computers[0][0] = processors[1]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[0] += []
                    computers[0][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[0] += []
                    computers[0][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 3:
                computers = [[[], [], [], [], []]]
                computers[0][0] = processors[2]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[0] += []
                    computers[0][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = [graphicscards[1]]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = int(input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[0] += []
                    computers[0][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 4:
                computers = [[[], [], [], [], []]]
                computers[0][0] = processors[3]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[0] += []
                    computers[0][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = [graphicscards[1]]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[0] += []
                    computers[0][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 5:
                computers = [[[], [], [], [], []]]
                computers[0][0] = processors[4]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[0] += []
                    computers[0][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[0] += []
                    computers[0][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[0][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[0][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[0][3] = ram[0]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[0][3] = ram[1]
                            computers[0][4] = (input("Please enter the rating of the computer: "))
        elif len(computers) == 1:
            computers += [[[], [], [], [], []]]
            choice3_1 = menu3_1()
            if choice3_1 == 1:
                computers[1][0] = processors[0]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[1][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[1] += []
                    computers[1][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 2:
                computers[1][0] = processors[1]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[1][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[1][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 3:
                computers[1][0] = processors[2]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[1][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = [graphicscards[1]]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[1][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 4:
                computers[1][0] = processors[3]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[1][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[1][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
            elif choice3_1 == 5:
                computers[1][0] = processors[4]
                choice3_2 = menu3_2()
                if choice3_2 == 1:
                    computers[1][1] = harddrives[0]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                elif choice3_2 == 2:
                    computers[1][1] = harddrives[1]
                    choice3_3 = menu3_3()
                    if choice3_3 == 1:
                        computers[1][2] = graphicscards[0]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                    elif choice3_3 == 2:
                        computers[1][2] = graphicscards[1]
                        choice3_4 = menu3_4()
                        if choice3_4 == 1:
                            computers[1][3] = ram[0]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
                        elif choice3_4 == 2:
                            computers[1][3] = ram[1]
                            computers[1][4] = (input("Please enter the rating of the computer: "))
        elif len(computers) == 2:
            choice3 = menu3()
            if choice3 == 1:
                computers = []
            elif choice3 == 2:
                pass
    elif choice == 4:
        if len(computers) == 0:
            print("\nPlease build a computer before you print.\n")
        elif len(computers) >= 1:
            choice4 = menu4()
            if choice4 == 1:
                print(str(Computer(computers[0][0], computers[0][1], computers[0][2], computers[0][3],
                                   computers[0][4])))
            elif choice4 == 2:
                print(computers)
                if len(computers) == 1:
                    print("\nPlease build a second computer to print computer 2.\n")
                else:
                    print(str(Computer(computers[1][0], computers[1][1], computers[1][2], computers[1][3],
                                       computers[1][4])))
    elif choice == 5:
        if len(computers) == 0:
            print("\nPlease build a computer before checking for 'GeForce'.\n")
        elif len(computers) == 1:
            if "GeForce" in Computer(computers[0][0], computers[0][1], computers[0][2], computers[0][3],
                                     computers[0][4]):
                print("\nComputer 1 is using the EVGA GeForce GTX 1050 Ti SC GAMING graphics card.\n")
            else:
                print("\nNo built computers have 'GeForce' in them.\n")
        elif len(computers) == 2:
            if "GeForce" in Computer(computers[0][0], computers[0][1], computers[0][2], computers[0][3],
                                     computers[0][4]):
                print("\nComputer 1 is using the EVGA GeForce GTX 1050 Ti SC GAMING graphics card.\n")
            elif "GeForce" in Computer(computers[1][0], computers[1][1], computers[1][2], computers[1][3],
                                       computers[1][4]):
                print("\nComputer 2 is using the EVGA GeForce GTX 1050 Ti SC GAMING graphics card.\n")
            elif "GeForce" in Computer(computers[0][0], computers[0][1], computers[0][2], computers[0][3],
                                       computers[0][4]) and Computer(computers[1][0], computers[1][1], computers[1][2],
                                                                     computers[1][3], computers[1][4]):
                print("\nComputer 1 and 2 are using the EVGA GeForce GTX 1050 Ti SC GAMING graphics card.\n")
    elif choice == 6:
        if len(computers) != 2:
            print("\nPlease build two computers before comparing.\n")
        else:
            print("\nComputer 1 is less than computer 2:")
            print(Computer(computers[0][0], computers[0][1], computers[0][2], computers[0][3],
                           computers[0][4]) < Computer(computers[1][0], computers[1][1], computers[1][2],
                                                       computers[1][3], computers[1][4]))
            print("")
