ration_weight = float(input())
daily_quantity = float(input())

remaining_ration = ration_weight - (daily_quantity * 6)
print(round(remaining_ration,4))