import ctypes
import os


class CreditCalc:
    def __init__(self, credit_lib):
        self.expression: str = ""
        self.lib = ctypes.CDLL(os.path.abspath(credit_lib))
        self.lib.create_credit_calculator.restype = ctypes.POINTER(ctypes.c_void_p)
        self.lib.destroy_credit_calculator.argtypes = [ctypes.POINTER(ctypes.c_void_p)]

        self.lib.calculate_ann.argtypes = [ctypes.POINTER(ctypes.c_void_p),
                                           ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                           ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                           ctypes.POINTER(ctypes.c_double)]

        self.lib.calculate_diff.argtypes = [ctypes.POINTER(ctypes.c_void_p),
                                            ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                            ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                            ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int)]

        self.calculator = self.lib.create_credit_calculator()

    def calculate_ann(self, percents, months, summa):
        self.percents_result = ctypes.c_double()
        self.result = ctypes.c_double()
        self.monthly_pay = ctypes.c_double()
        self.lib.calculate_ann(self.calculator, percents, months, summa, ctypes.byref(self.percents_result),
                               ctypes.byref(self.result),
                               ctypes.byref(self.monthly_pay))
        return [
            self.result.value,
            self.percents_result.value,
            self.monthly_pay.value
        ]

    def calculate_diff(self, percents, months, summa):
        self.percents_result = ctypes.c_double()
        self.result = ctypes.c_double()
        self.monthly_pay = ctypes.c_double()
        monthly_payments = (ctypes.c_double * int(months))()
        num_payments = ctypes.c_int()
        number_of_iterations = self.lib.calculate_diff(self.calculator, percents, months, summa, ctypes.byref(self.percents_result),
                                ctypes.byref(self.result),
                                monthly_payments, ctypes.byref(num_payments))
        return [
            self.result.value,
            self.percents_result.value,
            num_payments.value,
            monthly_payments
        ]

    def __del__(self):
        self.lib.destroy_credit_calculator(self.calculator)
