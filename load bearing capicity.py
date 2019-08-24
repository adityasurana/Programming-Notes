manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []
for cargo in manifest:
    print("debug: the weight is currently: {}".format(cargo_weight))
    if cargo_weight >= 100:
        print("debug: breaking loop now!")
        break
    else:
        print("debug: adding item: {}".format(cargo[1]))
        print("debug: with weight: {}".format(cargo[1]))
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
