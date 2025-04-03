class Perfil:
    def __init__(self, id_perfil, nombre_perfil, descripcion, fecha_creacion):
        self.id_perfil = id_perfil
        self.nombre_perfil = nombre_perfil
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion

    @staticmethod
    def from_dict(data):
        return Perfil(
            data.get('id_perfil'),
            data.get('nombre_perfil'),
            data.get('descripcion'),
            data.get('fecha_creacion')
        )
