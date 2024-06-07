from abc import ABC, abstractmethod

class InvalidCodeStructureError(Exception):
pass

class InvalidControlDigitError(Exception):
pass

class BarCodeValidator(ABC):
@abstractmethod
def check(self, code: str) -> bool:
pass

class LengthValidator(BarCodeValidator):
def check(self, code: str) -> bool:
return len(code) == 16

class CountryCodeValidator(BarCodeValidator):
def check(self, code: str) -> bool:
return code[:3].isalpha()

class ProductCodeValidator(BarCodeValidator):
def check(self, code: str) -> bool:
return code[3:16].isdigit()

class ControlDigitValidator(BarCodeValidator):
@staticmethod
def calculate_control_digit(code: str) -> int:
product_code = code[3:15] # First 12 digits after country code
odd_sum = sum(int(product_code[i]) for i in range(0, 12, 2))
even_sum = sum(int(product_code[i]) for i in range(1, 12, 2))
total_sum = odd_sum * 3 + even_sum
control_digit = (10 - (total_sum % 10)) % 10
return control_digit

def check(self, code: str) -> bool:
return int(code[-1]) == self.calculate_control_digit(code)

class BarCode:
def __init__(self, code: str):
self.code = code
self.validators = [
LengthValidator(),
CountryCodeValidator(),
ProductCodeValidator(),
ControlDigitValidator()
]

def validate(self) -> bool:
for validator in self.validators[:-1]:
if not validator.check(self.code):
raise InvalidCodeStructureError(f"Code {self.code} has an invalid structure.")
if not self.validators[-1].check(self.code):
raise InvalidControlDigitError(f"Code {self.code} has an invalid control digit.")
return True

# Ejemplo de uso
barcode = BarCode("ABC1234567890123")
try:
if barcode.validate():
print("El código de barras es válido.")
except (InvalidCodeStructureError, InvalidControlDigitError) as e:
print(e)
