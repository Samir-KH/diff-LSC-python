UP = "UP"
LEFT = "LEFT"
UP_LEFT = "UP_LEFT"

VALUE = "value"
ARROW = "arrow"
IS_CONNEXION = "is_connexion"

INDEX = "INDEX"

PLUS = "+"

MINUS = "-"

def make_connections_matrix(n, m):
    return [[0 for i in range(m)] for i in range(n)]



def fill_connections_matrix(connections_matrix,list1,list2,n,m):
    for i in range(n):
        for j in range(m):
            value = 0
            arrow = UP
            is_connexion = False

            if list1[i] == list2[j]:
                value = 1
                arrow = UP_LEFT
                if i > 0 and j == 0:
                    node = connections_matrix[i-1][j]
                    value = node[VALUE] +1
                elif i == 0 and j > 0 :
                    node = connections_matrix[i][j-1]
                    value = node[VALUE] +1
                elif i > 0 and j > 0:
                    node = connections_matrix[i-1][j-1]
                    value = node[VALUE] +1
            else:
                value = 0
                arrow = UP
                if i > 0 and j == 0:
                    node = connections_matrix[i-1][j]
                    vale = node[VALUE]
                elif i == 0 and j > 0 :
                    node = connections_matrix[i][j-1]
                    vale = node[VALUE]
                    arrow = LEFT
                elif i > 0 and j > 0:
                    node1 = connections_matrix[i-1][j]
                    node2 = connections_matrix[i][j-1]
                    value = max(node1[VALUE], node2[VALUE])
                    if node2[VALUE] == value :
                        arrow = LEFT
                
            new_node = {VALUE: value, ARROW: arrow}
            connections_matrix[i][j] = new_node

def back_track_connexions_matrix(connections_matrix,n,m):
    i = n - 1
    j = m - 1
    indexs_node_stack = []
    while i >= 0 and j >= 0:
        node = connections_matrix[i][j]
        if node[ARROW] == UP_LEFT:
            index_node = {INDEX : (i,j)}
            indexs_node_stack.append(index_node)
            i-=1
            j-=1
        elif node[ARROW] == UP:
            i-=1
        elif node[ARROW] == LEFT:
            j-=1
    return indexs_node_stack

def calulate_LSC(indexs_stack, list1):
    LSC = []
    length = len(indexs_stack)
    for i in range(length):
        index = indexs_stack[i][INDEX][0]
        LSC.insert(0, list1[index])
    return LSC


            
"""def calculate_plus_diff(LSC, list2, m, diff):
    index = 0
    for i in range(m):
        item_diff = ""
        if list2[i] == LSC[index]:
            index += 1
        else:
            item_diff = PLUS + list2[i]
            diff.insert(i ,item_diff)"""
        
def calculate__diff(LSC, list1, list2, n, m):
    diff = []
    list1_pointer = 0
    list2_pointer = 0
    length = len(LSC)
    for index in range(length):
        item_diff = ""
        while list1_pointer < n and list1[list1_pointer] != LSC[index]:
            item_diff = MINUS + list1[list1_pointer]
            diff.append(item_diff)
            list1_pointer+=1
        
        while list2_pointer < m and list2[list2_pointer] != LSC[index]:
            item_diff = PLUS + list2[list2_pointer]
            diff.append(item_diff)
            list2_pointer+=1
        
        diff.append(" " + LSC[index])
        list1_pointer+=1
        list2_pointer+=1
    while list1_pointer < n:
        item_diff = MINUS + list1[list1_pointer]
        diff.append(item_diff)
        list1_pointer+=1
    while list2_pointer < m:
        item_diff = PLUS + list2[list2_pointer]
        diff.append(item_diff)
        list2_pointer+=1
    return diff
        
    
def diff_algothim(lines_list1, lines_list2):
    n = len(lines_list1)
    m = len(lines_list2)
    connections_matrix = make_connections_matrix(n, m)
    fill_connections_matrix(connections_matrix,lines_list1,lines_list2, n, m)
    indexs_stack = back_track_connexions_matrix(connections_matrix,n,m)
    LSC = calulate_LSC(indexs_stack,lines_list1)
    diff = calculate__diff(LSC, lines_list1, lines_list2, n, m)
    return diff

def get_lines_list(file_name):
    list_lines = []
    with open(file_name, "r") as file:
        list_lines += file.readlines()
    return list_lines    

def diff(file1, file2):
    file1_lines = get_lines_list(file1)
    file2_lines = get_lines_list(file2)
    files_diff = diff_algothim(file1_lines, file2_lines)
    return files_diff

if __name__ == "__main__":
    import sys
    import os
    if len(sys.argv) == 1:
        exit(0)
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    print("-------------------------------------------" +"diff"+
          "-------------------------------------------")
    if not os.path.isfile(file1):
        print(file1, "file does not exist")
        exit(0)
    if not os.path.isfile(file2):
        print(file2, "file does not exist")
        exit(0)
    files_diff = diff(file1, file2)
    print("@ old file: " + file1)
    print("@ new file: " + file2)
    print("-------------------------------------------" +"----"+
          "-------------------------------------------")
    for i in files_diff:
        print(i, end = "")
            
"""
if __name__ == "__main__":
    list1 = ["A", "B", "C", "D", "E", "F", "K"]
    list2 = ["B", "H", "D", "E", "F", "C", "K"]

    #list1 = ["A", "B", "C", "D", "E", "F", "K"]
    #list2 = ["B", "H", "C", "D", "F", "C"]
    n = len(list1)
    m = len(list2)
    connections_matrix = make_connections_matrix(n, m)
    fill_connections_matrix(connections_matrix,list1,list2, n, m)
    indexs_stack = back_track_connexions_matrix(connections_matrix,n,m)
    LSC = calulate_LSC(indexs_stack,list1)
    diff = calculate__diff(LSC, list1, list2, n, m)
    print(connections_matrix)
    for i in connections_matrix:
       print( [ j[VALUE] for j in i])
    print("-------------------------")
    for i in connections_matrix:
       print( [ j[ARROW] for j in i])
    print("-------------------------")
    print( [ i[INDEX] for i in indexs_stack])
    print("-------------------------")
    print(LSC)
    print("-------------------------")
    for i in diff:
        print(i)"""
    
