  
def read_data(filename, train, variables): 
    f = open(filename, 'r')
    lines = f.read().split('\n')
    if train:
        columns = variables
    else:
        columns = variables[:-1]    

    data = list()

    for line in lines: 
        if line:
            values = {name: float(value) for name,value in zip(columns,line.split(','))}
            data.append(values)
    f.close()
    return data



