import unittest
from appium import webdriver

class Calculator_converter_Tests(unittest.TestCase):

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



    def getInput(self):
        """
        Get the display of Input
        Strip space, letters, and radix character
        :return: The display text
        """
        displaytext = self.driver.find_element("accessibility id", value="Value1").text
        displaytext = displaytext.strip("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm /-()")
        for j in displaytext:
            if j ==",":
                displaytext = displaytext.replace(",","")
        return displaytext

    def getOutput(self):
        """
        Get the result
        Strip space, letters, and radix character
        :return:
        """
        displaytext2 = self.driver.find_element("accessibility id", value="Value2").text
        displaytext2 = displaytext2.strip("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm /-()")
        for j in displaytext2:
            if j == ",":
                displaytext2 = displaytext2.replace(",", "")
        return displaytext2

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

    def test_currency_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Currency").click()
        self.assertEqual(self.get_header(), "Currency")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Australia\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("China\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "4730.85")

    def test_volume_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Volume").click()
        self.assertEqual(self.get_header(), "Volume")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Liters\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Cups\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "4226.753")

    def test_length_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Length").click()
        self.assertEqual(self.get_header(), "Length")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Meters\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Feet\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "3280.84")

    def test_weightandmass_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Weight").click()
        self.assertEqual(self.get_header(), "Weight and Mass")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Kilograms\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Ounces\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "35273.96")

    def test_temperature_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Temperature").click()
        self.assertEqual(self.get_header(), "Temperature")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Celsius\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Fahrenheit\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "1832")

    def test_energy_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Energy").click()
        self.assertEqual(self.get_header(), "Energy")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Joules\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Food calories\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "0.239006")

    def test_area_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Area").click()
        self.assertEqual(self.get_header(), "Area")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Square meters\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Acres\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "0.247105")

    def test_speed_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Speed").click()
        self.assertEqual(self.get_header(), "Speed")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Kilometers per hour\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Knots\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "540.0035")

    def test_time_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Time").click()
        self.assertEqual(self.get_header(), "Time")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Hours\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Days\r\t")
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "41.66667")

    def test_power_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Power").click()
        self.assertEqual(self.get_header(), "Power")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Watts\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Horsepower\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "1.341022")

    def test_data_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Data").click()
        self.assertEqual(self.get_header(), "Data")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Megabytes\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Gigabytes\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(100000)
        self.assertEqual(self.getInput(), "100000")
        self.assertEqual(self.getOutput(), "100")

    def test_pressure_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Pressure").click()
        self.assertEqual(self.get_header(), "Pressure")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Bars\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Pascals\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(1000)
        self.assertEqual(self.getInput(), "1000")
        self.assertEqual(self.getOutput(), "100000000")

    def test_angle_01(self):
        self.driver.find_element(by="accessibility id", value="TogglePaneButton").click()
        self.driver.find_element(by="accessibility id", value="Angle").click()
        self.assertEqual(self.get_header(), "Angle")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.driver.find_element(by="accessibility id", value="Units1").click()
        self.driver.find_element(by="accessibility id", value="Units1").send_keys("Degrees\r\t")
        self.driver.find_element(by="accessibility id", value="Units2").click()
        self.driver.find_element(by="accessibility id", value="Units2").send_keys("Radians\r\t")
        self.driver.find_element(by="accessibility id", value="ClearEntryButtonPos0").click()
        self.click_num(100)
        self.assertEqual(self.getInput(), "100")
        self.assertEqual(self.getOutput(), "1.745329")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_converter_Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)