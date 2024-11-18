import ctypes


class SmartCalculator:
    def __init__(self, calc_lib):
        self.expression: str = ""
        self.calc_lib = ctypes.CDLL(calc_lib)
        self.calc_lib.create_calculator.restype = ctypes.POINTER(ctypes.c_void_p)
        self.calc_lib.evaluate.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p, ctypes.c_int,
                                           ctypes.c_double]
        self.calc_lib.get_result.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.calc_lib.get_result.restype = ctypes.c_double
        self.calc_lib.destroy_calculator.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.calc_lib.get_last_error.restype = ctypes.c_char_p
        self.calculator = self.calc_lib.create_calculator()

    # def set_calc_lib(self, path_to_calc_lib):
    #     self.calc_lib = ctypes.CDLL(path_to_calc_lib)

    def set_expression(self, expressions):
        self.expression = expressions

    def get_result(self, x_detecor=0, x=0.0):
        if not self.calc_lib.evaluate(self.calculator, self.expression.encode('utf-8'), x_detecor, x):
            result = self.calc_lib.get_result(self.calculator)
        else:
            result = self.calc_lib.get_last_error().decode('utf-8')
        return result

    def __del__(self):
        self.calc_lib.destroy_calculator(self.calculator)
