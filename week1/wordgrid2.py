class WordFinder:
    grid=[]
    def set_grid(self, grid):
        self.grid = grid
        # for i in range(len(grid)) :
        #     row = ""
        #     for l in range(len(grid[i])):
        #         row = row + grid[i][l]
        #     grid.append(row)
        # print(grid)

    def find_word_in_rows(self, word):
        result = 0
        w_length = len(word)
        # first lets find in horizontal direction accors all row of the grid
        for i in range(len(self.grid)):
            row = self.grid[i]
            reverse_row = row[::-1]
            # print("row")
            # print(row)
            # print(reverse_row)
            row_length= len(row)
            start_index= 0
            while start_index < row_length:
                if start_index + w_length <= row_length:
                    splited_row_word = row[start_index:start_index + w_length]
                    reverse_splited_row_word = reverse_row[start_index:start_index + w_length]
                   # print("splitted row word", splited_row_word)
                    if len(word) ==1 :
                        if splited_row_word == word :
                            result +=1
                    if (splited_row_word == word or reverse_splited_row_word == word) and len(word)>1:
                        result += 1
                start_index += 1
        # print(result)
        return result
                
    def find_word_in_columns(self, word):
        result = 0
        columns_length= len(self.grid[0])
        rows_number = len(self.grid)
        # print(rows_number)
        columns = []
        for r in range(columns_length):
            # print(i)
            column = ""
            for c in range(rows_number):
                column += self.grid[c][r]
            columns.append(column)
        # print(columns)
        for col in columns:
            result += self.find_word_in_sequence(word,col)
            result += self.find_word_in_sequence(word, col[::-1])
        # print(columns)
        # print(result)
        return result
    
    def get_digonal_axises(self):
        max_col = len(self.grid[0])
        max_row = len(self.grid)
        cols = [[] for _ in range(max_col)]
        rows = [[] for _ in range(max_row)]
        fdiag = [[] for _ in range(max_row + max_col - 1)]
        bdiag = [[] for _ in range(len(fdiag))]
        bdiag_str =[]
        min_bdiag = -max_row + 1

        for x in range(max_col):
            for y in range(max_row):
                cols[x].append(self.grid[y][x])
                rows[y].append(self.grid[y][x])
                fdiag[x+y].append(self.grid[y][x])
                bdiag[x-y-min_bdiag].append(self.grid[y][x])
        return [ "".join(i) for i in bdiag], [ "".join(i) for i in fdiag] 
    
    def find_word_in_digonal_axis(self, word):
        bdiag, fdiag = self.get_digonal_axises()
        # print(bdiag)
        # print(fdiag)
        result = 0
        for i in range(len(bdiag)):
            result += self.find_word_in_sequence(word,bdiag[i]) + self.find_word_in_sequence(word, fdiag[i])
            # if word in bdiag[i] or word in fdiag[i]:
            #     result +=1
        return result
                    
    def find_word_in_sequence(self, word, string):
        string_length = len(string)
        word_length = len(word)
        result = 0
        start_index = 0
        while start_index < string_length:
                if start_index + word_length <= string_length:
                    splited_row_word = string[start_index:start_index + word_length]
                   # print("splitted row word", splited_row_word)
                    if splited_row_word == word:
                        result += 1
                start_index += 1
        return result


    def count(self, word):
        if len(word)==1:
            return self.find_word_in_rows(word)
        count = self.find_word_in_columns(word) + self.find_word_in_rows(word) + self.find_word_in_digonal_axis(word)
        return count

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)
    # print(finder.grid)
    # print(finder.find_word_in_rows("TIRA"))
    # print(finder.find_word_in_columns("TIRA"))
    # bd, fd = finder.get_digonal_axises()
    # print(bd)
    # print(fd)
    # print(finder.find_word_in_rows("A"))
    # print(finder.find_word_in_columns("A"))
    # print(finder.find_word_in_digonal_axis("AA"))

    


    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0 