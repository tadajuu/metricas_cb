def get_warriors_and_informant_gold(monster_drop: int, warriors_count: int) -> (int,int):
  warriors_gold = monster_drop // warriors_count
  informant_gold = monster_drop % warriors_count
  return warriors_gold, informant_gold

warriors_gold, informant_gold = get_warriors_and_informant_gold(50, 3)
print(warriors_gold)
print(informant_gold)