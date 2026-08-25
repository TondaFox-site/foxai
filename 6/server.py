# =========================================================
# FOXAI V6
# ČÁST 3/4 — SERVER
# =========================================================

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# =========================================================
# ZÁKLADNÍ NASTAVENÍ
# =========================================================

PORT = 5000


# =========================================================
# TESTOVACÍ STAV SERVERU
# =========================================================

@app.get("/")
def home():

    return jsonify({
        "name": "FoxAI",
        "project": "TondaFox AI Project 1",
        "version": "6.0",
        "status": "online"
    })


# =========================================================
# AI ENDPOINT
# =========================================================

@app.post("/api/chat")
def chat():

    data = request.get_json(
        silent=True
    )

    if not data:

        return jsonify({
            "error": "Nebyla přijata data."
        }), 400


    message = data.get(
        "message",
        ""
    )


    history = data.get(
        "history",
        []
    )


    if not isinstance(
        message,
        str
    ):

        return jsonify({
            "error": "Zpráva musí být text."
        }), 400


    message = message.strip()


    if not message:

        return jsonify({
            "error": "Zpráva je prázdná."
        }), 400


    # =====================================================
    # DŮLEŽITÉ
    # =====================================================
    #
    # TADY BUDE SKUTEČNÝ AI MODEL.
    #
    # Záměrně sem nedávám falešné odpovědi.
    #
    # Pokud model není připojený, server NESMÍ
    # předstírat, že AI odpověděla.
    #
    # =====================================================


    return jsonify({

        "error":
            "FoxAI server je připraven, "
            "ale skutečný AI model ještě není připojen."

    }), 503


# =========================================================
# SPUŠTĚNÍ
# =========================================================

if __name__ == "__main__":

    print()
    print("🦊 FoxAI V6")
    print("TondaFox AI Project 1")
    print("----------------------------")
    print("Server: ONLINE")
    print("API: vlastní FoxAI endpoint")
    print("Port:", PORT)
    print("----------------------------")
    print()

    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=False
    )
  
