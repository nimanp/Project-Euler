def cubicPermutations():
   cubes = []
   nums = []
   for i in range(1, 10000):
      nums.append(i)
      cube = i**3
      cube = int("".join(sorted(str(cube), reverse = True)))
      cubes.append(cube)
      cubes.sort()

   for j in range(0, len(cubes)-5):
      if cubes[j] == cubes[j+4]:
	 print cubes[j]
	 break

cubicPermutations()
