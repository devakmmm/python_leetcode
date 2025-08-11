# creating module newyork.py

from random import choice

capital = "Albany"
population = 19453561  # as of 2020 census
area = 54555  # in square miles 

def random_city():
    cities = ["New York City", "Buffalo", "Rochester", "Syracuse", "Albany"]
    
    index=choice("01234")

    print("Random city in New York:", cities[int(index)])