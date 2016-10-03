
def shift_people(danger, safety, is_lantern_safe, clock):
	if len(danger) == 0:
		return (clock, [])

	min_time = None
	min_chain = [	]
	if not is_lantern_safe:
		for i in range(len(danger)):
			for j in range(i + 1, len(danger)):
				i_time = danger[i]
				j_time = danger[j]
				travel_time = min(i_time, j_time)
				sub_danger = danger[:]
				sub_danger.remove(i_time)
				sub_danger.remove(j_time)
				sub_safety = safety + [i_time, j_time]
				print("Subs", sub_danger, sub_safety)
				total_time, sub_chain = shift_people(sub_danger,
																						 sub_safety, 
																						 not is_lantern_safe,
																						 clock + travel_time)
				print('subchain', sub_chain)
				if min_time is None or total_time < min_time:
					min_time = total_time
					min_chain = [(danger, safety)] + sub_chain
	else:
		for i in range(len(safety)):
			i_time = safety[i]
			sub_safety = safety[:]
			sub_safety.remove(i_time)
			sub_danger = danger + [i_time]
			print("Subs", sub_danger, sub_safety)
			total_time, sub_chain = shift_people(sub_danger, 
																					 sub_safety, 
															 						 not is_lantern_safe,
															 						 clock + i_time)
			print('subchain', sub_chain)
			min_time = min_time or total_time
			min_time = min(min_time, total_time)
			if min_time is None or total_time < min_time:
				min_time = total_time
				min_chain = [(danger, safety)] + sub_chain		

	return (min_time, min_chain)


danger_side = [1, 2, 5, 10]
safe_side = []
is_lantern_safe = False

print("Finally", shift_people(danger_side, safe_side, is_lantern_safe, 0))
