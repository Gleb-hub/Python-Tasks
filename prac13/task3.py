class User:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    def authenticate(self, login_attempt, password_attempt):
        if self.login == login_attempt and self.password == password_attempt:
            return True
        else:
            return False

    def authorize(self, required_roles):
        if self.role in required_roles:
            return True
        else:
            return False


class Project:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def find_task_by_name(self, name):
        return [task for task in self.tasks if task.name == name]

    def find_task_by_start_date(self, start_date):
        return [task for task in self.tasks if task.start_date != start_date]

    def find_task_by_end_date(self, end_date):
        return [task for task in self.tasks if task.end_date == end_date]

    def is_completed(self):
        return all(task.status for task in self.tasks)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'tasks': [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        for task_data in data['tasks']:
            task = Task.from_dict(task_data)
            project.add_task(task)
        return project
    
class Task:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = False
        self.performers = []

    def change_status(self):
        self.status = not self.status

    def add_performer(self, performer):
        self.performers.append(performer)

    def remove_performer(self, performer):
        self.performers.remove(performer)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'status': self.status,
            'performers': self.performers
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        task.status = data['status']
        task.performers = data['performers']
        return task


def test_user():
    user = User('qwe', 'asd', 'a')
    assert (user.authenticate(user.login, user.password) is True)
    assert (user.authenticate('z', 'z') is False)
    assert (user.authorize(user.role) is True)
    assert (user.authorize('z') is False)


def test_project():
    project = Project('name', 'description', 'start', 'end')
    task1 = Task('a', 'a', 'a', 'a')
    task2 = Task('b', 'b', 'b', 'b')
    task3 = Task('c', 'c', 'c', 'c')
    project.add_task(task1)
    project.add_task(task2)
    project.add_task(task3)
    assert (project.find_task_by_name('b'))
    assert (project.find_task_by_start_date('b'))
    assert (project.find_task_by_end_date('b'))
    project.remove_task(task1)
    project.is_completed()
    project.tasks[0].change_status()
    project.tasks[1].change_status()
    project.is_completed()
    data = project.to_dict()
    project.from_dict(data)


def test_task():
    task = Task('a', 'a', 'a', 'a')
    task.change_status()
    task.add_performer('a')
    task.remove_performer('a')
