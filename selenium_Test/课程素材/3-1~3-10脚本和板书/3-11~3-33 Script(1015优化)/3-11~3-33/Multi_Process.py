from time import ctime,sleep
import multiprocessing

#定义两个方法说和写
def talk(content,loop):
    for i in range(loop):
        print("Talk: %s %s" %(content,ctime()))
        sleep(2)

def write(content, loop):
    for i in range(loop):
        print("write: %s %s" % (content, ctime()))
        sleep(3)

#定义两个进程
process=[]
p1=multiprocessing.Process(target=talk,args=('hello,51zxw',2))
process.append(p1)

p2=multiprocessing.Process(target=write,args=('Python',2))
process.append(p2)

#调用进程
if __name__=='__main__':
    for p in process:
        p.start()
    for p in  process:
        p.join()
    print("All process is Run! %s" %ctime())