// calculate.h
#ifndef CPP3_SMARTCALC_V2_0_1_SRC_BACKEND_CALCULATE_H
#define CPP3_SMARTCALC_V2_0_1_SRC_BACKEND_CALCULATE_H

#include <functional>
#include <stdexcept>
#include <unordered_map>
#include <stack>
#include <string>

#include "RPNConverter.h"

namespace s21 {
class Calculate {
 public:
  Calculate() = default;
  ~Calculate() = default;
  void Evaluate(const char* input_expression, int num_params, double x);
  double GetResult();

 private:
  void NumberProcessing(int &i, std::stack<double> &stack);
  static double Addition(double param_1, double param_2);
  static double Subtraction(double param_1, double param_2);
  static double Multiplication(double param_1, double param_2);
  static double Division(double param_1, double param_2);
  static double Mod(double param_1, double param_2);
  static double PowFunc(double param_1, double param_2);
  static double Sinus(double param_1);
  static double Cosinus(double param_1);
  static double Tangent(double param_1);
  static double Asinus(double param_1);
  static double Acosinus(double param_1);
  static double Atangent(double param_1);
  static double SquareRoot(double param_1);
  static double NaturalLogariphtm(double param_1);
  static double CommonLogariphtm(double param_1);
  static double MinusOne(double param_1);
  void PushValue(double x, int num_params);
  void ValidateForEvaluate(double (*func)(double, double));
  void ValidateForEvaluate(double (*func)(double));
  bool IsInf(double value);
  bool IsNan(double value);

 private:
  std::string token;
  std::stack<double> values;
  double result;
};
}  // namespace s21
std::string last_error_message;
extern "C" {
  s21::Calculate* create_calculator() {
    return new s21::Calculate();
  }

  void destroy_calculator(s21::Calculate* calc) {
    delete calc;
  }

  int evaluate(s21::Calculate* calc, const char* expr, int num_params, double x) {
    try {
      calc->Evaluate(expr, num_params, x);
      return 0;
    } catch (const std::exception &e) {
      last_error_message = e.what();
      return -1;
    }
  }

  double get_result(s21::Calculate* calc) {
    return calc->GetResult();
  }

  const char* get_last_error() {
     static std::string error_message_copy;
     error_message_copy = last_error_message;
     return error_message_copy.c_str();
  }
}
#endif
