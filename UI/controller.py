import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handleCreaGrafo(self, e):
        store= self._view._ddStore.value
        if store is None or store == "":
            self._view.create_alert("Selezionare lo store")
            return
        self._model.creaGrafo(str(store))
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text("Numero di nodi: "+ str(self._model.getNumNodi())))
        self._view.update_page()

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

    def storeSelected(self, e):
        store = self._view._ddStore.value
        if store is None or store == "":
            self._view.create_alert("Selezionare lo store")
            return

    def handle_store(self):
        self._view._ddStore.options.clear()
        for store in self._model.getAllStore():
            self._view._ddStore.options.append(ft.dropdown.Option(text=store.store_name, data=store))
        self._view.update_page()
