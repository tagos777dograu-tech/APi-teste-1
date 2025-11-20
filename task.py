class task:
    def __init__(self,id,title,description,completada=False):
        self.id = id
        self.title = title
        self.description = description
        self.completada = completada
    
    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "completada":self.completada
        }
