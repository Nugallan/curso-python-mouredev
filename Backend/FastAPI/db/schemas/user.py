def user_schema(user) -> dict:  # Devuelve un diccionario con los datos del usuario
    return {"id": str(user["_id"]), # Este id es un ObjectId de MongoDB y hay que transformarlo a string
            "username": user["username"],
            "email": user["email"]}

def users_schema(users) -> list: # Devuelve una lista de diccionarios con los datos de los usuarios
    return [user_schema(user) for user in users] # Devuelve una lista de diccionarios
