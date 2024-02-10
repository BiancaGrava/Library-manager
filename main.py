from repository import BiblioFileRepo
from service import BiblioSrv
from UI import Consola
def main():
    repo=BiblioFileRepo("carti.txt")
    serv=BiblioSrv(repo)
    cons=Consola(serv)
    cons.run()

main()
