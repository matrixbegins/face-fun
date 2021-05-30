import os, json, boto3, base64, shortuuid, traceback

from datetime import datetime, timedelta
from time import time
from PIL import Image
from io import BytesIO
from face_handler import FaceHandler
from object_handler import ObjectDetector

from constants import get200Response, get400Response, get50XResponse, getAPIGateWayKey, get401Response, getResponse200NoObject

BUCKET_NAME = os.getenv("BUCKET_NAME")
PREFIX = "thumbnails"
thumb_size = (50, 50)

img_domain = "https://d2fp043e7v1132.cloudfront.net/"


def upload_handler(event, context):
    print("event obj:: ", event)

    validate_request(event)

    file_content = base64.b64decode(event['body'])
    try:
        if not validate_file(event):
            return get400Response("Invalid file format! Supported types JPG and PNG.")

        # now resize Image for s3 and create Image URL
        resized_img = resize_image(file_content, thumb_size)

        # upload to S3
        upload_path = create_s3_key()
        upload_response = put_s3_object(upload_path, resized_img)
        print("S3 upload response:: ", upload_response)

        # now we are ready for amazon rekognition call
        obj_detection_response = get_object_rekognition_data(file_content, upload_path)

        return build_response(upload_path, obj_detection_response)

    except FileNotFoundError as no_face:
        print('FileNotFoundError:: ',no_face)

        return getResponse200NoObject()

    except Exception as err:
        traceback.print_exception(None, err, err.__traceback__)
        return get50XResponse()



def validate_file(event:dict):
    try:
        content_type = event.get("headers").get("content-type")

        supported_types = [ "image/jpeg", "image/jpg", "image/png" ]
        return False if content_type not in supported_types else True

    except Exception as err:
        traceback.print_exception(None, err, err.__traceback__)
        return False


def put_s3_object(target_key, payload):
    # init boto3 client
    client = boto3.client('s3')

    expdate = datetime.now() + timedelta(days=15)
    return client.put_object(
            Body=payload,
            Bucket=BUCKET_NAME,
            Key=target_key,
            ContentType="image",
            CacheControl="public, max-age=31536000",
            Expires=expdate
        )


def create_s3_key():
    return f"{PREFIX}/{shortuuid.uuid()}.jpg"


def resize_image(image, size_vector):
    img = Image.open(BytesIO(image)).convert('RGB')
    payload = BytesIO()
    img.thumbnail( size_vector, Image.ANTIALIAS )
    img.save( payload, format="jpeg",optimize=True, quality=80)
    payload.seek(0)

    return payload


def get_rekognition_data(image, img_name):
    face_request = FaceHandler(image, img_domain)

def get_object_rekognition_data(image, image_name):
    obj_request = ObjectDetector(image, image_name)
    return obj_request.getLabelList()


def validate_request(event):
    httpMethod = event.get('requestContext').get('http').get('method')
    print('httpMethod', httpMethod)

    if httpMethod.upper() == 'OPTIONS':
        return get200Response()

    api_key = event.get('headers').get('ff-api-key')
    print(api_key, 'api_key')

    if(api_key.upper() != getAPIGateWayKey()):
        return get401Response()


def build_response(upload_path, object_data):
    response = get200Response()
    # prepare message
    msg = "Labels found: " + ", ".join(object_data)
    responseBody = {
        "status": "success",
        "image_url": img_domain + upload_path,
        "timestamp": int(time()*1000000),
        "message": msg
    }
    response['body'] = json.dumps(responseBody)

    return response


if __name__ == "__main__":
    event = {
            "version": "2.0",
            "routeKey": "POST /face_upload",
            "rawPath": "/face_upload",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "content-length": "1634",
                "content-type": "image/jpeg",
                "host": "6o0-1.amazonaws.com",
                "user-agent": "curl/7.64.1",
                "x-amzn-trace-id": "Root=1-602cf8d5-0b6bfa9024nyde51bf4180a3d7",
                "x-forwarded-for": "XX.XX.XX.XX",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https",
                "ff-api-key": "D3U3DNGD6C"
            },
            "requestContext": {
                "accountId": "7e99988",
                "apiId": "c7e9",
                "domainName": "6o0-south-1.amazonaws.com",
                "domainPrefix": "6oe9",
                "http": {
                    "method": "POST",
                    "path": "/face_upload",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "103.204.134.77",
                    "userAgent": "curl/7.64.1"
                },
                "requestId": "a4vRWjFmhcwEPNg=",
                "routeKey": "POST /face_upload",
                "stage": "$default",
                "time": "17/Feb/2021:11:07:01 +0000",
                "timeEpoch": 1613560021374
            },
            "body": "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",
            "isBase64Encoded": True
        }


    print("MAIN::", upload_handler(event, {}) )

