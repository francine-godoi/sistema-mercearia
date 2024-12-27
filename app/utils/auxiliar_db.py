import csv

class AuxiliarDB:

    @staticmethod
    def salvar_na_db(db_name: str, dados: list):
        with open(f"./db/{db_name}.csv", "a", newline="", encoding="utf-8") as csvfile:
            csv.writer(csvfile).writerow(dados)

    @staticmethod
    def pegar_dados_db(db_name: str):
        dados = []
        with open(f"./db/{db_name}.csv", encoding="utf-8") as csvfile:
            for x in csv.reader(csvfile):
                dados.append(x)
        return dados



if __name__ == "__main__":
    d = AuxiliarDB()
    dados = d.dados_db("produtos")
    print(sum(1 for x in dados))




