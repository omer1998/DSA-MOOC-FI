# class WordFinder:
#     grid=[]
#     def set_grid(self, grid):
#         self.grid = grid

#     def count(self, word):
#         return self.search_word(word)

#     def find_word_in_all_direction(self,row,col,word)->bool:
#         row_num= len(self.grid)
#         col_num= len(self.grid[0])

#         # all 8 direction; represented by two arrays 
#         # each direction combined by similar index of both array(list) 
#         # ex. (x_dir[0],y_dir[0]
#         x_dir = [-1,-1,-1,  0, 0,  1, 1, 1]
#         y_dir = [-1, 0, 1, -1, 1, -1, 0, 1]

#         word_length = len(word)
#         for i in range(len(x_dir)):
#             current_x = row + x_dir[i]
#             current_y = col + y_dir[i]

#             if current_x < 0 or current_x >= row_num or current_y < 0 or current_y >= col_num:
#                 break
            
#             if self.grid[current_x][current_y] == word[0]:
#                 break
#             c = 1
#             while c < word_length:
#                 if self.grid[current_x][current_y] != word[0]:
#                     break
#                     # now we need to see and check all the character in this direction
#                 current_x += x_dir[i]
#                 current_y += y_dir[i]
#                 c+= 1
#             if c == word_length:
#                 return True
#         return False
    
#     def search_word(self,word):
#         row_num = len(grid)
#         col_num = len(grid[0])
#         result= 0
#         for i in range(row_num):
#             for j in range(col_num):
#                 if self.find_word_in_all_direction(i,j,word):
#                     result+=1
#         return result
                
                




# if __name__ == "__main__":
#     grid = ["TIRATIRA",
#             "IRATIRAT",
#             "RATIRATI",
#             "ATIRATIR"]

#     finder = WordFinder()
#     finder.set_grid(grid)

#     print(finder.count("TIRA")) # 7 
#     print(finder.count("TA")) # 13
#     print(finder.count("RITARI")) # 3
#     print(finder.count("A")) # 8
#     print(finder.count("AA")) # 6
#     print(finder.count("RAITA")) # 0     

# Python program to search word in 2D grid in 8 directions

# This function searches for the given word
# in all 8 directions from the coordinate.
def search2D(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    # return false if the given coordinate
    # does not match with first index char.
    if grid[row][col] != word[0]:
        return False

    lenWord = len(word)

    # x and y are used to set the direction in which
    # word needs to be searched.
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    # This loop will search in all the 8 directions
    # one by one. It will return true if one of the
    # directions contain the word.
    for dir in range(8):

        # Initialize starting point for current direction
        currX, currY = row + x[dir], col + y[dir]
        k = 1

        while k < lenWord:

            # break if out of bounds
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break

            # break if characters dont match
            if grid[currX][currY] != word[k]:
                break

            # Moving in particular direction
            currX += x[dir]
            currY += y[dir]
            k += 1

        # If all character matched, then value of must
        # be equal to length of word
        if k == lenWord:
            return True

    # if word is not found in any direction,
    # then return false
    return False

# This function calls search2D for each coordinate


def count(grid, word):
    m = len(grid)
    n = len(grid[0])

    result = 0

    for i in range(m):
        for j in range(n):

            # if the word is found from this coordinate,
                    # then append it to result.
            if search2D(grid, i, j, word):
                result += 1

    return result




if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

   

    print(count(grid,"TIRA")) # 7 
    print(count(grid,"TA")) # 13
    print(count(grid,"RITARI")) # 3
    print(count(grid,"A")) # 8
    print(count(grid, "AA")) # 6
    print(count(grid,"RAITA")) # 0   

    # ans = count(grid, word)
    # print(ans)

    