
from ilovesyd import api

api = api.IloveSydAPI(api_key="krishhh")

def main():
    result = api.predict_pokemon("https://media.discordapp.net/attachments/1267308928946016340/1351882786956513290/pokemon.png?ex=67e09bb5&is=67df4a35&hm=0e5866663e47eefeeee7454f1c0f8084a0facefbb2de5dcdce035fe87f91908a&=&format=webp&quality=lossless&width=246&height=154")
    print(result)

main()