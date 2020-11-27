class binary_number:
    def __init__(self, num=0):
        self.num = num

    def __str__(self):
        return str(self.num)

    def BinaryToDecimal(self):
        tbnum = self.num
        decimal = 0
        i = 0

        while tbnum != 0:
            digit = tbnum % 10

            decimal = decimal + digit * pow(2, i)
            tbnum = tbnum // 10
            i += 1

        return decimal

    def BinaryToOctal(self):
        return oct(self.BinaryToDecimal())

    def BinaryToHexadecimal(self):
        return hex(self.BinaryToDecimal())


class octal_number:
    def __init__(self, num=0):
        self.num = num

    def __str__(self):
        return str(self.num)

    def OctalToDecimal(self):
        toctnum = self.num
        decimal = 0
        i = 0

        while toctnum != 0:
            digit = toctnum % 10
            decimal = decimal + digit * pow(8, i)
            toctnum = toctnum // 10
            i += 1

        return decimal

    def OctalToBinary(self):
        return bin(self.OctalToDecimal())

    def OctalToHexadecimal(self):
        return hex(self.OctalToDecimal())


class hexadecimal_number:
    def __init__(self, num=0):
        self.num = num

    def __str__(self):
        return str(self.num)

    def HexadecimalToDecimal(self):
        thexnum = self.num
        decimal = 0
        i = 0

        while thexnum != 0:
            digit = thexnum % 10
            decimal = decimal + digit * pow(16, i)
            thexnum = thexnum // 10
            i += 1

        return decimal

    def HexadecimalToBinary(self):
        return bin(self.HexadecimalToDecimal())

    def HexadecimalToOctal(self):
        return oct(self.HexadecimalToDecimal())


class decimal_number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def DecimalToBinary(self):
        return bin(self.num)

    def DecimalToOctal(self):
        return oct(self.num)

    def DecimalToHexadecimal(self):
        return hex(self.num)


class calculator:
    def __init__(self, num1=0, num2=0, num_tp=""):
        self.num1 = num1
        self.num2 = num2
        self.num_tp = num_tp

    def addition(self):
        if self.num_tp == "dec":
            return self.num1 + self.num2

        elif self.num_tp == "bin":
            tnum1 = binary_number(self.num1)
            tnum2 = binary_number(self.num2)
            return bin(tnum1.BinaryToDecimal() + tnum2.BinaryToDecimal())

        elif self.num_tp == "oct":
            tnum1 = octal_number(self.num1)
            tnum2 = octal_number(self.num2)
            return oct(tnum1.OctalToDecimal() + tnum2.OctalToDecimal())

        elif self.num_tp == "hex":
            tnum1 = hexadecimal_number(self.num1)
            tnum2 = hexadecimal_number(self.num2)
            return hex(tnum1.HexadecimalToDecimal() + tnum2.HexadecimalToDecimal())

    def subtraction(self):
        if self.num_tp == "dec":
            return self.num1 - self.num2

        elif self.num_tp == "bin":
            a = binary_number(self.num1)
            b = binary_number(self.num2)
            return bin(a.BinaryToDecimal() - b.BinaryToDecimal())

        elif self.num_tp == "oct":
            tnum1 = octal_number(self.num1)
            tnum2 = octal_number(self.num2)
            return oct(tnum1.OctalToDecimal() - tnum2.OctalToDecimal())

        elif self.num_tp == "hex":
            tnum1 = hexadecimal_number(self.num1)
            tnum2 = hexadecimal_number(self.num2)
            return hex(tnum1.HexadecimalToDecimal() - tnum2.HexadecimalToDecimal())

    def multiplication(self):
        if self.num_tp == "dec":
            return self.num1 * self.num2

        elif self.num_tp == "bin":
            a = binary_number(self.num1)
            b = binary_number(self.num2)
            return bin(a.BinaryToDecimal() * b.BinaryToDecimal())

        elif self.num_tp == "oct":
            tnum1 = octal_number(self.num1)
            tnum2 = octal_number(self.num2)
            return oct(tnum1.OctalToDecimal() * tnum2.OctalToDecimal())

        elif self.num_tp == "hex":
            tnum1 = hexadecimal_number(self.num1)
            tnum2 = hexadecimal_number(self.num2)
            return hex(tnum1.HexadecimalToDecimal() * tnum2.HexadecimalToDecimal())

    def division(self):
        if self.num_tp == "dec":
            return self.num1 // self.num2

        elif self.num_tp == "bin":
            tnum1 = binary_number(self.num1)
            tnum2 = binary_number(self.num2)
            return bin(tnum1.BinaryToDecimal() // tnum2.BinaryToDecimal())

        elif self.num_tp == "oct":
            tnum1 = octal_number(self.num1)
            tnum2 = octal_number(self.num2)
            return oct(tnum1.OctalToDecimal() // tnum2.OctalToDecimal())

        elif self.num_tp == "hex":
            tnum1 = hexadecimal_number(self.num1)
            tnum2 = hexadecimal_number(self.num2)
            return hex(tnum1.HexadecimalToDecimal() // tnum2.HexadecimalToDecimal())


def menu():
    print("---------------------------------------------------------------------------------------")
    print("Welcome to the decimal, octal, hexadecimal, and binary numbers calculators and converters.")
    print("Enter bin to binary menu.")
    print("Enter oct to octal menu.")
    print("Enter dec to decimal menu.")
    print("Enter hex to hexadecimal menu.")
    print("Enter exit to terminate program.")
    print("----------------------------------------------------------------------------------------")

    ch = input(">> ")

    return ch


def menuf(strn):
    print("----------------------------------------")
    print("Welcome to the", strn, "Number menu.")
    print("Enter exit to exit from", strn, "Number.")
    print("Enter conv to", strn, "Number Conversion.")
    print("Enter calc to", strn, "Number Calculator.")
    print("----------------------------------------")

    ch = input(">> ")

    return ch


def menu_cv(strn, strn1, strn2, strn3, st, st1, st2):
    print("-------------------------------------------------------")
    print("Welcome to the", strn, "Number conversion menu.")
    print("Enter exit to Exit.")
    print("Enter", st, "to convert", strn, "number to", strn1, "number.")
    print("Enter", st1, "to convert", strn, " number to", strn2, "number.")
    print("Enter", st2, "to convert ", strn, "number to", strn3, "number.")
    print("-------------------------------------------------------")

    ccl = input(">> ")

    return ccl


def menu_cl(strn, strn1):
    print("-------------------------------------------------------")
    print("Welcome to the", strn, " Calculator menu.")
    print("Enter exit to Exit.")
    print("Enter + : ", strn1, " + ", strn1, ".")
    print("Enter - : ", strn1, " - ", strn1, ".")
    print("Enter * : ", strn1, " * ", strn1, ".")
    print("Enter / : ", strn1, " / ", strn1, ".")
    print("-------------------------------------------------------")

    ccl = input(">> ")

    return ccl


if __name__ == "__main__":
    print("Welcome to the Numbers Program.")
    print("This Program created by Enes Erten & Semih Vazgecen.\nTo support the Lecture of Logic Design Number System topics.")

    while True:
        ch = menu()

        if ch == "bin":
            while True:
                chb = menuf("Binary")

                if chb == "calc":
                    while True:
                        chbc = menu_cl("Binary", "BIN")

                        if chbc == '+':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first binary number\n>> "))
                            sbnum = int(input("Enter second binary number\n>> "))
                            a = calculator(fbnum, sbnum, "bin")

                            print(str(fbnum), " + ", str(sbnum), "=", str(a.addition()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == '-':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first binary number\n>> "))
                            sbnum = int(input("Enter second binary number\n>> "))
                            a = calculator(fbnum, sbnum, "bin")

                            print(str(fbnum), " - ", str(sbnum), "=", str(a.subtraction()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == '*':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first binary number\n>> "))
                            sbnum = int(input("Enter second binary number\n>> "))
                            a = calculator(fbnum, sbnum, "bin")

                            print(str(fbnum), " * ", str(sbnum), "=", str(a.multiplication()))
                            print("--------------------------------------------")
                            del a

                        elif chbc == '/':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first binary number\n>> "))
                            sbnum = int(input("Enter second binary number\n>> "))
                            a = calculator(fbnum, sbnum, "bin")

                            print(str(fbnum), " / ", str(sbnum), "=", str(a.division()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == "exit":
                            print("Exiting From Binary Number Calculation Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif chb == "conv":
                    while True:
                        chbcl = menu_cv("Binary", "Octal", "Decimal", "Hexadecimal", "BinToOct", "BinToDec", "BinToHex")

                        if chbcl == "BinToOct":
                            bnum = int(input("Enter a binary number\n>> "))
                            b = binary_number(bnum)
                            print(str(bnum), "BIN = OCT", str(b.BinaryToOctal()))

                            del b

                        elif chbcl == "BinToDec":
                            bnum = int(input("Enter a binary number\n>> "))
                            b = binary_number(bnum)
                            print(str(bnum), "BIN = DEC", str(b.BinaryToDecimal()))

                            del b

                        elif chbcl == "BinToHex":
                            bnum = int(input("Enter a binary number\n>> "))
                            b = binary_number(bnum)
                            print(str(bnum), "BIN = HEX", str(b.BinaryToHexadecimal()))

                            del b

                        elif chbcl == "exit":
                            print("Exiting from Binary Number Conversion Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif chb == "exit":
                    print("Exiting From Binary Menu.")
                    break

                else:
                    print("Invalid Input!\nPlease try again.")

        elif ch == "oct":
            while True:
                cho = menuf("Octal")

                if cho == "calc":
                    while True:
                        choc = menu_cl("Octal", "OCT")

                        if choc == '+':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first octal number\n>> "))
                            sbnum = int(input("Enter second octal number\n>> "))
                            a = calculator(fbnum, sbnum, "oct")

                            print(str(fbnum), " + ", str(sbnum), "=", str(a.addition()))
                            print("--------------------------------------------")

                            del a

                        elif choc == '-':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first octal number\n>> "))
                            sbnum = int(input("Enter second octal number\n>> "))
                            a = calculator(fbnum, sbnum, "oct")

                            print(str(fbnum), " - ", str(sbnum), "=", str(a.subtraction()))
                            print("--------------------------------------------")

                            del a

                        elif choc == '*':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first octal number\n>> "))
                            sbnum = int(input("Enter second octal number\n>> "))
                            a = calculator(fbnum, sbnum, "oct")

                            print(str(fbnum), " * ", str(sbnum), "=", str(a.multiplication()))
                            print("--------------------------------------------")

                            del a

                        elif choc == '/':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first octal number\n>> "))
                            sbnum = int(input("Enter second octal number\n>> "))
                            a = calculator(fbnum, sbnum, "oct")

                            print(str(fbnum), " / ", str(sbnum), "=", str(a.division()))
                            print("--------------------------------------------")

                            del a

                        elif choc == "exit":
                            print("Exiting From Octal Number Calculation Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif cho == "conv":
                    while True:
                        chbcl = menu_cv("Octal", "Binary", "Decimal", "Hexadecimal", "OctToBin", "OctToDec", "OctToHex")

                        if chbcl == "OctToBin":
                            onum = int(input("Enter a Octal number\n>> "))
                            b = octal_number(onum)
                            print(str(onum), "OCT = BIN", str(b.OctalToBinary()))

                            del b

                        elif chbcl == "OctToDec":
                            onum = int(input("Enter a Octal number\n>> "))
                            b = octal_number(onum)
                            print(str(onum), "OCT = DEC", str(b.OctalToDecimal()))

                            del b
                        elif chbcl == "OctToHex":
                            onum = int(input("Enter a Octal number\n>> "))
                            b = octal_number(onum)
                            print(str(onum), "Oct = HEX", str(b.OctalToHexadecimal()))

                            del b

                        elif chbcl == "exit":
                            print("Exiting from Octal Number Conversion Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif cho == "exit":
                    print("Exiting From Octal Menu.")
                    break

                else:
                    print("Invalid Input!\nPlease try again.")

        elif ch == "dec":
            while True:
                chd = menuf("Decimal")

                if chd == "calc":
                    while True:
                        chbc = menu_cl("Decimal", "Dec")

                        if chbc == '+':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Decimal number\n>> "))
                            sbnum = int(input("Enter second Decimal number\n>> "))
                            a = calculator(fbnum, sbnum, "dec")

                            print(str(fbnum), " + ", str(sbnum), "=", str(a.addition()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == '-':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Decimal number\n>> "))
                            sbnum = int(input("Enter second Decimal number\n>> "))
                            a = calculator(fbnum, sbnum, "dec")

                            print(str(fbnum), " - ", str(sbnum), "=", str(a.subtraction()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == '*':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Decimal number\n>> "))
                            sbnum = int(input("Enter second Decimal number\n>> "))
                            a = calculator(fbnum, sbnum, "dec")

                            print(str(fbnum), " * ", str(sbnum), "=", str(a.multiplication()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == '/':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Decimal number\n>> "))
                            sbnum = int(input("Enter second Decimal number\n>> "))
                            a = calculator(fbnum, sbnum, "dec")

                            print(str(fbnum), " / ", str(sbnum), "=", str(a.division()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == "exit":
                            print("Exiting From Decimal Number Calculation Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif chd == "conv":
                    while True:
                        chbcl = menu_cv("Decimal", "Binary", "Octal", "Hexadecimal", "DecToBin", "DecToOct", "DecToHex")

                        if chbcl == "DecToBin":
                            dnum = int(input("Enter a Decimal number\n>> "))
                            b = decimal_number(dnum)
                            print(str(dnum), "DEC = BIN", str(b.DecimalToBinary()))

                            del b

                        elif chbcl == "DecToOct":
                            dnum = int(input("Enter a Decimal number\n>> "))
                            b = decimal_number(dnum)
                            print(str(dnum), "DEC = BIN", str(b.DecimalToOctal()))

                            del b

                        elif chbcl == "DecToHex":
                            dnum = int(input("Enter a Decimal number\n>> "))
                            b = decimal_number(dnum)
                            print(str(dnum), "DEC = HEX", str(b.DecimalToHexadecimal()))

                            del b

                        elif chbcl == "exit":
                            print("Exiting from Binary Number Conversion Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif chd == "exit":
                    print("Exiting From Decimal Menu.")
                    break

                else:
                    print("Invalid Input!\nPlease try again.")

        elif ch == "hex":
            while True:
                chd = menuf("Hexadecimal")

                if chd == "calc":
                    while True:
                        chbc = menu_cl("Hexadecimal", "HEX")

                        if chbc == '+':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Hexadecimal number\n>> "))
                            sbnum = int(input("Enter second Hexadecimal number\n>> "))
                            a = calculator(fbnum, sbnum, "hex")

                            print(str(fbnum), " + ", str(sbnum), "=", str(a.addition()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == '-':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Hexadecimal number\n>> "))
                            sbnum = int(input("Enter second Hexadecimal number\n>> "))
                            a = calculator(fbnum, sbnum, "hex")

                            print(str(fbnum), " - ", str(sbnum), "=", str(a.subtraction()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == '*':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Hexadecimal number\n>> "))
                            sbnum = int(input("Enter second Hexadecimal number\n>> "))
                            a = calculator(fbnum, sbnum, "hex")

                            print(str(fbnum), " * ", str(sbnum), "=", str(a.multiplication()))
                            print("--------------------------------------------")
                            del a

                        elif chbc == '/':
                            print("--------------------------------------------")
                            fbnum = int(input("Enter first Hexadecimal number\n>> "))
                            sbnum = int(input("Enter second Hexadecimal number\n>> "))
                            a = calculator(fbnum, sbnum, "hex")

                            print(str(fbnum), " / ", str(sbnum), "=", str(a.division()))
                            print("--------------------------------------------")

                            del a

                        elif chbc == "exit":
                            print("Exiting From Hexadecimal Number Calculation Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif chd == "conv":
                    while True:
                        chbcl = menu_cv("Hexadecimal", "Binary", "Octal", "Decimal", "HexToBin", "HexToOct", "HexToDec")

                        if chbcl == "HexToBin":
                            hnum = int(input("Enter a Hexadecimal number\n>> "))
                            b = hexadecimal_number(hnum)
                            print(str(hnum), "HEX = BIN", str(b.HexadecimalToBinary()))

                            del b

                        elif chbcl == "HexToOct":
                            hnum = int(input("Enter a Hexadecimal number\n>> "))
                            b = hexadecimal_number(hnum)
                            print(str(hnum), "HEX = OCT", str(b.HexadecimalToOctal()))

                            del b

                        elif chbcl == "HexToDec":
                            hnum = int(input("Enter a Hexadecimal number\n>> "))
                            b = hexadecimal_number(hnum)
                            print(str(hnum), "HEX = DEC", str(b.HexadecimalToDecimal()))

                            del b

                        elif chbcl == "exit":
                            print("Exiting from Binary Number Conversion Menu.")
                            break

                        else:
                            print("Invalid Input!\nPlease try again.")

                elif chd == "exit":
                    print("Exiting From Hexadecimal Menu.")
                    break

                else:rd bias
                    print("Invalid Input!\nPlease try again.")

        elif ch == "exit":
            print("Terminating program")
            print("----------------------------------------------------------------------------------------")
            exit(0)

        else:
            print("Invalid Input!\nPlease Enter again.")