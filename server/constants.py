import json

response200 = {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': '*'
    },
    "body": json.dumps({
        "status": "success",
        "message": "Its working!"
    })
}

response200NoFace = {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': '*'
    },
    "body": json.dumps({
        "status": "error",
        "message": "Oops! I can't see you. Are you sure you are facing camera?"
    })
}

response200NoObject = {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': '*'
    },
    "body": json.dumps({
        "status": "error",
        "message": "Oops! I can't see you. Are you sure you are facing camera?"
    })
}

response400 = {
    "statusCode": 400,
    "headers": {
        "Content-Type": "application/json"
    },
    "body": ""
}

response50X = {
    "statusCode": 503,
    "headers": {
        "Content-Type": "application/json"
    },
    "body": json.dumps({
        "status": "error",
        "message": "We encountered an unrecoverable error! Please try again later."
    })
}

quote_dict = {
    "emotion": {
        "HAPPY": [
            "Hey happy human!",
        ],
        "SAD": [
            "Things will be alright.",

        ],
        "ANGRY": [
            "Hey there angry bird! just relax",
        ],

        "CONFUSED": [
            "I can remedy your confusion",
            "Quote2"
            "Quote3"
        ],

        "DISGUSTED": [
            "Relax its not that gross!",
        ],

        "SURPRISED": [
            "Surprise Surprise!!!",

        ],

        "CALM": [
            "Calm as a lake",
        ],

        "UNKNOWN": [
            "Don't really know what's going on with you.",
            "Quote2"
            "Quote3"
        ],

        "FEAR": [
            "Why fear me?",
        ],

    },

    "gender": {
        "MALE": [
            "Quote1",
            "Quote2"
            "Quote3"
        ],

        "FEMALE": [
            "Quote1",
            "Quote2"
            "Quote3"
        ],
    },
    "smile": [
            "Quote1",
            "Quote2"
            "Quote3"
        ],
    "eyeglasses": [
            "Quote1",
            "Quote2"
            "Quote3"
        ],

    "sunglasses": [
            "Quote1",
            "Quote2"
            "Quote3"
        ],

    "beard": [
            "Quote1",
            "Quote2"
            "Quote3"
        ],

    "mustache": [
            "Quote1",
            "Quote2"
            "Quote3"
        ]

}



def get200Response():
    return response200.copy()


def get400Response(msg: str = "Invalid request parameters!"):
    temp = response400.copy()
    temp["body"] = json.dumps({
        "status": "error",
        "message": msg
    })
    return temp


def get401Response(msg: str = "Not Authorized!"):
    resp = {
        "statusCode": 401,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "status": "error",
            "message": msg
            })
    }

    return resp


def get50XResponse():
    return response50X.copy()


def getNoFaceResponse():
    return response200NoFace.copy()


def getAPIGateWayKey():
    return "D3U3DNGD6C"


def getResponse200NoObject():
    return response200NoObject.copy()