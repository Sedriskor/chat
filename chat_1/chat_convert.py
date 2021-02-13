
def read_file(filename): #read file
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #-sig為去編碼資料
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines): #convert into lines
    new = []
    person = None #將person一開始設成沒有
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue

        if person: #如果person有值 執行：
            new.append(person + ': ' + line)
    return new        

def write_file(filename, lines): #putput file
    with open(filename, 'w', encoding='utf-8') as f: 
        for line in lines:
            f.write(line + '\n') 

def main():
    lines = read_file('input.txt')
    print(lines)
    lines = convert(lines)
    print(lines)
    write_file('out.txt', lines)

main()


