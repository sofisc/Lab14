from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):

        self._grafo = nx.DiGraph()
        self._idMap={}

    def getAllStore(self):
        return DAO.getAllStore()

    def creaGrafo(self, store):
        self._grafo.clear()
        self._ordini = DAO.getAllOrdini(store)
        for o in self._ordini:
            self._idMap[o.order_id] = o
        self._grafo.add_nodes_from(self._ordini)

    def getNumNodi(self):
        return len(self._grafo.nodes)
