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
        self.task_score_dict ={}
        

    def add_submission(self, name, task, score):
        # we have two problem;
        # 1/ find the max score of this participat for specific task
        # 2/ get the total score for a participant across all tasks

        # for first problem; we could represent the data as dictionary of int (task number) : dictionary name:score
        if task in self.task_score_dict:
            # get the dictionarary that hold name:score of each participant of this task
            score_dict = self.task_score_dict[task]
            if name in score_dict:
                score_dict[name] = max(score_dict[name], score)
            else:
                score_dict[name] = score
                
            
        else:
            self.task_score_dict[task] = {name: score}
        
    def create_scoreboard(self):
        print(self.task_score_dict)
        result = []
        for name in self.names:
            total_score = 0
            for i in range(1, self.task_count +1):
                scores_dict = self.task_score_dict[i] # dict; name:score
                if name in scores_dict:
                    total_score += scores_dict[name]
            
            result.append((name,total_score))
        return sorted(result, key= lambda x: x[1], reverse=True)
            
            

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]