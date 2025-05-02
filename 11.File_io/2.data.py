with open("C:\\Users\\Pavish\\Python\\class\\10.Functions\\Data.csv","r") as csv_file:
    data_dict={}
    for line in csv_file:
        data=line.split(sep=",",maxsplit=1)
        data_dict.update({data[0]:[data[1]]})
    print(data_dict)