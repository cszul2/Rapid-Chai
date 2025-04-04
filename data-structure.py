import uuid

class AbstractObject:
    def __init__(self):
        self.id = uuid.uuid4()

class Project(AbstractObject):
    def __init__(self, name, status=None):
        super().__init__()
        self.name = name
        self.status = status
        self.members = list()

    def addProjectLead(self, lead):
        self.projectLead = lead

    def addMember(self, member):
        self.members.append(member)

    def addMembers(self, members):
        for member in members:
            self.addMember(member)

class Person(AbstractObject):
    def __init__(self, name):
        super().__init__()
        self.name = name