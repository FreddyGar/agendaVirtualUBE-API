class TipoCita:
    def __init__(self, id_tipo_cita, nombre_tipo_cita, descripcion):
        self.id_tipo_cita = id_tipo_cita
        self.nombre_tipo_cita = nombre_tipo_cita
        self.descripcion = descripcion

    @staticmethod
    def from_dict(data):
        return TipoCita(
            data.get('id_tipo_cita'),
            data.get('nombre_tipo_cita'),
            data.get('descripcion')
        )
