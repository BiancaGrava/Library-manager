class Consola:
    def __init__(self,service):
        self.__service=service
        self.__comenzi={
            "adauga" : self.__add_ui,
            "sterge" :self.__del_ui,
            "modifica filtru":self.__mod_f_ui,
            "filtreaza":self.__filter_ui,
            "undo":self.__undo
        }

    def __add_ui(self,params):
        if len(params)!=4:
            raise Exception("numar parametri incorect!\n")
        else:
            try:
                id=int(params[0])
                titlu=params[1]
                autor=params[2]
                anap=int(params[3])
                self.__service.add_srv(id,titlu,autor,anap)
                print("adaugare efectuata cu succes!\n")
            except ValueError:
                raise ValueError("id nu e intreg!\n")
            except Exception as ex:
                raise Exception(ex)

    def __del_ui(self,params):
        if len(params)!=1:
            raise Exception("nr parametri incorect!\n")

        else:
            try:
                cifra=int(params[0])
                self.__service.del_srv(cifra)
                print("stergere efectuata cu succes!\n")
            except Exception as ex:
                raise Exception(ex)

    def __mod_f_ui(self,params):
        if len(params)!=2:
            raise Exception("nr parametri incorect!\n")

        else:
            try:
                titlu=params[0]
                anap=int(params[1])
                self.__service.modify_filter(titlu,anap)
                print("filtrul a fost schimbat!\n")
            except Exception as ex:
                raise Exception(ex)


    def __filter_ui(self,params):
        if len(params)!=0:
            raise Exception("nr parametri incorect!\n")
        else:
            try:
                lista=self.__service.filter()
                for carte in lista:
                    print(str(carte)+"\n")

            except Exception as ex:
                raise Exception(ex)

    def __undo(self,params):
        if len(params)!=0:
            raise Exception("nr parametri incorect!\n")
        else:
            try:
                #print(self.__service.undo(self.__history))
                for carte in self.__service.undo(self.__service._history):
                    print(str(carte)+"\n")
            except Exception as ex:
                if str(ex)=="list index out of range":
                    raise Exception("nu exista operatii mai vechi efectuate in aceastra rulare!\n")
                else:
                    raise Exception(ex)

    def run(self):
        while True:
            ui=input(">>>")
            ui=ui.strip()
            if ui=="exit":
                return
            else:
                parts=ui.split(">")
                nume=parts[0]
                nume=nume.strip()
                if len(parts)==1:
                    params=[]
                else:
                    params=parts[1].strip().split(",")

                if nume in self.__comenzi:
                    try:
                        self.__comenzi[nume](params)
                    except Exception as ex:
                        print(ex)

                else:
                    print("numele comenzii nu e cunoscut!\n")
