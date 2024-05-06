my_scores = {
    'a': 10,
    'b': 7,
    'm': 14,
}

new_scores = {k: v * 10 for k, v in my_scores.items()}
scores_set = {v * 10 for k, v in my_scores.items()}
scores_list = [v * 10 for k, v in my_scores.items()]
scores_tuple = (v * 10 for k, v in my_scores.items())

print(my_scores)
print(new_scores)
print(scores_set)
print(type(scores_set))
print(scores_list)
print(type(scores_list))
print(scores_tuple)
print(tuple(scores_tuple))
print(type(scores_tuple))
