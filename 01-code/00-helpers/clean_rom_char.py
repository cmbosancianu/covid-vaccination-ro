def fun_clean_rom_char(data, name):
    """Function which strips special Romanian characters from strings"""
    dict_rom_char = {'ș':'s',
                     'ş':'s',
                     'ț':'t',
                     'ţ':'t',
                     'ă':'a',
                     'â':'a',
                     'î':'i',
                     'Ș':'S',
                     'Ş':'S',
                     'Ț':'T',
                     'Ţ':'T',
                     'Ă':'A',
                     'Â':'A',
                     'Î':'I'}
    data[name] = data[name].replace(dict_rom_char, regex = True)
    return data