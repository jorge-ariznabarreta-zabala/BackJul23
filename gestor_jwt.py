import jwt
from functools import wraps
from flask import request, jsonify


# Función para verificar el token JWT en las solicitudes protegidas
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        secret= request.headers.get('Logindate')
        #print(secret, token)
        if not token:
            return jsonify({'error': 'Token de autorización faltante'}), 401
        try:
            #print(token)
            token = token.replace("Bearer", "").strip()
            #print("Token recibido:", token)
            data = jwt.decode(token, secret)
            #print("Token decodificado:", data)

            # Aquí podrías realizar más validaciones o verificar permisos adicionales si es necesario
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError as e:
            print("Error de token expirado:", e)
            return {'error: Token expirado': str(e)}, 401
        except jwt.InvalidTokenError as e:
            print("Error de token inválido:", e)
            return {'error: Token inválido ': str(e)}, 401
        except Exception as e:
            return {"Error en token_required": str(e)}, 500
    return decorated
