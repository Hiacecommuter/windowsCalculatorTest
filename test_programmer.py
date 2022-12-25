import unittest
from appium import webdriver

class Calculator_programmer_Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
         Establish connection with WinAppDriver Server
         Calculator and WinAppDriver is on PC with IP 192.168.1.157
         :return:
         """
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        desired_caps["platformName"] = "Windows"
        desired_caps["deviceName"] = "WindowsPC"
        self.driver = webdriver.Remote("http://192.168.1.157:4723", desired_caps)


    @classmethod
    def tearDownClass(self):
        """
        Close Calculator
        :return:
        """
        self.driver.quit()



    # def getInput(self):
    #     """
    #     Get the display of Input
    #     Strip space, letters, and radix character
    #     :return: The display text
    #     """
    #     displaytext = self.driver.find_element("accessibility id", value="Value1").text
    #     displaytext = displaytext.strip("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ")
    #     for j in displaytext:
    #         if j ==",":
    #             displaytext = displaytext.replace(",","")
    #     return displaytext

    # def getOutput(self):
    #     """
    #     Get the result
    #     Strip space, letters, and radix character
    #     :return:
    #     """
    #     displaytext2 = self.driver.find_element("accessibility id", value="Value2").text
    #     displaytext2 = displaytext2.strip("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ")
    #     for j in displaytext2:
    #         if j == ",":
    #             displaytext2 = displaytext2.replace(",", "")
    #     return displaytext2

    def getresults(self):
        """
        Get the display result
        Strip space and radix character
        :return: The display text
        """
        displaytext = self.driver.find_element("accessibility id", value="CalculatorResults").text
        displaytext = displaytext.replace("Display is ", "")
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')

        for j in displaytext:
            if j ==",":
                displaytext = displaytext.replace(",","")
            if j == " ":
                displaytext = displaytext.replace(" ", "")
        return displaytext

    def index_table(self, ch):
        """
        Convert single digit number or decimal point into AutomationId
        :param ch: a number or a decimal point
        :return: Automation Id
        """
        self.ch = ch
        if self.ch == ".":
            return "decimalSeparatorButton"
        else:
            return "num" + self.ch + "Button"

    def click_num(self, num):
        """
        Receive a number, then click it
        :param num: the number you want to click on panel
        :return:
        """
        minus_num = False
        self.num = num
        self.num = str(self.num)
        if self.num[0] == "-":
            minus_num = True
            self.num = self.num[1:]
        for digit in self.num:
            self.driver.find_element(by="accessibility id", value=self.index_table(digit) ).click()
        if minus_num:
            self.driver.find_element(by="accessibility id", value="negateButton").click()

    def index_table_hex(self, ch_hex):
        """
        Convert single hex digit into AutomationId
        :param ch:
        :return:
        """
        self.ch_hex = ch_hex
        return ch_hex.lower() + "Button"

    def click_hex(self, num_hex, type = "dec"):
        """
        Receive a number which is hex, dec, oct, or bin, then click it
        :param num:
        :return:
        """
        self.driver.find_element(by="accessibility id", value="fullKeypad").click()
        minus_num = False
        self.num_hex = num_hex

        if type.lower() == "hex":
            self.num_hex = hex(self.num_hex)
            self.driver.find_element(by="accessibility id", value="hexButton").click()
            self.num_hex = str(self.num_hex).replace("0x","")
        elif type.lower() == "oct":
            self.num_hex = oct(self.num_hex)
            self.driver.find_element(by="accessibility id", value="octolButton").click()
            self.num_hex = str(self.num_hex).replace("0o","")
        elif type.lower() == "bin":
            self.num_hex = bin(self.num_hex)
            self.driver.find_element(by="accessibility id", value="binaryButton").click()
            self.num_hex = str(self.num_hex).replace("0b","")
        else:
            self.driver.find_element(by="accessibility id", value="decimalButton").click()
            self.num_hex = str(self.num_hex)


        if self.num_hex[0] == "-":
            minus_num = True
            self.num_hex = self.num_hex[1:]
        for digit_hex in self.num_hex:
            if digit_hex.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
                self.driver.find_element(by="accessibility id", value=self.index_table_hex(digit_hex)).click()
            else:
                self.driver.find_element(by="accessibility id", value=self.index_table(digit_hex)).click()
        if minus_num:
            self.driver.find_element(by="accessibility id", value="negateButton").click()

    def bin_index(self, bin_digit):
        return "Bit" + bin_digit

    def bitFlip_choose(self, bitlen="q"):
        try:
            self.bit_len = self.driver.find_element(by="accessibility id", value="qwordButton").text
        except:
            pass
        try:
            self.bit_len = self.driver.find_element(by="accessibility id", value="dwordButton").text
        except:
            pass
        try:
            self.bit_len = self.driver.find_element(by="accessibility id", value="wordButton").text
        except:
            pass
        try:
            self.bit_len = self.driver.find_element(by="accessibility id", value="byteButton").text
        except:
            pass
        if self.bit_len == "Quadruple Word toggle":
            if bitlen.lower() == "q":
                pass
            elif bitlen.lower() == "d":
                self.driver.find_element(by="accessibility id", value="qwordButton").click()
            elif bitlen.lower() == "w":
                self.driver.find_element(by="accessibility id", value="qwordButton").click()
                self.driver.find_element(by="accessibility id", value="dwordButton").click()
            elif bitlen.lower() == "b":
                self.driver.find_element(by="accessibility id", value="qwordButton").click()
                self.driver.find_element(by="accessibility id", value="dwordButton").click()
                self.driver.find_element(by="accessibility id", value="wordButton").click()

        elif self.bit_len =="Double Word toggle":
            if bitlen.lower() == "q":
                self.driver.find_element(by="accessibility id", value="dwordButton").click()
                self.driver.find_element(by="accessibility id", value="wordButton").click()
                self.driver.find_element(by="accessibility id", value="byteButton").click()
            elif bitlen.lower() == "d":
                pass
            elif bitlen.lower() == "w":
                self.driver.find_element(by="accessibility id", value="dwordButton").click()
            elif bitlen.lower() == "b":
                self.driver.find_element(by="accessibility id", value="dwordButton").click()
                self.driver.find_element(by="accessibility id", value="wordButton").click()

        elif self.bit_len =="Word toggle":
            if bitlen.lower() == "q":
                self.driver.find_element(by="accessibility id", value="wordButton").click()
                self.driver.find_element(by="accessibility id", value="byteButton").click()
            elif bitlen.lower() == "d":
                self.driver.find_element(by="accessibility id", value="wordButton").click()
                self.driver.find_element(by="accessibility id", value="byteButton").click()
                self.driver.find_element(by="accessibility id", value="qwordButton").click()
            elif bitlen.lower() == "w":
                pass
            elif bitlen.lower() == "b":
                self.driver.find_element(by="accessibility id", value="wordButton").click()

        elif self.bit_len =="Byte toggle":
            if bitlen.lower() == "q":
                self.driver.find_element(by="accessibility id", value="byteButton").click()
            elif bitlen.lower() == "d":
                self.driver.find_element(by="accessibility id", value="byteButton").click()
                self.driver.find_element(by="accessibility id", value="qwordButton").click()
            elif bitlen.lower() == "w":
                self.driver.find_element(by="accessibility id", value="byteButton").click()
                self.driver.find_element(by="accessibility id", value="qwordButton").click()
                self.driver.find_element(by="accessibility id", value="dwordButton").click()
            elif bitlen.lower() == "b":
                pass

    def click_bin_keyboard(self, num_value, word_len_input = "q"):
        self.driver.find_element(by="accessibility id", value="bitFlip").click()
        # try:
        #     self.word_len = self.driver.find_element(by="accessibility id", value="qwordButton").text
        # except:
        #     pass
        # try:
        #     self.word_len = self.driver.find_element(by="accessibility id", value="dwordButton").text
        # except:
        #     pass
        # try:
        #     self.word_len = self.driver.find_element(by="accessibility id", value="wordButton").text
        # except:
        #     pass
        # try:
        #     self.word_len = self.driver.find_element(by="accessibility id", value="byteButton").text
        # except:
        #     pass
        #
        # if self.word_len == "Quadruple Word toggle":
        #     if word_len_input.lower() == "q":
        #         pass
        #     elif word_len_input.lower() == "d":
        #         self.driver.find_element(by="accessibility id", value="qwordButton").click()
        #     elif word_len_input.lower() == "w":
        #         self.driver.find_element(by="accessibility id", value="qwordButton").click()
        #         self.driver.find_element(by="accessibility id", value="dwordButton").click()
        #     elif word_len_input.lower() == "b":
        #         self.driver.find_element(by="accessibility id", value="qwordButton").click()
        #         self.driver.find_element(by="accessibility id", value="dwordButton").click()
        #         self.driver.find_element(by="accessibility id", value="wordButton").click()
        #
        # elif self.word_len =="Double Word toggle":
        #     if word_len_input.lower() == "q":
        #         self.driver.find_element(by="accessibility id", value="dwordButton").click()
        #         self.driver.find_element(by="accessibility id", value="wordButton").click()
        #         self.driver.find_element(by="accessibility id", value="byteButton").click()
        #     elif word_len_input.lower() == "d":
        #         pass
        #     elif word_len_input.lower() == "w":
        #         self.driver.find_element(by="accessibility id", value="dwordButton").click()
        #     elif word_len_input.lower() == "b":
        #         self.driver.find_element(by="accessibility id", value="dwordButton").click()
        #         self.driver.find_element(by="accessibility id", value="wordButton").click()
        #
        # elif self.word_len =="Word toggle":
        #     if word_len_input.lower() == "q":
        #         self.driver.find_element(by="accessibility id", value="wordButton").click()
        #         self.driver.find_element(by="accessibility id", value="byteButton").click()
        #     elif word_len_input.lower() == "d":
        #         self.driver.find_element(by="accessibility id", value="wordButton").click()
        #         self.driver.find_element(by="accessibility id", value="byteButton").click()
        #         self.driver.find_element(by="accessibility id", value="qwordButton").click()
        #     elif word_len_input.lower() == "w":
        #         pass
        #     elif word_len_input.lower() == "b":
        #         self.driver.find_element(by="accessibility id", value="wordButton").click()
        #
        # elif self.word_len =="Byte toggle":
        #     if word_len_input.lower() == "q":
        #         self.driver.find_element(by="accessibility id", value="byteButton").click()
        #     elif word_len_input.lower() == "d":
        #         self.driver.find_element(by="accessibility id", value="byteButton").click()
        #         self.driver.find_element(by="accessibility id", value="qwordButton").click()
        #     elif word_len_input.lower() == "w":
        #         self.driver.find_element(by="accessibility id", value="byteButton").click()
        #         self.driver.find_element(by="accessibility id", value="qwordButton").click()
        #         self.driver.find_element(by="accessibility id", value="dwordButton").click()
        #     elif word_len_input.lower() == "b":
        #         pass
        self.bitFlip_choose(word_len_input)
        self.num_value = str(bin(num_value)).replace("0b", "")
        if self.num_value[0] == "-":
            minus_hex = True
        else:
            minus_hex = False
        self.num_value = self.num_value[::-1]
        for i in range(0, len(self.num_value)):
            if self.num_value[i] == '1':
                self.driver.find_element(by="accessibility id", value= self.bin_index(str(i))).click()
        if minus_hex:
            self.driver.find_element(by="accessibility id", value="negateButton").click()




    def get_header(self):
        """
        Check the panel name
        :return: panel name
        """
        self.pane_header = self.driver.find_element(by="accessibility id", value="Header").text
        return self.pane_header

    """
    for all functions, input is dec
    display is hex, dec, oct, or bin depands on last input format
    """

    def test_000_initialize(self):
        """
        Choose Programmer panel
        :return:
        """
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by= "accessibility id", value="Programmer").click()
        self.assertEqual(self.get_header(), "Programmer")
    """
    bin, 1, 2, 3, 4, 5
    oct, 1, 7, 8, 29, 50
    dec, 1, 9, 10, 11, 45
    hex, 1, 15, 16, 17, 60
    """
    def test_001_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="bin")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "110")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(9, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1011")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(4, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "101")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(4, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "110")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(8, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "17")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(8, type="oct")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(29, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "45")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(29, type="oct")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(50, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "117")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(8, type="oct")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(50, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "72")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="dec")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "19")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(11, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "21")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="dec")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(45, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "56")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="dec")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(1, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(16, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1F")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(16, type="hex")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(17, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "21")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(17, type="hex")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4D")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_addition(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_hex(17, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "20")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    """
        bin 5, 11, 15 -- 3, 8
        oct 9, 15, 23 -- 7, 11 
        dec 9, 21, 35 -- 7, 13
        hex 15, 33, 56 -- 10, 20

    """


    def test_001_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.bitFlip_choose(bitlen="q")
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")


    def test_002_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(8, type="bin")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="bin")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()

    def test_004_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="bin")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(8, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="bin")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(8, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="oct")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="oct")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(9, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="oct")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="oct")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(11, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(23, type="oct")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(11, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "14")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_subtructionn(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(13, type="dec")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(21, type="dec")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "14")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(21, type="dec")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(13, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "8")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(35, type="dec")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "28")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(10, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "5")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(20, type="hex")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "5")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(33, type="hex")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(10, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "17")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(33, type="hex")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(20, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "D")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_subtruction(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(56, type="hex")
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_hex(10, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2E")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    """
        bin 2, 3, 5 -- 2, 3
        oct 7, 11, 13 -- 4, 5
        dec 9, 15, 17 -- 7, 9
        hex 33, 60, 101- - 15, 40

    """

    def test_001_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "100")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "110")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1001")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1010")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "34")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(5, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "43")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="oct")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "54")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="oct")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(5, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "67")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(13, type="oct")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "64")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "63")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "81")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="dec")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "105")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="dec")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "135")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(17, type="dec")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "119")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(33, type="hex")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1EF")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(33, type="hex")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(40, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "528")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "384")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(40, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "960")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_multiple(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(101, type="hex")
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "5EB")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    """
        bin 2, 3, 5 -- 0 2, 3
        oct 7, 11, 13 -- 0 4, 5
        dec 9, 15, 17 -- 0 7, 9
        hex 33, 60, 101- - 0 15, 40
    
    """

    def test_001_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="bin")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannotdividebyzero")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(7, type="bin")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="bin")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(4, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(13, type="bin")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="bin")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(0, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannotdividebyzero")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="oct")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(13, type="oct")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(5, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(13, type="oct")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "3")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_divisionn(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="dec")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(0, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannotdividebyzero")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="dec")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(17, type="dec")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(17, type="dec")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="hex")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(0, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannotdividebyzero")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(33, type="hex")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(101, type="hex")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "6")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_division(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(101, type="hex")
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_hex(40, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()

    """
    bin 9, 17, 99
    oct 5, 10, 25
    dec 13, 99, 123
    hex 49, 166, 1001
    
    2, 3, 5
    """
    def test_001_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="bin")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="bin")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(17, type="bin")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(17, type="bin")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(99, type="bin")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(5, type="oct")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(10, type="oct")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(10, type="oct")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(25, type="oct")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(25, type="oct")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(13, type="dec")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(99, type="dec")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(99, type="dec")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(123, type="dec")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(123, type="dec")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(5, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "3")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(49, type="hex")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(2, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(66, type="hex")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(66, type="hex")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(3, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1001, type="hex")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(5, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_mod(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1001, type="hex")
        self.driver.find_element(by="accessibility id", value="modButton").click()
        self.click_hex(5, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    """
    bin 1, 2 , 3 ,4 ,5 
    oct 7 , 8, 10, 20, 100
    dec 9 , 10, 30, 99, 121
    hex 15, 19, 27, 101, 999 
    5, 4, 3, 2,1
    """

    def test_001_lefts(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1, type="bin")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "100000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_lefts(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(4, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "100000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_lefts(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(4, type="bin")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(1, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1010")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_lefts(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(5, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "340")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_lefts(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(8, type="oct")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "200")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_lefts(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(10, type="oct")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(3, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "120")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(20, type="oct")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(2, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "120")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(100, type="oct")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "310")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_lefts(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(5, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "288")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_lefts(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(4, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "160")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_lefts(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(30, type="dec")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(3, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "240")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(99, type="dec")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(2, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-116")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(121, type="dec")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(1, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-14")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_lefts(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(5, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1E0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_lefts(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(17, type="hex")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(4, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "110")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_lefts(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(27, type="hex")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(3, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "D8")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(101, type="hex")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(2, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "94")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_lefts(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(999, type="hex")
        self.driver.find_element(by="accessibility id", value="lshButton").click()
        self.click_hex(1, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "7C")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    """
    bin 11, 5, 3, 4, 2 
    oct 40, 31, 19, 13, 7
    dec 150 99 50 10 9
    hex 1501 480 121 33 15
    5, 4, 3 ,2 ,1
    """
    def test_001_rights(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(11, type="bin")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_002_rights(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(5, type="bin")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(4, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_003_rights(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_004_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(4, type="bin")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(2, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_005_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(3, type="bin")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(1, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_006_rights(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(40, type="oct")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(5, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_007_rights(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(31, type="oct")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(4, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_008_rights(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(19, type="oct")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(3, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_009_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(13, type="oct")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(2, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "3")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_010_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(7, type="oct")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "3")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_011_rights(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(150, type="dec")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(5, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_012_rights(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(99, type="dec")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(4, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "6")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_013_rights(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(50, type="dec")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(3, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "6")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_014_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(2, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_015_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(9, type="dec")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(1, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_016_rights(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1501, type="hex")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(5, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2E")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_017_rights(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(480, type="hex")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(4, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1E")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_018_rights(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(121, type="hex")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(3, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_019_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(33, type="hex")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(2, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "8")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_020_rights(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(15, type="hex")
        self.driver.find_element(by="accessibility id", value="rshButton").click()
        self.click_hex(1, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "7")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_001_and(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xFFFFFFFFFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_and(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(0xFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_and(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(15, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_and(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xF0F00F0F00000000, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(1148681852194652160, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "3600000740000000000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_and(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(252702960, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(267448335, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1700170000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_and(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFF00, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(4080, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "7400")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(42, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "50")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_and(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(71777214277877760, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(281470681743360, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1095216660480")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_and(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(16776960, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(267448320, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "15790080")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_and(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(-4081, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(-3856, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-4096")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(85, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "5")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(24, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "8")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_and(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1080880403494997760, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(281406508892160, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F000F000000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_and(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(251658480, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(150998784, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9000000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_and(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(21845, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(13107, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(14, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "C")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_and(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(102, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="andButton").click()
        self.click_hex(96, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "60")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_001_or(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xFFFFFFFFFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*64)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_or(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(0xFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*32)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_or(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*16)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*8)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(15, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11111111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_or(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xF0F00F0F00000000, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(1148681852194652160, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1777607760740000000000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_or(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(252702960, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(267448335, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1777770377")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_or(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFF00, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(4080, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "177760")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(42, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "76")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_or(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(71777214277877760, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(281470681743360, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "72057589742960640")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_or(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(16776960, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(267448320, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "268435200")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_or(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(-4081, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(-3856, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-3841")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(85, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "87")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(24, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "26")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_or(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1080880403494997760, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(281406508892160, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F00FFF00F000F00")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_or(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(251658480, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(150998784, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F000FF0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_or(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(21845, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(13107, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "7777")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(14, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "3E")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_or(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(102, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="orButton").click()
        self.click_hex(96, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "66")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_001_not(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xFFFFFFFFFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_not(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(0xFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_not(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_not(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xF0F00F0F00000000, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "74177417037777777777")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_not(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(252702960, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "36074007417")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_not(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFF00, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "377")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "303")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "377")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_not(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(71777214277877760, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "-71777214277877761")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_not(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(16776960, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "-16776961")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_not(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(-4081, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "4080")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(85, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "-86")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(24, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "-25")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_not(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1080880403494997760, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "F0FFF0FFF0FFF0FF")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_not(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(251658480, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "F0FFFF0F")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_not(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(21845, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "AAAA")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "C3")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_not(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(102, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="notButton").click()
        self.assertEqual(self.getresults(), "99")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_001_nand(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xFFFFFFFFFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*64)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_nand(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(0xFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*32)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_nand(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*16)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11111111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(15, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11110000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_nand(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xF0F00F0F00000000, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(1148681852194652160, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1774177777037777777777")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_nand(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(252702960, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(267448335, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "36077607777")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_nand(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFF00, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(4080, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "170377")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(42, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "327")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "377")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_nand(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(71777214277877760, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(281470681743360, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1095216660481")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_nand(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(16776960, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(267448320, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-15790081")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_nand(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(-4081, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(-3856, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4095")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(85, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-6")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(24, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-9")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_nand(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1080880403494997760, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(281406508892160, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "FFFFF0FFF0FFFFFF")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_nand(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(251658480, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(150998784, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F6FFFFFF")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_nand(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(21845, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(13107, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "EEEE")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(14, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F3")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_nand(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(102, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="nandButton").click()
        self.click_hex(96, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9F")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_001_nor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xFFFFFFFFFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_nor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(0xFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_nor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(15, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_nor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xF0F00F0F00000000, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(1148681852194652160, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "170017037777777777")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_nor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(252702960, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(267448335, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "36000007400")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_nor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFF00, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(4080, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "17")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(42, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "301")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_010_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "376")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_011_nor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(71777214277877760, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(281470681743360, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-72057589742960641")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_012_nor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(16776960, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(267448320, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-268435201")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_013_nor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(-4081, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(-3856, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "3840")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_014_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(85, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-88")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_015_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(24, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-27")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_016_nor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1080880403494997760, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(281406508892160, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F0FF000FF0FFF0FF")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_017_nor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(251658480, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(150998784, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F0FFF00F")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_018_nor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(21845, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(13107, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "8888")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_019_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(14, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "C1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_020_nor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(102, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="norButton").click()
        self.click_hex(96, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "99")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_001_xor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xFFFFFFFFFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*64)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_002_xor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(0xFFFFFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*32)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_003_xor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFFFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1"*16)
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_004_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(0, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11111111")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_005_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0xFF, type="bin")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(15, type="bin")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11110000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_006_xor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(0xF0F00F0F00000000, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(1148681852194652160, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1774007760000000000000")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_007_xor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(252702960, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(267448335, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "77600377")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_008_xor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(0xFF00, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(4080, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "170360")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_009_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(42, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "26")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_010_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(0, type="oct")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(1, type="oct")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_011_xor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(71777214277877760, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(281470681743360, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "72056494526300160")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_012_xor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(16776960, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(267448320, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "252645120")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_013_xor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(-4081, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(-3856, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "255")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_014_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(85, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(7, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "82")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_015_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(24, type="dec")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(10, type="dec")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "18")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_016_xor(self):
        self.bitFlip_choose(bitlen="q")
        self.click_hex(1080880403494997760, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(281406508892160, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "F00F0F000000F00")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_017_xor(self):
        self.bitFlip_choose(bitlen="d")
        self.click_hex(251658480, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(150998784, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "6000FF0")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_018_xor(self):
        self.bitFlip_choose(bitlen="w")
        self.click_hex(21845, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(13107, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "6666")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_019_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(60, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(14, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "32")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()



    def test_020_xor(self):
        self.bitFlip_choose(bitlen="b")
        self.click_hex(102, type="hex")
        self.driver.find_element(by="accessibility id", value="bitwiseButton").click()
        self.driver.find_element(by="accessibility id", value="xorButton").click()
        self.click_hex(96, type="hex")
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "6")
        try:
            self.driver.find_element(by="accessibility id", value="clearButton").click()
        except:
            self.driver.find_element(by="accessibility id", value="clearEntryButton").click()


    def test_001_bitkeyboard(self):
        self.click_bin_keyboard(0xffffffffffffffff, word_len_input="q")
        self.driver.find_element(by="accessibility id", value="hexButton").click()
        self.assertEqual(self.getresults(), "FFFFFFFFFFFFFFFF")

    def test_002_bitkeyboard(self):
        self.click_bin_keyboard(0xffffffff, word_len_input="d")
        self.driver.find_element(by="accessibility id", value="hexButton").click()
        self.assertEqual(self.getresults(), "FFFFFFFF")

    def test_003_bitkeyboard(self):
        self.click_bin_keyboard(0xffff, word_len_input="w")
        self.driver.find_element(by="accessibility id", value="hexButton").click()
        self.assertEqual(self.getresults(), "FFFF")

    def test_004_bitkeyboard(self):
        self.click_bin_keyboard(0xff, word_len_input="b")
        self.driver.find_element(by="accessibility id", value="hexButton").click()
        self.assertEqual(self.getresults(), "FF")




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_programmer_Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
