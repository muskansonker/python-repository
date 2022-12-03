movies=['PK','Bahubali','The kashmir Files','Dhol']
stars=['⭐⭐','⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐','⭐⭐⭐']

for movie,star in zip(movies,stars):
    print(f'{movie:<16}{star}') #also use ljust but this is better