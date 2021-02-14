


def read_file(filename): #read file
    lines =[]
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())#strip()去掉換行
    return lines


def chat_split(lines): #split chat
    new =[]
    for line in lines:
        line_split = line.split(' ', 1)#這邊切成兩部分(只切第一個空格)就好：['13:32Allen', '請問分公司代號是 9432 嗎']
        time = line_split[0][:5]
        name = line_split[0][5:]
        chat = line_split[1]
        new.append(time + ' ' + name + ' ' + chat)
    return new


def write_file(filename, new): #output file
    with open(filename, 'w', encoding='utf-8') as f: 
        for line in new:
            f.write(line + '\n') 


def main():
    lines = read_file('3.txt')
    new = chat_split(lines)
    write_file('3_split.txt', new)

main()