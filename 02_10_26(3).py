tecnologias = {'Python', 'SQL', 'Git', 'Docker', 'Linux'}

tecnologias.add('FastAPI')
tecnologias.discard('SQL')

for item in tecnologias:
    print(item)

print(sorted(tecnologias))

backend = {'Python', 'SQL', 'Linux', 'Git'}
cloud = {'Docker', 'Linux', 'AWS', 'Terraform', 'Git'}

a = backend.union(cloud)
print(a)
b = backend.intersection(cloud)
print(b)
c = backend.difference(cloud)
print(c)
d = backend.symmetric_difference(cloud)
print(d)
