import os


full_str = ""
for ctr in range(134, len(os.listdir("C:/Users/vince/Desktop/book5_t/"))+1):
    f_name = 'C:\\Users\\vince\\Desktop\\book5_t\\{}.txt'.format(ctr)
    print(f_name)
    f = open(f_name, "r")
    m_str = f.read()
    m_str = m_str.split("\n")
    m_str2 = ""
    for i in range(0, len(m_str), 2):
        m_str2 += m_str[i]

    full_str += "".join(m_str)
    f.close()

f = open("C:\\Users\\vince\\Desktop\\book5_full.txt", "w")
f.write(full_str)
f.close()