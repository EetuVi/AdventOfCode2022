def get_lines(file, use_strings: bool = False, split=None):
    input_list = []
    lines = file.readlines()
    if len(lines) == 1 and split is not None:
        input_list = int(lines.split(split))
    else:
        for line in lines:
            if line == "\n":
                input_list.append(None)
            elif use_strings:
                if split is None:
                    input_list.append(line.strip())
                else:
                    input_list.append(line.rstrip().split(split))
            else:
                if split is None:
                    input_list.append(line.strip())
                else:
                    input_list.append([eval(i) for i in line.split(split)])
    return input_list
