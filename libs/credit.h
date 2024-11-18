#ifndef CPP3_SMARTCALC_V2_0_1_SRC_BACKEND_CREDIT_H
#define CPP3_SMARTCALC_V2_0_1_SRC_BACKEND_CREDIT_H
#include <cmath>
#include <ctime>
#include <iostream>
#include <vector>

inline constexpr int YEAR = 365;
inline constexpr int MONTHS_YEAR = 12;
namespace s21 {
enum Months {
  December,
  January,
  February,
  March,
  April,
  May,
  June,
  July,
  August,
  September,
  October,
  November
};

class CreditCalculator {
 public:
  CreditCalculator() = default;
  ~CreditCalculator() = default;
  void CalculateAnn(double percents, double months, double sum,
                    double &percents_result, double &result,
                    double &monthly_pay);

  int CalculateDiff(double percents, double months, double sum,
                    double &percents_result, double &result,
                    std::vector<double> &monthly_payments);
};
}  // namespace s21

extern "C" {
  s21::CreditCalculator* create_credit_calculator() {
    return new s21::CreditCalculator();
  }

  void destroy_credit_calculator(s21::CreditCalculator* calc) {
    delete calc;
  }

  int calculate_ann(s21::CreditCalculator* calc, double percents, double months, double sum,
                    double* percents_result, double* result, double* monthly_pay) {
    try {
      calc->CalculateAnn(percents, months, sum, *percents_result, *result, *monthly_pay);
      return 0;
    } catch (const std::exception &e) {
      return -1;
    }
  }

  int calculate_diff(s21::CreditCalculator* calc, double percents, double months, double sum,
                     double* percents_result, double* result, double* monthly_payments, int* num_payments) {
    try {
      std::vector<double> payments;
      int ret = calc->CalculateDiff(percents, months, sum, *percents_result, *result, payments);
      *num_payments = payments.size();
      for (int i = 0; i < *num_payments; ++i) {
        monthly_payments[i] = payments[i];
      }
      return *num_payments;
    } catch (const std::exception &e) {
      return -1;
    }
  }
}
#endif