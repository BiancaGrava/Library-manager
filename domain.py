class Carte:
    def __init__(self,id,titlu,autor,anap):
        self.__id=id
        self.__titlu=titlu
        self.__autor=autor
        self.__anap=anap

    def get_id(self):
        """Getter method"""
        return self.__id

    def get_titlu(self):
        """Getter method"""
        return self.__titlu

    def get_autor(self):
        """Getter method"""
        return self.__autor

    def get_anap(self):
        """Getter method"""
        return self.__anap

    def set_id(self,id):
        """Setter method"""
        self.__id=id

    def set_titlu(self,titlu):
        """Setter method"""
        self.__titlu=titlu

    def set_autor(self,autor):
        """Setter method"""
        self.__autor=autor

    def set_anap(self,anap):
        """Setter method"""
        self.__anap=anap

    def __str__(self):
        """Convert to string method"""
        return f"{self.__id},{self.__titlu},{self.__autor},{self.__anap}"

    def __eq__(self, other):
        return self.__id==other.get_id()

def test_create():
    carte=Carte(12,"Ana","Maricela",2000)
    assert carte.get_id()==12
    assert carte.get_titlu()=="Ana"
    assert carte.get_autor()=="Maricela"
    assert carte.get_anap() == 2000

def test_change():
    carte = Carte(12, "Ana", "Maricela", 2000)
    carte.set_id(13)
    assert carte.get_id()==13




