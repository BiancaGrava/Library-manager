from domain import Carte
from extras_reusable import cifre
class BiblioRepo:
    def __init__(self):
        self._carti=[]

    def add(self,carte):
        """
        adds a book to the list
        :param carte: book
        :return: modifies book list in memory
        """
        for cart in self._carti:
            if cart==carte:
                raise Exception("id ul exista deja!\n")

        self._carti.append(carte)

    def delete(self,cifra):
        """
        deletes all books which release year contains a digit given
        cifra:digit given
        return: modifies book list in memory by deleting accordingly
        """
        #self._carti=[]
        ok=0
        lista=[]
        for carte in self._carti:
            if cifra not in cifre(carte.get_anap()):
                lista.append(carte)
            else:
               ok=1
        if ok==0:
            raise Exception("nu s-a sters nimic!\n")
        self._carti = []
        self._carti=lista
    def get_all(self):

        lista=[x for x in self._carti]
        if lista==None:
            return []
        return lista
class BiblioFileRepo(BiblioRepo):
    def __init__(self,filename):
        BiblioRepo.__init__(self)
        self.__filename=filename

    def __load_from_file(self):
        """
        reads all the books from the file to the list of books
        :return: modifies the book list
        """
        self._carti=[]
        with open(self.__filename,"r") as f:
            lines=f.readlines()
            for line in lines:
                if line!="":
                    parts=line.strip().split(",")
                    id=int(parts[0])
                    titlu=parts[1]
                    autor=parts[2]
                    anap=int(parts[3])
                    carte=Carte(id,titlu,autor,anap)
                    self._carti.append(carte)

    def __write_to_file(self):
        """
        writes all the books to file(exports list of books)
        :return: modifies file
        """
        with open(self.__filename, "w") as f:
            for carte in self._carti:
                f.write(str(carte)+"\n")

    def golire(self):
        self._carti=[]
        with open(self.__filename, "w") as f:
            f.write("")

    def add(self,carte):
        """
                adds a book to the list
                :param carte: book
                :return: modifies list in file
                """
        self.__load_from_file()
        BiblioRepo.add(self,carte)
        self.__write_to_file()

    def delete(self,cifra):
        """
                deletes all books which release year contains a digit given
                cifra:digit given
                return: modifies book list in file by deleting accordingly
                """
        self.__load_from_file()
        BiblioRepo.delete(self,cifra)
        self.__write_to_file()

    def get_all(self):
        """Gets all books from file"""
        self.__load_from_file()
        return BiblioRepo.get_all(self)

def test_add_get__all():
    repo = BiblioFileRepo("carti_test.txt")
    repo.golire()
    assert repo.get_all()==[]
    carte = Carte(15, "ana", "maria", 2002)
    repo.add(carte)
    assert repo.get_all()==[carte]
test_add_get__all()

def test_del():
    repo = BiblioFileRepo("carti_test.txt")
    repo.golire()
    assert repo.get_all()==[]
    carte = Carte(15, "ana", "maria", 2002)
    repo.add(carte)
    carte1 = Carte(16, "ana", "maria", 1999)
    repo.add(carte1)
    assert repo.get_all()==[carte,carte1]
    repo.delete(2)
    assert repo.get_all() == [carte1]
test_del()