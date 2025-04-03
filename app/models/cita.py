class Cita:
    def __init__(self, id_cita, id_solicitante, id_responsable, id_tipo_cita, id_modalidad,
                 fecha_hora_inicio, fecha_hora_fin, estado, notas):
        self.id_cita = id_cita
        self.id_solicitante = id_solicitante
        self.id_responsable = id_responsable
        self.id_tipo_cita = id_tipo_cita
        self.id_modalidad = id_modalidad
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin
        self.estado = estado
        self.notas = notas

    @staticmethod
    def from_dict(data):
        return Cita(
            data.get('id_cita'),
            data.get('id_solicitante'),
            data.get('id_responsable'),
            data.get('id_tipo_cita'),
            data.get('id_modalidad'),
            data.get('fecha_hora_inicio'),
            data.get('fecha_hora_fin'),
            data.get('estado'),
            data.get('notas')
        )
