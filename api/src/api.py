import hug

api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, allow_origins=["*"]))

#Minhas rotas


