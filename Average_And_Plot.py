import os
import xlrd
import xlsxwriter
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def average(file_name):
    file_handler = os.open(file_name, os.O_RDONLY)
    workbook = xlsxwriter.Workbook(u'D:/Uob/Postgraduate/Class/Final_Project/Code/Test2/plot_reward.xlsx')
    print("create a new xlsx\n")
    table = workbook.add_worksheet(file_name)
    average_matrix = []
    f = open(file_handler, "r")
    cnt = 0
    average_cnt = 0
    for line in f.readlines():
        line = (line.strip())
        average_matrix.append(float(line))
        cnt = cnt + 1
        average_num = 0
        if cnt == 100:
            average_num = np.mean(average_matrix)
            print("average_num is " + str(average_num) + "，average_cnt is " + str(average_cnt) + "\n")
            average_matrix.clear()
            cnt = 0
            # table.write_row(average_cnt, 0, average_num)
            table.write(average_cnt, 0, average_num)
            average_cnt += 1

    workbook.close()



def plot(file):
    wb = xlrd.open_workbook(u'D:/Uob/Postgraduate/Class/Final_Project/Code/Test2/plot_backup.xlsx')
    sh = wb.sheet_by_name(file)
    print(sh.nrows)  # 有效数据行数
    print(sh.ncols)  # 有效数据列数
    print(sh.cell(0, 0).value)  # 输出第一行第一列的值
    print(sh.cell(0, 1).value)  # 输出第一行第二列的值

    x, y, z, n, p = [], [], [], [], []
    for i in range(0, sh.nrows):
        x.append(i)
        y.append(sh.cell(i, 0).value)
        z.append(sh.cell(i, 1).value)
        n.append(sh.cell(i, 2).value)
        p.append(sh.cell(i, 3).value)
    plt.plot(x, y, 'r', label='Original')
    plt.plot(x, z, 'y', label='Optimized')
    plt.plot(x, n, 'b', label='KSP-FF')
    plt.plot(x, p, color='black', label='SP-FF')
    plt.legend()
    # plt.plot(x, y)
    plt.xlabel('Ep x 100000')
    plt.ylabel('Blocking Probability')
    plt.title('OG VS OP')
    plt.show()
    # for i in range(sh.nrows):
        # print(sh.row_values(i))

def plot_rewards(file):
    wb = xlrd.open_workbook(u'D:/Uob/Postgraduate/Class/Final_Project/Code/Test2/plot_reward.xlsx')
    sh = wb.sheet_by_name(file)
    print(sh.nrows)  # 有效数据行数
    print(sh.ncols)  # 有效数据列数
    print(sh.cell(0, 0).value)  # 输出第一行第一列的值
    x, y = [], []
    for i in range(0, sh.nrows):
        x.append(i)
        y.append(sh.cell(i, 0).value)

    plt.plot(x, y, 'blue', label='Optimized')

    plt.legend()
    # plt.plot(x, y)
    plt.xlabel('Ep x 100000')
    plt.ylabel('Rewards')
    plt.title('Rewards MAP')
    plt.show()



if __name__ == "__main__":
    # average('rewards.dat')
    plot('BP.dat')
    #plot_rewards('rewards.dat')