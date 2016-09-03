def pg(intro, *outros, **pgs):
    print(intro)
    for outro in outros:
        print(outro)
    keys = sorted(pgs.keys())
    for key in keys:
        print(key, ":", pgs[key])

pgs = ['Python', 'Go', 'Scala', 'Ruby', 'Java', 'PHP', 'Clojure', 'C', 'C++', 'Perl', 'C#', 'JavaScript']

pg('どうぞ！', 'あうとろ１', 'あうとろ２', 'あうとろ３',
   p00=pgs[0],
   p01=pgs[1],
   p02=pgs[2],
   p03=pgs[3],
   p04=pgs[4],
   p05=pgs[5],
   p06=pgs[6],
   p07=pgs[7],
   p08=pgs[8],
   p09=pgs[9],
   p10=pgs[10],
   p11=pgs[11]
   )

print("=" * 100)

pg('Hey!', 'Out!', *pgs)