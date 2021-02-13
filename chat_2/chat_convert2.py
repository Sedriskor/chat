
def read_file(filename): #read file
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #-sig為去編碼資料
        for line in f:
            lines.append(line.strip())
    return lines


def sum_words(lines): #sum things in lines
    person = None #將person一開始設成沒有
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0

    for line in lines:
        s = line.split(' ')#當遇到空白鍵切割
        time = s[0]
        name = s[1]
        word = s[2:] 
        #算到結尾值
        #[:2]=從頭算到2但結尾值[2]不含
        #[-2:]=從結尾值開始算抓最後2個
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)


    print('Allen傳了 %s 個字 %s 張貼圖 %s 張圖片' % (allen_word_count, allen_sticker_count, allen_image_count))
    print('Vikin傳了 %s 個字 %s 張貼圖 %s 張圖片' % (viki_word_count, viki_sticker_count, viki_image_count))


def write_file(filename, lines): #output file
    with open(filename, 'w', encoding='utf-8') as f: 
        for line in lines:
            f.write(line + '\n') 


def main():
    lines = read_file('LINE-Viki.txt')
    sum_words(lines)
    #write_file('output.txt', lines)

main()


