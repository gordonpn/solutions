def getTopToys(numToys, topToys, toys, numQuotes, quotes):
    """
    :type numToys: int
    :type topToys: int
    :type toys: List[str]
    :type numQuotes: int
    :type quotes: List[str]
    :rtype: List[str]
    """
    toys_data = {toy: [0, 0] for index, toy in enumerate(toys)}
    for quote in quotes:
        prev_toy = ""
        for toy in toys:
            found = False
            quote_split = quote.split()
            for quote_chunk in quote_split:
                if toy in quote_chunk.lower():
                    found = True
                    prev_toy = toy
                    toys_data.get(toy)[0] += 1
            if found:
                toys_data.get(prev_toy)[1] += 1

    data_list = list(toys_data.items())
    data_list.sort(key=lambda x: x[1][1], reverse=True)
    data_list.sort(key=lambda x: x[1][0], reverse=True)
    return [data_list[num][0] for num in range(topToys)]


numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
    "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
    "The new Elmo dolls are super high quality",
    "Expect the Elsa dolls to be very popular this year, Elsa",
    "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
    "For parents of older kids, look into buying them a drone",
    "Warcraft is slowly rising in popularity ahead of the holiday season",
]

print(getTopToys(numToys, topToys, toys, numQuotes, quotes))
