import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

inputfile = "input_hw1.txt"
outputfile = "106062523_hw1_output.txt"

fp = open(inputfile, "r") # Open input file
fp2 = open(outputfile, "w") # Open output file 

line = fp.readline().rstrip('\n') # Read the first line
while line:
    Path = [] # 起始地址 -> 地址1 -> 地址2 -> 地址3
    count = 0
    while line and count<=3: # 提前結束或到地址3
        Path.append(line)
    #     print(line)
        url = "https://www.blockchain.com/eth/address/" + line + "?view=standard"
    #     print(url)
        html = urlopen(url).read()
        soup = BeautifulSoup(html,"html.parser")
    #     print(soup)
        detail = soup.find('div', 'hnfgic-0 blXlQu').find_all('span', 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk')
    #     print(detail)
        detail2 = soup.find('div', 'hnfgic-0 blXlQu').find_all('span', 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh sc-1n72lkw-0 bKaZjn')

        # 把tag裡面的text抓出來
        L = []
        for d in detail:
            attr = d.text.strip()
    #         print(attr)
            L.append(attr)
        i = 0
        for d in detail2:   
            attr_name = d.text.strip()
            if i!= 0:
                fp2.write(attr_name+': '+ L[i] + '\n')
                print(attr_name+': '+ L[i] + '\n')
            i = i+1
        if soup.find_all('span', 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk sc-85fclk-0 gskKpd') == []: # 提前結束
            fp2.write('--------------------------------------------------------------------------'+'\n')
            print('--------------------------------------------------------------------------'+'\n')
            break
        Date = soup.find_all('span', 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk sc-85fclk-0 gskKpd')[-1].parent.parent.parent.parent.previous_sibling.previous_sibling.find('div', 'sc-1rk8jst-0 jKHeRh').text.strip()
        To = soup.find_all('span', 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk sc-85fclk-0 gskKpd')[-1].parent.parent.parent.parent.previous_sibling.find_all('a', 'sc-1r996ns-0 dEMBMB sc-1tbyx6t-1 gzmhhS iklhnl-0 dVkJbV')[-1].text.strip()
        Amount = soup.find_all('span', 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk sc-85fclk-0 gskKpd')[-1].text.strip()

        fp2.write('Date: '+ Date + '\n')
        fp2.write('To: '+ To + '\n')
        fp2.write('Amount: '+ Amount + '\n')
        fp2.write('--------------------------------------------------------------------------'+'\n')
        print('Date: '+ Date + '\n')
        print('To: '+ To + '\n')
        print('Amount: '+ Amount + '\n')
        print('--------------------------------------------------------------------------'+'\n')
        
        # 下一個地址
        line = To
        count = count +1 
    
    # 寫路徑 
    
    for node in Path:
        fp2.write(node)
        print(node)
        if node != Path[-1]:
            fp2.write(' -> ')
            print(' -> ')
    fp2.write('\n')
    print('\n')
    
    fp2.write('--------------------------------------------------------------------------'+'\n')
    print('--------------------------------------------------------------------------'+'\n')

    line = fp.readline().rstrip('\n') # Read the next line    

fp.close()  # Close input file
fp2.close() # Close outut file