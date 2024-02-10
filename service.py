from domain import Carte
from repository import BiblioFileRepo
class BiblioSrv:
    def __init__(self,repo):
        self.__repo=repo
        self.__filtru_titlu=""
        self.__filtru_an=-1
        self._history=[self.get_all()]



    def add_srv(self,id,titlu,autor,anap):
        """takes data from ui and transmits it to repo for work
        for adding to the list of books
        id:id
        titlu:title
        autor:author
        anap:realese date
        modifies the book list in memory or file depending on the repo given
        """
        carte=Carte(id,titlu,autor,anap)
        try:
            self.__repo.add(carte)
            self._history.append(self.get_all())
        except Exception as ex:
            raise Exception(ex)

    def del_srv(self,cifra):
        """takes data from ui and transmits it to repo for work
        for deleting by digit in release year from the list of books
                cifra:cifra
                modifies the book list in memory or file depending on the repo given
                """
        try:
            self.__repo.delete(cifra)
            self._history.append(self.get_all())
        except Exception as ex:
            raise Exception(ex)

    def modify_filter(self,titlu,anap):
        """modifies the filter"""
        self.__filtru_titlu=titlu
        self.__filtru_an=anap

    def filter(self):
        """
        filters by age year and title
        :return: list filtered
        """

        carti=self.__repo.get_all()
        filtrata=[f"filtrul este: {self.__filtru_titlu},{self.__filtru_an}"]
        for carte in carti:
            if (self.__filtru_titlu in carte.get_titlu()) and carte.get_anap()<self.__filtru_an:
                filtrata.append(carte)
        return filtrata

    def undo(self,list):
        """returns the list before the last action"""
        list.pop()
        return list[len(list)-1]

    def get_all(self):
        """gets all from repo"""
        return self.__repo.get_all()

def test_add_get__all():
    repo = BiblioFileRepo("carti_test.txt")
    serv=BiblioSrv(repo)
    repo.golire()
    assert serv.get_all()==[]
    carte = Carte(15, "ana", "maria", 2002)
    serv.add_srv(15, "ana", "maria", 2002)
    assert repo.get_all() == [carte]
test_add_get__all()

def test_filter():
    repo = BiblioFileRepo("carti_test.txt")
    serv = BiblioSrv(repo)
    repo.golire()
    carte = Carte(15, "ana", "maria", 2002)
    serv.add_srv(15, "ana", "maria", 2002)
    serv.modify_filter("ana",2004)
    lista=serv.filter()
    assert lista==['filtrul este: ana,2004',carte]
test_filter()

def test_del():
    repo = BiblioFileRepo("carti_test.txt")
    serv = BiblioSrv(repo)
    repo.golire()
    carte = Carte(15, "ana", "maria", 2002)
    serv.add_srv(15, "ana", "maria", 2002)
    assert repo.get_all() == [carte]
    carte1 = Carte(17, "ana", "maria", 1999)
    serv.add_srv(17, "ana", "maria", 1999)
    serv.del_srv(0)
    assert serv.get_all()==[carte1]
test_del()

def test_undo():
    repo = BiblioFileRepo("carti_test.txt")
    serv = BiblioSrv(repo)
    repo.golire()
    carte = Carte(15, "ana", "maria", 2002)
    serv.add_srv(15, "ana", "maria", 2002)
    assert repo.get_all() == [carte]
    carte1 = Carte(17, "ana", "maria", 1999)
    serv.add_srv(17, "ana", "maria", 1999)
    assert repo.get_all() == [carte,carte1]
    assert serv.undo([[carte],[carte,carte1]])==[carte]
test_undo()

