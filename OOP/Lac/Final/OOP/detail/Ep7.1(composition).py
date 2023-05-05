class Printer:
    def print_page(self, data):
        print("printing {}".format(data))


class Scanner:
    def scan_page(self):
        print("scanning...")


class Fax:
    def fax_page(self, number):
        print("faxing to {}".format(number))


class Aio:  # all in one printer
    def __init__(self, printer, scanner, fax):
        self.printer = printer
        self.scanner = scanner
        self.fax = fax

obj1 = Aio(Printer(), Scanner(), Fax())
obj1.printer.print_page("hello")
obj1.scanner.scan_page()
obj1.fax.fax_page("022185765")