#  Cette classe permet de charger toutes les data afin d'être appelé dans différentes vues. CEla evitera la duplication de code


class DataManager:
    _data = None
    _model = None
    _X_reduced = None

    @classmethod
    def get_data(cls):
        if cls._data is None:
            try:
                cls._data = load_data()  # Remplacez par votre fonction de chargement réelle
            except Exception as e:
                print("Une erreur s'est produite lors du chargement des données.")
                print(str(e))
        return cls._data

    @classmethod
    def get_model(cls):
        if cls._model is None:
            try:
                cls._model = load_modele_machine_learning()  # Remplacez par votre fonction de chargement réelle
            except Exception as e:
                print("Une erreur s'est produite lors du chargement du modele de machine learning.")
                print(str(e))
        return cls._model

    @classmethod
    def get_X_reduced(cls):
        if cls._X_reduced is None:
            try:
                cls._X_reduced = load_X_reduced()  # Remplacez par votre fonction de chargement réelle
            except Exception as e:
                print("Une erreur s'est produite lors du chargement de X_reduced.")
                print(str(e))
        return cls._X_reduced
