def get_value_per_person(total_spent: float, total_people: int) -> float:
  return total_spent / total_people

result = get_value_per_person(180, 4)
print(result)