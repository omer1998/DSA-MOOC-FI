"""
The participants of a contest send in their solutions for tasks. 
 --> The tasks are numbered 1,2,3,..., and a solution for each task is worth 0-100 points.
 --> If a contestant submits multiple solutions to the same task, the score for the task is the maximum score of a single solution. 
 --> The total score of a contestant is the sum of scores over all tasks.

 --> Your task is to compile the score board of the contest containing 
     the name and the total score of each contestant. T
     
  --> The contestants are sorted by their score from the highest to the lowest. 
  --> If two contestants have the same score, the one that achieved this score first is listed higher. 
  --> If two or more participants have a score 0, they are listed in alphabetical order."""
class Contest:
    
    def __init__(self, names, task_count):
        self.names = names
        self.task_count = task_count
        self.scores_dict = {} # dict name -> task : max_score
        self.score_update_time = {} #dict name -> max_score:current_time
        self.current_time = 0
        

    def add_submission(self, name, task, score):
        if name not in self.scores_dict:
            
            self.scores_dict[name] = {task : score}
            self.score_update_time[name] = self.current_time
        
        prev_scor_task = self.scores_dict[name].get(task,0)
        
        if score > prev_scor_task:
            self.scores_dict[name][task] = score
            
            # track total score
            # total_score = sum(self.scores_dict[name].values())
            self.score_update_time[name] = self.current_time
        
        self.current_time +=1
            
        
        
        
    def create_scoreboard(self):
        # print(self.score_update_time)
        result = []
        for name in self.names:
            total_score = sum(self.scores_dict.get(name, {}).values())
            last_update_time = self.score_update_time.get(name, self.current_time +1 )
            result.append((total_score, last_update_time ,name))
        # print(result)
        sorted_result = sorted(result, key=lambda x: (-x[0], x[2] if x[0] == 0 else x[1], x[2]),  )
        return [(element[2], element[0]) for element in sorted_result]
            

if __name__ == "__main__":
    # names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    # contest = Contest(names, 3)

    # contest.add_submission("tiina", 2, 30)
    # contest.add_submission("pekka", 1, 40)
    # contest.add_submission("tiina", 1, 20)
    # contest.add_submission("pekka", 1, 50)
    # contest.add_submission("pekka", 2, 0)
    # contest.add_submission("eeva", 3, 100)
    # contest.add_submission("anna", 1, 0)
    # contest.add_submission("eeva", 3, 80)
    # contest.add_submission("tiina", 2, 30)

    # scoreboard = contest.create_scoreboard()
    # print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]
    names = ["kalle", "pekka", "eeva", "tiina"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 1, 0)
    contest.add_submission("kalle", 3, 77)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)