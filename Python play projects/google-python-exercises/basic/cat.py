
import sys

def Cat(filename):
  f = open(filename,'rU')
  print 'f variable size: ', sys.getsizeof(f)
  for line in f:
    l = line
  print 'f variable size: ', sys.getsizeof(f)
  f.close()
  
def Cat2(filename):
  f = open(filename,'rU')  
  print 'f variable size: ', sys.getsizeof(f)
  lines = f.readlines()
  for line in lines:
    l=line
  print 'lines variable size: ', sys.getsizeof(lines)
  f.close()
  
def main():
  Cat(sys.argv[1])
  Cat2(sys.argv[1])
  
if __name__ == '__main__':
  main()
  