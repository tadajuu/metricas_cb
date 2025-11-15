def get_rounded_total_value(total_value: float, people_count: float, decimal_precision: int) -> float:
  total_value_raw = total_value/people_count
  return round(total_value_raw, decimal_precision)

result = get_rounded_total_value(250,6,2)
print(result)