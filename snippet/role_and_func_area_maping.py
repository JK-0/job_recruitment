    f1 = open(os.path.join(BASE_DIR, 'func_un.json'), encoding="utf8")
    f2 = open(os.path.join(BASE_DIR, 'role_un.json'), encoding="utf8")

    functional_area_data = json.load(f1)
    role_data = json.load(f2)

    print('00000000000000000000000000000000000000000000000000000000')
    for i in functional_area_data['data'].keys():
        functional_area =    FunctionalArea.objects.get(functional_area_name=functional_area_data['data'][i])
        # #id
        print('************Functional Area Start****************')
        print(i)
        # functional area name
        print(functional_area_data['data'][i])
        # pk
        print(functional_area.id)
        print('----------------------------')

        # map functional area with pk
        # print(role_data['data'].keys())
        for j in role_data['data'].keys():
            if(j == i):
                # #id
                print(j)

                # role_group & Role_name
                for k in role_data['data'][j].keys():

                    # role_group
                    if(k[0] != '#'):
                        print('group: '+ k)
                        for y in role_data['data'][j][k].keys():

                            # role_name
                            print('    role: ' + role_data['data'][j][k][y])
                            d = Role.objects.get_or_create(role_name=role_data['data'][j][k][y], role_group=k, functional_area=functional_area, verified=True)
                            print(d)
                    # role_name
                    else:
                        print('role: ' + role_data['data'][j][k])
                        u = Role.objects.get_or_create(role_name=role_data['data'][j][k], functional_area=functional_area, verified=True)
                        print(u)
                print('----------------------------------------------')

    f1.close()
    f2.close()
