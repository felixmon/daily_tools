# split text with multiple separators from a text file and write the result to a new text file,
# and export to excel file for further analysis.

import sys
import os
import re

# open the source file to read
f = open('1.txt','r')
# open the destination file to write
f2 = open('2.txt','w')
# state the list type variable 'result'
result=[]

# create empty dataframe
df = pd.DataFrame()

# read each line and split
# use regex split method to split with multiple separators
for item in f.readlines():
    result.append(re.split('，|。',item))

n = 0
j = 0

# write the result into new text file
# the reason that using two loops is that 'result' has two levels of list, and you cannot write a list directly to a text file, 
# or it will raise a Type error: TypeError: write() argument must be str, not list
for item in result:
    for item2 in item:
        df.loc[j,str(n)] = item2# row 0, col['0']; row 1, col['0']; row 2, col['0']...
        f2.write(item2)
        j += 1
        f2.write('\n')
    n += 1
    j = 0

# export to excel file
df.to_excel('1.xlsx')

# this script is to help fast split the long paragraph that need to be type into excel and analyze
# sample data:
'''

(1)2016-2019年6月，公司通过三井住友融资租赁(香港)有限公司融资购入41台设备，共计融资1,671,914.00美元及 81,631,516.00日元，截止2019年6月30日，公司尚未偿还融资款295,105.00美元及44,139,259.00日元。
(2)2017年-2018年12月，公司通过远东国际租赁有限公司融资购入23台设备，共计融资人民币12,223,306.00元，截止 2019年6月30日，公司尚未偿还融资贷款人民币3,318,773.00元。
(3)2018年-2019年6月，公司及全资子公司共同与前海兴邦金融租赁有限责任公司签订固定资产售后回租合同，共计 融资114,000,000.00元，截止2019年6月30日，公司尚未尚未偿还售后回租贷款人民币67,584,074.27元。
(4)2018年-2019年6月，公司通过中鑫国际融资租赁(深圳)有限公司融资购入24台设备，共计融资5,668,640.32元， 截止2019年6月30日，公司尚未偿还融资贷款2,834,820.16元。
(5)2018年-2019年6月，公司及全资子公司共同与中远海运租赁有限公司签订固定资产售后回租合同，共计融资人民 币170,000,000.00元。截止2019年6月30日，公司尚未偿还售后回租贷款人民币165,253,600.00元。
(6)2018年-2019年6月，公司与平安国际融资租赁有限公司签订固定资产售后回租合同，共计取得融资金额人民币 84,000,000.00元。截止2019年6月30日，公司尚未偿还融资款人民币56,796,334.60元。
(7)2018年8月-2018年12月，公司及全资子公司与海尔融资租赁有限公司签订固定资产售后回租合同，共计取得融资 金额人民币60,000,000.00元。截止2019年6月30日，公司尚未偿还售后回租贷款人民币53,847,929.08元。
(8)2008年-2019年6月，公司之控股公司Meta System S.p.A. 通过BANCA融资购入21台设备，共计融资5,059,995.00欧 元，截止2019年6月30日，公司尚未偿还融资款1,682,815.00欧元。
(9)2016-2019年6月，公司与中广核国际融资租赁有限公司签订固定资产售后回租合同，共计取得融资金额人民币 100,000,000.00元。截止2019年6月30日，公司尚未偿还售后回租赁款人民币8,905,669.09元。
(10)2019年5月，公司及全资子公司共同与海通恒信国际租赁股份有限公司签订固定资产售后回租合同，共计取得融 资金额人民币85,000,000.00元。截止2019年6月30日，公司尚未偿还售后回租贷款人民币87,548,700.00元。

'''
# output data

'''
(1)2016-2019年6月
公司通过三井住友融资租赁(香港)有限公司融资购入41台设备
共计融资1,671,914.00美元及 81,631,516.00日元
截止2019年6月30日
公司尚未偿还融资款295,105.00美元及44,139,259.00日元


(2)2017年-2018年12月
公司通过远东国际租赁有限公司融资购入23台设备
共计融资人民币12,223,306.00元
截止 2019年6月30日
公司尚未偿还融资贷款人民币3,318,773.00元


(3)2018年-2019年6月
公司及全资子公司共同与前海兴邦金融租赁有限责任公司签订固定资产售后回租合同
共计 融资114,000,000.00元
截止2019年6月30日
公司尚未尚未偿还售后回租贷款人民币67,584,074.27元


(4)2018年-2019年6月
公司通过中鑫国际融资租赁(深圳)有限公司融资购入24台设备
共计融资5,668,640.32元
 截止2019年6月30日
公司尚未偿还融资贷款2,834,820.16元


(5)2018年-2019年6月
公司及全资子公司共同与中远海运租赁有限公司签订固定资产售后回租合同
共计融资人民 币170,000,000.00元
截止2019年6月30日
公司尚未偿还售后回租贷款人民币165,253,600.00元


(6)2018年-2019年6月
公司与平安国际融资租赁有限公司签订固定资产售后回租合同
共计取得融资金额人民币 84,000,000.00元
截止2019年6月30日
公司尚未偿还融资款人民币56,796,334.60元


(7)2018年8月-2018年12月
公司及全资子公司与海尔融资租赁有限公司签订固定资产售后回租合同
共计取得融资 金额人民币60,000,000.00元
截止2019年6月30日
公司尚未偿还售后回租贷款人民币53,847,929.08元


(8)2008年-2019年6月
公司之控股公司Meta System S.p.A. 通过BANCA融资购入21台设备
共计融资5,059,995.00欧 元
截止2019年6月30日
公司尚未偿还融资款1,682,815.00欧元


(9)2016-2019年6月
公司与中广核国际融资租赁有限公司签订固定资产售后回租合同
共计取得融资金额人民币 100,000,000.00元
截止2019年6月30日
公司尚未偿还售后回租赁款人民币8,905,669.09元


(10)2019年5月
公司及全资子公司共同与海通恒信国际租赁股份有限公司签订固定资产售后回租合同
共计取得融 资金额人民币85,000,000.00元
截止2019年6月30日
公司尚未偿还售后回租贷款人民币87,548,700.00元
'''
