import unittest
from appium import webdriver

class Calculator_standard_Tests(unittest.TestCase):

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



    def getresults(self):
        """
        Get the display result
        Strip space and radix character
        :return: The display text
        """
        displaytext = self.driver.find_element("accessibility id", value="CalculatorResults").text
        displaytext = displaytext.strip("Display is ")
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        for j in displaytext:
            if j ==",":
                displaytext = displaytext.replace(",","")
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


    def get_header(self):
        """
        Check the panel name
        :return: panel name
        """
        self.pane_header = self.driver.find_element(by="accessibility id", value="Header").text
        return self.pane_header

    def test_00_initialize(self):
        """
        Choose Standard panel
        :return:
        """
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by= "accessibility id", value="Standard").click()
        self.assertEqual(self.get_header(), "Standard")
    """
    Test input as 1, 2, & 3 digits positive & negative integer
    0, 1, 9, 10, 99, 100, 999,  -1, -9, -10, -999
    Test input as positive & negative decimals 
    0.01, 0.1, 9.9, 99.01, 100.7, 999.99
    -0.01, -0.1, -9.9, -99.01, -100.7, -999.99    
    
    """
    def test_addition_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(0)
        self.driver.find_element(by = "accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")

    def test_addition_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")

    def test_addition_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(9)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "19")

    def test_addition_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "109")

    def test_addition_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "199")

    def test_addition_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1099")

    def test_addition_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1000")

    def test_addition_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-10")

    def test_addition_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-19")

    def test_addition_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-10)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1009")

    def test_addition_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1000")

    def test_addition_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1099")

    def test_addition_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1")


    def test_addition_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.01)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.11")

    def test_addition_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")

    def test_addition_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.01)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9.91")

    def test_addition_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99.01)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "108.91")

    def test_addition_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.7)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "199.71")

    def test_addition_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.7)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(999.99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1100.69")

    def test_addition_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.01)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-0.11")

    def test_addition_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-10")

    def test_addition_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-108.91")

    def test_addition_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100.7)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-199.71")

    def test_addition_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100.7)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-999.99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1100.69")

    def test_addition_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")

    def test_addition_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "19.9")

    def test_addition_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "989.1")

    def test_addition_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "11")

    def test_addition_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(10)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "108.91")

    def test_addition_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-1)
        self.driver.find_element(by = "accessibility id", value="plusButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-11.1")

    def test_subtraction_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")

    def test_subtraction_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")

    def test_subtraction_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(9)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1")

    def test_subtraction_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-89")

    def test_subtraction_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1")

    def test_subtraction_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "899")

    def test_subtraction_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "998")

    def test_subtraction_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "8")

    def test_subtraction_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")

    def test_subtraction_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "989")

    def test_subtraction_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "998")

    def test_subtraction_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "899")

    def test_subtraction_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1")

    def test_subtraction_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.01)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-0.09")

    def test_subtraction_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-9.8")

    def test_subtraction_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.01)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-9.89")

    def test_subtraction_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "89.11")

    def test_subtraction_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.7)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1.69")

    def test_subtraction_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.7)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(999.99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-899.29")

    def test_subtraction_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.01)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.09")

    def test_subtraction_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9.8")

    def test_subtraction_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "89.11")

    def test_subtraction_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100.7)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1.69")

    def test_subtraction_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100.7)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-999.99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "899.29")

    def test_subtraction_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-2")

    def test_subtraction_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.1")

    def test_subtraction_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1008.9")

    def test_subtraction_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-10.8")

    def test_subtraction_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-109.11")

    def test_subtraction_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10.9")

    def test_multiply_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")


    def test_multiply_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")


    def test_multiply_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(9)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "90")


    def test_multiply_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "990")


    def test_multiply_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9900")


    def test_multiply_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "99900")


    def test_multiply_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "999")


    def test_multiply_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9")


    def test_multiply_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "90")


    def test_multiply_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9990")


    def test_multiply_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "999")


    def test_multiply_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-999)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "99900")


    def test_multiply_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")


    def test_multiply_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.01)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.001")


    def test_multiply_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.99")


    def test_multiply_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.01)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.099")


    def test_multiply_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "980.199")


    def test_multiply_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.7)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9970.307")


    def test_multiply_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.7)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(999.99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "100698.993")


    def test_multiply_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.01)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.001")


    def test_multiply_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.99")


    def test_multiply_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "980.199")


    def test_multiply_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100.7)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "9970.307")


    def test_multiply_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-100.7)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-999.99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "100698.993")


    def test_multiply_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1")


    def test_multiply_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "99")


    def test_multiply_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-9890.1")


    def test_multiply_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(9.9)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.99")


    def test_multiply_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-99.01")


    def test_multiply_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="multiplyButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1")

    """
    0, 1, 3, 7, 11, 13, 99, 100,  
    -2, -5, -10, -23, -91, -101
    0.1, 0.3, 0.05, 0.007
    -0.11, -0.17, -0.019, -0.0023
    """

    def test_division_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannot divide by zero")


    def test_division_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(3)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "0.33333333")


    def test_division_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(7)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "0.14285714")


    def test_division_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(11)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "0.09090909")


    def test_division_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(13)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "0.07692307")


    def test_division_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "0.01010101")


    def test_division_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.01")


    def test_division_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-2)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-0.5")


    def test_division_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-5)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-0.4")


    def test_division_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(3)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-0.3")


    def test_division_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(4)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.1739130")


    def test_division_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(5)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-91)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0549450")


    def test_division_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(6)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-101)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0594059")


    def test_division_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "10")


    def test_division_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0.3)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "6.66666666")


    def test_division_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0.05)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "20")


    def test_division_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0.007)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "285.714285")


    def test_division_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-0.11)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-18.181818")


    def test_division_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-0.17)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-5.8823529")


    def test_division_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-0.019)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-52.631578")


    def test_division_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-0.0023)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-434.78260")


    def test_division_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9.9)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-99.01)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "0.09998990")


    def test_division_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-5)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-0.11)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "45.4545454")


    def test_division_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-101)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "0.22772277")


    def test_division_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.11)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(13)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0084615")


    def test_division_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0.3)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-76.666666")


    def test_division_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.007)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(-0.0023)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults()[0:10], "-3.0434782")


    def test_division_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannot divide by zero")


    def test_division_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannot divide by zero")


    def test_division_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.17)
        self.driver.find_element(by="accessibility id", value="divideButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "Cannot divide by zero")


    def test_inverse_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "Cannot divide by zero")


    def test_inverse_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "1")


    def test_inverse_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(9)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "0.11111111")


    def test_inverse_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "0.1")


    def test_inverse_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(11)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "0.09090909")


    def test_inverse_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "0.01010101")


    def test_inverse_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "0.01")


    def test_inverse_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "0.00100100")


    def test_inverse_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1000)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "0.001")


    def test_inverse_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-2)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "-0.5")


    def test_inverse_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-5)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "-0.2")


    def test_inverse_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-17)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0588235")


    def test_inverse_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0434782")


    def test_inverse_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-91)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0109890")


    def test_inverse_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-997)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0010030")


    def test_inverse_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1001)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual("{0:.7f}".format(float(self.getresults())), "-0.0009990")


    def test_inverse_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.3)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "3.33333333")


    def test_inverse_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.7)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "1.42857142")


    def test_inverse_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1.5)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "0.66666666")


    def test_inverse_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10.7)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "0.09345794")


    def test_inverse_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.9)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "0.00991080")


    def test_inverse_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.9)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-1.1111111")


    def test_inverse_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1.2)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.8333333")


    def test_inverse_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9.5)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.1052631")


    def test_inverse_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-12.2)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0819672")


    def test_inverse_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-120.4)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults()[0:10], "-0.0083056")


    def test_inverse_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(5)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "5")


    def test_inverse_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "0.1")


    def test_inverse_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "-23")


    def test_inverse_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-10.17)
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.driver.find_element(by="accessibility id", value="invertButton").click()
        self.assertEqual(self.getresults(), "-10.17")

    def test_percent_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-11)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-11.22")

    def test_percent_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-11)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(5)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-10.45")

    def test_percent_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-7)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(7)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-7.49")

    def test_percent_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-7)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(9)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-6.37")

    def test_percent_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-3)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-3.3")

    def test_percent_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-3)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(13)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-2.61")

    def test_percent_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(17)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-1.17")

    def test_percent_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(21)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-0.79")

    def test_percent_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(28)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")

    def test_percent_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(30)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0")

    def test_percent_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(41)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2.82")

    def test_percent_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(49)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "1.02")

    def test_percent_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(5)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(50)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "7.5")

    def test_percent_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(5)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(56)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "2.2")

    def test_percent_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(13)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(60)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "20.8")

    def test_percent_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(13)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(64)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "4.68")

    def test_percent_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(101)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(77)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "178.77")

    def test_percent_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(101)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(83)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "17.17")

    def test_percent_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-15.6)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(95)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-30.42")

    def test_percent_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-15.6)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-0.156")

    def test_percent_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-2.2)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-2.2022")

    def test_percent_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-2.2)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(0.5)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-2.189")

    def test_percent_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1.9)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(110)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-3.99")

    def test_percent_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1.9)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(110)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "0.19")

    def test_percent_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(6.9)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(150)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "17.25")

    def test_percent_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(6.9)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(200)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-6.9")

    def test_percent_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(18.1)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(500)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "108.6")

    def test_percent_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(18.1)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(1000)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "-162.9")

    def test_percent_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(150.9)
        self.driver.find_element(by="accessibility id", value="plusButton").click()
        self.click_num(-10)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "135.81")

    def test_percent_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(150.9)
        self.driver.find_element(by="accessibility id", value="minusButton").click()
        self.click_num(-50)
        self.driver.find_element(by="accessibility id", value="percentButton").click()
        self.driver.find_element(by="accessibility id", value="equalButton").click()
        self.assertEqual(self.getresults(), "226.35")

    def test_sequare_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "0")


    def test_sequare_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "1")


    def test_sequare_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(9)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "81")


    def test_sequare_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "100")


    def test_sequare_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(11)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "121")


    def test_sequare_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "9801")


    def test_sequare_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "10000")


    def test_sequare_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "998001")


    def test_sequare_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1000)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "1000000")


    def test_sequare_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-2)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "4")


    def test_sequare_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-5)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "25")


    def test_sequare_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-17)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "289")


    def test_sequare_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "529")


    def test_sequare_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-91)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "8281")


    def test_sequare_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-997)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "994009")


    def test_sequare_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1001)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "1002001")


    def test_sequare_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.3)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "0.09")


    def test_sequare_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.7)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "0.49")


    def test_sequare_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1.5)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "2.25")


    def test_sequare_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10.7)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "114.49")


    def test_sequare_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.9)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "10180.81")


    def test_sequare_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.9)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "0.81")


    def test_sequare_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1.2)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "1.44")


    def test_sequare_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9.5)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "90.25")


    def test_sequare_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-12.2)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "148.84")


    def test_sequare_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-120.4)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "14496.16")


    def test_sequare_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(5)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "625")


    def test_sequare_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "0.0001")


    def test_sequare_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(3)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "6561")


    def test_sequare_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.driver.find_element(by="accessibility id", value="xpower2Button").click()
        self.assertEqual(self.getresults(), "65536")

    def test_root_01(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "0")


    def test_root_02(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "1")


    def test_root_03(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(9)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "3")


    def test_root_04(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "3.16227766")


    def test_root_05(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(11)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "3.31662479")


    def test_root_06(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(99)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "9.94987437")


    def test_root_07(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "10")


    def test_root_08(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(999)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "31.6069612")


    def test_root_09(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1000)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "31.6227766")


    def test_root_10(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-2)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_11(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-5)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_12(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-17)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_13(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-23)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_14(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-91)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_15(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-997)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_16(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1001)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_17(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.3)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "0.54772255")


    def test_root_18(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.7)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "0.83666002")


    def test_root_19(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(1.5)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "1.22474487")


    def test_root_20(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(10.7)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "3.27108544")


    def test_root_21(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(100.9)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "10.0448992")


    def test_root_22(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-0.9)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_23(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-1.2)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_24(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-9.5)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_25(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-12.2)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_26(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(-120.4)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults(), "Invalid input")


    def test_root_27(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(5)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "1.49534878")


    def test_root_28(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(0.1)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "0.56234132")


    def test_root_29(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(3)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "1.14720269")


    def test_root_30(self):
        self.driver.find_element(by="accessibility id", value="clearButton").click()
        self.click_num(2)
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.driver.find_element(by="accessibility id", value="squareRootButton").click()
        self.assertEqual(self.getresults()[0:10], "1.04427378")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_standard_Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)