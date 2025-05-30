import os

class TodoModel:
    def __init__(self, filePath: str):
        self.__filePath = filePath
        self.__tasks = []

    def saveTasks(self, tasks: list[str]):
        print("saveTasks erfolgreich aufgerufen!")
        with open(self.__filePath, "w", encoding="utf-8") as file:
            for i in range(len(tasks)):
                file.write(tasks[i])
            print("Tasks gespeichert!")

    def loadTasks(self):
        if os.path.exists(self.__filePath): # gleichbedeutend mit "./tasks.txt"
            print("Pfad: ", self.__filePath)
            with open(self.__filePath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.__tasks.append(line)
                print("Tasks geladen!")
    
    def getTasks(self):
        return self.__tasks
