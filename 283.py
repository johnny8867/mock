#First try no problem:

#easy:
numbers1 = [1, 14, 20, 21, 27, 35, 1046, 66, 67, 100, 101, 104, 118, 119, 121, 125, 141, 144, 169, 202, 203, 217, 219, 226, 228, 232, 242,
 243, 252, 278, 283, 344, 346, 349, 350, 359, 367, 374, 383, 387, 409, 412, 414, 448, 485, 504, 509, 543, 561, 599, 653, 700, 704]

#medium:
numbers2 = [2, 3, 8, 11, 15, 28, 56, 57, 75, 98, 102, 122, 1167, 128, 129, 134, 150, 151, 155, 167, 189, 199, 200, 209, 215, 230, 235,
 238, 240, 253, 286, 438, 454, 513,525, 542]

#hard:
numbers3 = [42, 164, 239]

#one little error/one minor panic/'ran' a couple Wrong Answer
numbers4 = [16, 26, 33, 36, 37, 50, 53, 54, 69, 70, 72, 88, 94, 112, 133, 139, 145,191, 205, 224, 236, 259, 270, 288, 328, 415, 557, 605, 617, 622]


#not optimal solution (not good enough for interview)
numbers5 = [9, 13, 136, 142, 160, 173, 268, 347, 705]


#have some thoughts, but looked at solution to solve:
numbers6 = [5, 17, 19, 22, 34, 39, 49, '51','52', 61, 76,79, 83, 84, '105','106', 146, 170, 186, '206', 208, 211, 227, 234, 249, 295, 297, 408, 435, 449,
 487, 498, 538, 680, 702, 706, 707]


#No clue:
numbers7 = [24, 40, '46','47', 78, 95, 96, 108, 110, 114,'116','117', 120, 124, 147, 153, 154, 162, '207', '210', 225, 250, 337, 378, '394', 405, 426, 496, 669, 696]


#Will not know how to solve no matter how many times:
numbers8 = [4, 212, 218, 287, 309, 416, 489, 494, 560, 572, 606, 652, 658]

#Skipping:
#[bits questions] #solved on record: 137, 260, 338
#numbers9 = [89, 137, 190, 201, 260, 338, 371, 595]

#Mocked and good:
#20, 28, 42, 105, 155, 1046, 1167, 169, 108, 235, 208, 435, 116

#Mocked and no good:
print(len(numbers1)+len(numbers2)+len(numbers3))
print(len(numbers1)+len(numbers2)+len(numbers3)+len(numbers4)+len(numbers5)+len(numbers6)+len(numbers7)+len(numbers8)+3)
