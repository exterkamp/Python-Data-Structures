def calculate_edit_distance(str1, str2):
    '''
    Calculate the edit distance between two strings.

    An edit is defined as one of three actions, a deletion, 
    a replacement, or an addition.

    '''
    

    # operation enums
    MATCH, INSERT, DELETE = 0, 1, 2

    # three possible operations @ each point
    opt = [0,0,0]

    # 2D array to hold all edit distance data
    distance = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]
    # 2D array to hold parent least cost relationships
    parent = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]

    str1 = " " + str1
    str2 = " " + str2

    # initial values
    for i in range(len(str2)):
        distance[i][0] = i
        parent[i][0] = DELETE


    for j in range(len(str1)):
        distance[0][j] = j
        parent[0][j] = INSERT

    distance[0][0] = 0
    parent[0][0] = -1


    # go through every letter combination
    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            opt = [0,0,0]

            # populate with edit data
            if j > 0:
                opt[INSERT] = distance[i][j-1] + 1 # indel
            if i > 0:
                opt[DELETE] = distance[i-1][j] + 1 # indel
            if j > 0 and i > 0:
                opt[MATCH] = distance[i-1][j-1] + (0 if str1[j] == str2[i] else 1) # match or substitution

            # find min cost operation
            lowest_cost = min(opt)
            parent_opt = opt.index(lowest_cost)
            # print(opt, lowest_cost, parent_opt)
            distance[i][j] = lowest_cost
            parent[i][j] = parent_opt
    
    # for i in range(len(distance)):
    #     print(distance[i])
    # print('-----')
    # for i in range(len(parent)):
    #     print(parent[i])
    
    # traceback
    current_pos = (len(str2)-1, len(str1)-1)
    D,I,M,S = 'Delete','Insert','M','Substitute'
    trace_stack = []
    while parent[current_pos[0]][current_pos[1]] != -1:
        parent_val = parent[current_pos[0]][current_pos[1]]
        if parent_val == 0:
            if str2[current_pos[0]] == str1[current_pos[1]]:
                # trace_stack.append(M)
                pass
            else:
                trace_stack.append(S + ' ' + str1[current_pos[1]])

            current_pos = (current_pos[0]-1, current_pos[1]-1)
        elif parent_val == 1:
            trace_stack.append(I + ' ' + str1[current_pos[1]])
            current_pos = (current_pos[0], current_pos[1]-1)
            
        else:
            trace_stack.append(D + ' ' + str2[current_pos[0]])
            current_pos = (current_pos[0]-1, current_pos[1])
            
    return trace_stack[::-1]
  