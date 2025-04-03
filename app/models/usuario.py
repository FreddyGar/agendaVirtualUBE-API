class Usuario:
    def __init__(self, id_usuario, nombre, apellido, email, contrasena, telefono, estado):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.telefono = telefono
        self.estado = estado

    @staticmethod
    def from_dict(data):
        return Usuario(
            data['id_usuario'], data['nombre'], data['apellido'],
            data['email'], data['contrasena'], data['telefono'], data['estado']
        )

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "estado": self.estado,
            "ultima_sesion": "19/03/2025",  # si quieres ponerla fija por ahora
            "horario": "07:00 AM - 06:00 PM"  # también puedes ponerlo así
        }