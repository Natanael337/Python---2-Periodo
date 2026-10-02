data_scientist = {'Python', 'Javascript', 'Git', 'C#'}
data_engineer = {'JAVA', 'Python', 'COBOL', 'C#', 'RUBY'}

uniao = data_scientist.union(data_engineer)
print(uniao)
intersection = data_scientist.intersection(data_engineer)
print(intersection)
diferenca = data_scientist.difference(data_engineer)
print(diferenca)
diferenca_simetrica = data_scientist.symmetric_difference(data_engineer)
print(diferenca_simetrica)
