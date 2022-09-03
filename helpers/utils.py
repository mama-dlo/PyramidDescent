pfile = "flaskr/static/io/input_sample.txt"

def line_check(line, l):
    line = line.lower()
    if l == 0:
        if line[:8] != 'target: ':
            return "Target not found."
    try: 
        return int(line[8:])
    except ValueError:
        return "ValueError. Floating points are not accepted as targets."


def parse(file):
    parsed_dict = {}
    target = 1
    with open(file) as f:
        for l, line in enumerate(f):
            if l == 0: # Does the check once
                target = line_check(line, l)
                if isinstance(target, str):
                    return f" Could not continue: {target}"
            if l > 0: # Begin dict population from here
                try:
                    parsed_dict[l] = [int(i.rstrip()) for i in line.split(',')]
                except ValueError as e:
                    return e
        parsed_dict[0] = int(target)
    return parsed_dict

print(parse(pfile))