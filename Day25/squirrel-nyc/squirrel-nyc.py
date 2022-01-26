import pandas

data = pandas.read_csv("squirrel.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(grey_squirrels)

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels)

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
