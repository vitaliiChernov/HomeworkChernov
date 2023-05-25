my_dict = {
    'Nechitailo Bogdan': {'Python', 'Java'},
    'Marhalov Volodimir': {'FrontEnd', 'FullStack'},
    'Bulat Sofiya': {'Python', 'FrontEnd'},
    'Kovalchuk Valerii': {'FrontEnd'}
    }

backEnd = {'Python', 'Java'}
for name, groups in my_dict.items():
    if len(groups) > 1:
        print('2 or more groups: ', name, groups)
    if 'FrontEnd' not in groups:
        print('no FrontEnd: ', name, groups)
    if backEnd & groups:
        print('backEnd: ', name, groups)
    



        