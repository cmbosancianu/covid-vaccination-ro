def fun_clean_uat_name(data, name):
    """Function which takes in an array of locality names and does standard cleaning tasks on them"""
    data[name] = data[name].str.title()
    data[name] = data[name].str.replace(' De ', ' de ')
    data[name] = data[name].str.replace(' Din ', ' din ')
    data[name] = data[name].str.replace(' Sub ', ' sub ')
    data[name] = data[name].str.replace(' Cel ', ' cel ')
    data[name] = data[name].str.replace(' Cu ', ' cu ')
    data[name] = data[name].str.replace(' La ', ' la ')
    data[name] = data[name].str.replace(' Lui ', ' lui ')
    data[name] = data[name].str.replace(' - ', '-')
    return data