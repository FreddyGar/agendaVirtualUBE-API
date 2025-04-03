class ModalidadCita:
    def __init__(self, id_modalidad, nombre_modalidad, descripcion):
        self.id_modalidad = id_modalidad
        self.nombre_modalidad = nombre_modalidad
        self.descripcion = descripcion

    @staticmethod
    def from_dict(data):
        return ModalidadCita(
            data.get('id_modalidad'),
            data.get('nombre_modalidad'),
            data.get('descripcion')
        )
class ModalidadCita:
    def __init__(self, id_modalidad, nombre_modalidad, descripcion):
        self.id_modalidad = id_modalidad
        self.nombre_modalidad = nombre_modalidad
        self.descripcion = descripcion

    @staticmethod
    def from_dict(data):
        return ModalidadCita(
            data.get('id_modalidad'),
            data.get('nombre_modalidad'),
            data.get('descripcion')
        )
