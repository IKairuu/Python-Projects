import datetime
import os

os.chdir("C:\\Users\\aband\\Downloads\\vsCode\\Python Projects\\Task Manager Project2.0")
class Background_Process:
    dictionary = {}
    dueTasks = []
    def __init__(self):
        self.process = Background_Process
        self.current_time = datetime.datetime.now()
        with open("nameTask.txt", "r") as nameFile, open("dayTask.txt", "r") as dayFile, open("markTask.txt") as markFile, \
            open("checkList.txt", "r") as checkFile, open("monthTask.txt", "r") as monthFile, open("yearTask.txt", "r") as yearFile:
                self.listName = [name.replace("\n", "") for name in nameFile]
                self.listDay = [day.replace("\n", "") for day in dayFile]
                self.listMark = [mark.replace("\n", "") for mark in markFile]
                self.listMonth = [month.replace("\n", "") for month in monthFile]
                self.listYear = [year.replace("\n", "") for year in yearFile]
                self.listCheck = [check.replace("\n", "") for check in checkFile]
        
    def save_files(self):
        with open("dayTask.txt", "w") as dayFile, open("markTask.txt", "w") as markFile, open("monthTask.txt", "w") as monthFile, \
            open("nameTask.txt", "w") as nameFile, open("yearTask.txt", "w") as yearFile, open("checkList.txt", "w") as checkFile:
                for index, x in enumerate(self.listName):
                    dayFile.write(str(self.listDay[index]) + "\n")
                    markFile.write(str(self.listMark[index]) + "\n")
                    monthFile.write(str(self.listMonth[index]) + "\n")
                    nameFile.write(str(self.listName[index]) + "\n")
                    yearFile.write(str(self.listYear[index]) + "\n")
                    checkFile.write(str(self.listCheck[index]) + "\n")
    def save_check(self):
        with open("checkList.txt", "w") as checkFile, open("markTask.txt", "w") as markFile:
           for index, x in enumerate(self.listMark):
               checkFile.write(str(self.listCheck[index]) + "\n")
               markFile.write(self.listMark[index] + "\n")
    def create_dictionary(self):
        for index, name in enumerate(self.listName):
            self.process.dictionary.update({name : int(self.listCheck[index])})
        return self.dictionary
            
    def due_tasks(self):
        if len(self.process.dueTasks) != 0:
            self.process.dueTasks.clear()  
        for index, x in enumerate(self.listName):
            if (int(self.listDay[index]) <= int(self.current_time.strftime("%d")) and int(self.listMonth[index]) <= int(self.current_time.strftime("%m")) and int(self.listYear[index]) <= int(self.current_time.strftime("%Y")) or \
            (int(self.listMonth[index]) < int(self.current_time.strftime("%m")) and int(self.listYear[index]) <= int(self.current_time.strftime("%Y"))) or (int(self.listYear[index]) < int(self.current_time.strftime("%Y")))) and \
            self.listMark[index] == "Undone":
                self.dueTasks.append({"name":self.listName[index], "day":int(self.listDay[index]),  "month":int(self.listMonth[index]), "year":int(self.listYear[index]), "mark":self.listMark[index]})
