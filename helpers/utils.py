

file = "PyramidDescent/static/io/input_sample.txt"
def parse(file):
    samp = []
    with open(file) as f:
        for line in f:
            samp = line.split(",").append()
    return samp