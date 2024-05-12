import random

print(random.random())
print(random.randint(0, 100))
print(random.choice(['a', 'b', 'c']))
print(random.choices(['a', 'b', 'c'], k=2))

m_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.shuffle(m_list))
print(m_list)
random.shuffle(m_list)
print(m_list)

print(''.join(random.choices('0123456789', k=8)))
