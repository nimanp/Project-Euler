def maxPathSum(triangle):
   for i in range(len(triangle)-1, 0, -1):
      for j in range(0, i):
	 triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
   print triangle[0][0]
   
def main():
   triangle = []
   file = open("prob67.txt", "r")
   str = file.read()
   rows = str.splitlines()

   for line in rows: # create the array of lines in triangle
      curList = line.split(" ")
      for i in range(0, len(curList)):
	 curList[i] = int(curList[i])
      triangle.append(curList)
   
   maxPathSum(triangle)

main()
